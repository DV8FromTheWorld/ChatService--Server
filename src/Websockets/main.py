# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import asyncio
import json
import logging
import websockets
import events
import uuid
import datetime

logging.basicConfig()

CONNECTED_USERS = dict()

# Default channel created at server startup
CHANNELS = dict()

def rest_create_channel(channel_name: str):
    channel = {
        "id": str(uuid.uuid4()),
        "name": channel_name,
        "createdAt": str(datetime.datetime.now())
    }

    CHANNELS[channel["id"]] = channel

    return channel

async def dispatch_to_users(dispatch_event):
    if CONNECTED_USERS:  # asyncio.wait doesn't accept an empty list
        await asyncio.wait([user["connection"].send(dispatch_event) for user in CONNECTED_USERS.values()])


async def register_connection(user, websocket):
    CONNECTED_USERS[user["id"]] = {
        "user": user,
        "connection": websocket
    }
    await dispatch_to_users(events.user_connected_dispatch(user))


async def unregister_connection(user):
    del CONNECTED_USERS[user["id"]]
    await dispatch_to_users(events.user_disconnected_dispatch(user["id"]))


async def handle_connection(websocket, path):
    # register(websocket) sends user_event() to websocket
    # await register_connection(websocket)

    await websocket.send(events.identify_dispatch())

    user = None
    try:
        async for message in websocket:
            print("Event: " + message)
            event = json.loads(message)
            event_type = event["type"]
            if event_type == "IDENTIFY_RESPONSE":
                user = {
                    "id": event["data"]["id"],
                    "name": event["data"]["name"]
                }

                await register_connection(user, websocket)

                # Convert our Dict<userId, { connection: WS, user: UserDetails }> to Dict<userId, UserDetails>
                users = {user_id: user_connection_details["user"] for user_id, user_connection_details in CONNECTED_USERS.items()}

                await websocket.send(events.ready_dispatch(users, CHANNELS))
            elif event_type == "REST_CREATE_MESSAGE":
                message_content = event["data"]["content"]
                message_channel_id = event["data"]["channelId"]

                await dispatch_to_users(events.message_create_dispatch(user, message_channel_id, message_content))
            elif event_type == "REST_CREATE_CHANNEL":
                channel_name = event["data"]["name"]
                channel = rest_create_channel(channel_name)

                await dispatch_to_users(events.channel_create_dispatch(channel))
            else:
                logging.error("unsupported event: %s", event)
    except Exception as e:
        print(e.with_traceback())

    finally:
        if user is not None:
            await unregister_connection(user)


def start_websocket():
    # Initial data setup
    rest_create_channel("default")

    start_server = websockets.serve(handle_connection, port=8085)

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start_websocket()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

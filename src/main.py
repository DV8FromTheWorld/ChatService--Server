# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import asyncio
import json
import logging
import websockets
import events

logging.basicConfig()

MESSAGE_LOG_STATE = {
    "message_ids": []
}

STATE = {"value": 0}

CONNECTED_USERS = dict()
CHANNELS = ["default"]


async def dispatch_to_users(dispatch_event):
    if CONNECTED_USERS:  # asyncio.wait doesn't accept an empty list
        await asyncio.wait([user.send(dispatch_event) for user in CONNECTED_USERS.values()])


async def register_connection(user_id, websocket):
    CONNECTED_USERS[user_id] = websocket
    await dispatch_to_users(events.user_connected_dispatch())


async def unregister_connection(user_id):
    if user_id is None:
        return

    del CONNECTED_USERS[user_id]
    await dispatch_to_users(events.user_disconnected_dispatch())


async def handle_connection(websocket, path):
    # register(websocket) sends user_event() to websocket
    # await register_connection(websocket)

    await websocket.send(events.identify_dispatch())

    user_id = None
    try:
        async for message in websocket:
            print("Event: " + message)
            event = json.loads(message)
            event_type = event["type"]
            if event_type == "IDENTIFY_RESPONSE":
                user_id = event["data"]["userId"]

                await register_connection(user_id, websocket)
                await websocket.send(events.ready_dispatch(len(CONNECTED_USERS), CHANNELS))
            elif event_type == "SEND_MESSAGE":
                message_content = event["data"]["content"]
                await dispatch_to_users(events.message_create_dispatch(message_content))
            elif event_type == "CHANNEL_CREATE":
                channel = event["data"]["channel"]
                CHANNELS.append(channel["name"])
                await dispatch_to_users(events.channel_create_dispatch(channel["name"]))
            else:
                logging.error("unsupported event: %s", event)
    except Exception as e:
        print(e.with_traceback())

    finally:
        await unregister_connection(user_id)


def start_websocket():
    start_server = websockets.serve(handle_connection, port=8085)

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start_websocket()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

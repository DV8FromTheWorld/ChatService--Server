import json
import uuid
import datetime


def identify_dispatch():
    return json.dumps({
        "type": "IDENTIFY",
    })


def ready_dispatch(num_of_users: int, channels: set):
    return json.dumps({
        "type": "READY",
        "data": {
            "connectedUserTotal": num_of_users,
            "currentMessages": [],  # TODO populate this
            "channels": channels
        }
    })


def message_create_dispatch(message_content):
    return json.dumps({
        "type": "MESSAGE_CREATE",
        "data": {
            "message": {
                "id": str(uuid.uuid4()),
                "content": message_content,
                "updatedAt": str(datetime.datetime.now())
            }
        }
    })


def message_update_dispatch(message_id, message_content):
    return json.dumps({
        "type": "MESSAGE_UPDATE",
        "data": {
            "message": {
                "id": message_id,
                "content": message_content,
                "updatedAt": str(datetime.datetime.now())
            }
        }
    })


def message_delete_dispatch(message_id):
    return json.dumps({
        "type": "MESSAGE_DELETE",
        "data": {
            "messageId": message_id
        }
    })


def channel_create_dispatch(channel_name):
    return json.dumps({
        "type": "CHANNEL_CREATE",
        "data": {
            "channel": {
                "id": str(uuid.uuid4()),
                "name": channel_name,
                "updatedAt": str(datetime.datetime.now())
            }
        }
    })


def user_connected_dispatch():
    return json.dumps({
        "type": "USER_CONNECTED",
        "data": {
            "user": {}  # TODO
        }
    })


def user_disconnected_dispatch():
    return json.dumps({
        "type": "USER_DISCONNECTED",
        "data": {
            "user": {}  # TODO
        }
    })

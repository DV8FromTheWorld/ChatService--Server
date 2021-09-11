import json
import uuid
import datetime


def identify_dispatch():
    return json.dumps({
        "type": "IDENTIFY",
    })


def ready_dispatch(users: dict, channels: dict):
    return json.dumps({
        "type": "READY",
        "data": {
            "users": users,
            "channels": channels
        }
    })


def message_create_dispatch(user, message_channel_id, message_content):
    return json.dumps({
        "type": "MESSAGE_CREATE",
        "data": {
            "message": {
                "id": str(uuid.uuid4()),
                "content": message_content,
                "authorId": user["id"],
                "channelId": message_channel_id,
                "createdAt": str(datetime.datetime.now()),
            }
        }
    })


def message_update_dispatch(user, message_id, message_channel_id, message_content):
    return json.dumps({
        "type": "MESSAGE_UPDATE",
        "data": {
            "message": {
                "id": message_id,
                "content": message_content,
                "authorId": user["id"],
                "channelId": message_channel_id,
                "updatedAt": str(datetime.datetime.now())
            }
        }
    })


def message_delete_dispatch(message_id, message_channel_id):
    return json.dumps({
        "type": "MESSAGE_DELETE",
        "data": {
            "messageId": message_id,
            "channelId": message_channel_id
        }
    })


def channel_create_dispatch(channel):
    return json.dumps({
        "type": "CHANNEL_CREATE",
        "data": {
            "channel": channel
        }
    })


def user_connected_dispatch(user):
    return json.dumps({
        "type": "USER_CONNECTED",
        "data": {
            "user": user
        }
    })


def user_disconnected_dispatch(user_id):
    return json.dumps({
        "type": "USER_DISCONNECTED",
        "data": {
            "userId": user_id
        }
    })

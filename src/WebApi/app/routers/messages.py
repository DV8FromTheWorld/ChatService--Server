from fastapi import APIRouter

router = APIRouter(
    prefix='/api/v1/channels',
    tags=["Messages"]
)

@router.post("/{channel_id}/messages")
async def create_message(channel_id: str):
    return {"msg": "Hi from messages controller"}


@router.get("/{channel_id}/messages")
async def get_message_history(channel_id: str, before: str = None, after: str = None, around: str = None):
    return {"msg": "Hi from messages controller"}


@router.get("/{channel_id}/messages/{message_id}")
async def get_message(channel_id: str, message_id: str):
    return {"msg": "Hi from messages controller"}


@router.put("/{channel_id}/messages/{message_id}")
async def update_message(channel_id: str, message_id: str):
    return {"msg": "Hi from messages controller"}


@router.delete("/{channel_id}/messages/{message_id}")
async def delete_message(channel_id: str, message_id: str):
    return {"msg": "Hi from messages controller"}
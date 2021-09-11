from fastapi import APIRouter, Body, status
from fastapi.responses import JSONResponse
from ..models import Channel

router = APIRouter(
    prefix='/api/v1/channels',
    tags=["channels"]
)


@router.get("/")
async def get_channels():
    return {"msg": "Hi from channels controller"}


@router.get("/{channelId}", response_model=Channel)
async def get_channel(channelId):
    model = Channel()
    model.channel_id = channelId
    return model


@router.get("/{channelId}/messages")
async def get_channel_messages(channelId, limit: int = 100, offset: int = 0):
    return {"channelId": channelId, "messages": ["msg1", "msg2"], "limit": limit, "offset": offset}


@router.post("/{channelId}/messages")
async def post_message(channelId):
    return JSONResponse(status_code=status.HTTP_200_OK)

from fastapi import APIRouter, Body, status
from fastapi.responses import JSONResponse
from ..models import Channel

router = APIRouter(
    prefix='/api/v1/channels',
    tags=["Channels"]
)

@router.get("/{channel_id}", response_model=Channel)
async def get_channel(channel_id: str):
    model = Channel()
    model.channel_id = channel_id
    return model

@router.put("/{channel_id}", response_model=Channel)
async def update_channel(channel_id: str):
    model = Channel()
    model.channel_id = channel_id
    return model

@router.delete("/{channel_id}")
async def delete_channel(channel_id: str):
    return {"msg": "Hi from channels controller"}


@router.post("/{channel_id}/typing")
async def send_typing(channel_id: str):
    return {"msg": "Hi from channels controller"}


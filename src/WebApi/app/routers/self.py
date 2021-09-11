from fastapi import APIRouter
from .users import get_user

router = APIRouter(
    prefix='/api/v1/users/@me',
    tags=["Self User"]
)


@router.get("/")
async def get_self():
    # TODO - get user's id from auth bearer token
    self_user_id = 'put id here!'
    return get_user(self_user_id)


@router.put("/")
async def update_self():
    return {"msg": "Hello from self user controller!"}


@router.get("/guilds")
async def get_guilds():
    return {"msg": "Hello from self user controller!"}


@router.delete("/guilds/{guild_id}")
async def leave_guild(guild_id: str):
    return {"msg": "Hello from self user controller!"}


@router.get("/channels")
async def get_private_channels():
    return {"msg": "Hello from self user controller!"}


@router.post("/channels/{user_id}")
async def create_private_channel(user_id: str):
    return {"msg": "Hello from self user controller!"}


@router.get("/notes/{user_id}")
async def get_user_notes(user_id: str):
    return {"msg": "Hello from self user controller!"}


@router.put("/notes/{user_id}")
async def update_user_notes(user_id: str):
    return {"msg": "Hello from self user controller!"}


@router.delete("/notes/{user_id}")
async def remove_user_notes(user_id: str):
    return {"msg": "Hello from self user controller!"}

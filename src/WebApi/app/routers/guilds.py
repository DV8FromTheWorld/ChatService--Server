from fastapi import APIRouter

router = APIRouter(
    prefix='/api/v1/guilds',
    tags=["Guilds"]
)


@router.post("/")
async def create_guild():
    return {"msg": "Hi from guilds controller"}


# Not sure we actually need this as we'll get all guilds on READY
@router.get("/")
async def get_guilds():
    return {"msg": "Hi from guilds controller"}


@router.get("/{guild_id}")
async def get_guild(guild_id: str):
    return {"guildId": guild_id}


@router.post("/{guild_id}")
async def update_guild(guild_id: str):
    return {"msg": "Hi from guilds controller"}


@router.delete("/{guild_id}")
async def delete_guild(guild_id: str):
    return {"msg": "Hi from guilds controller"}


@router.get("/{guild_id}/channels")
async def get_guild_channels(guild_id: str):
    return {"msg": "Hi from guild controller"}


@router.post("/{guild_id}/channels")
async def create_guild_channel(guild_id: str):
    return {"msg": "Hi from guild controller"}

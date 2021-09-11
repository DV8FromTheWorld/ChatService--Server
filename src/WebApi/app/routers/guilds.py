from fastapi import APIRouter

router = APIRouter(
    prefix='/api/v1/guilds',
    tags=["guilds"]
)


@router.get("/")
async def get_guilds():
    return {"msg": "Hi from guilds controller"}


@router.get("/{guildId}")
async def get_guilds(guildId):
    return {"guildId": guildId}

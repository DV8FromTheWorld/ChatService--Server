from fastapi import APIRouter

router = APIRouter(
    prefix='/api/v1/channels',
    tags=["channels"]
)


@router.get("/")
async def get_channels():
    return {"msg": "Hi from channels controller"}

from fastapi import APIRouter

router = APIRouter(
    prefix='/api/v1/users',
    tags=["Users"]
)


@router.get("/{user_id}")
async def get_user(user_id: str):
    return {"msg": "Hi from users controller"}

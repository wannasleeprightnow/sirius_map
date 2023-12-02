from fastapi import APIRouter, Body, Depends

from dependencies import user_service
from services.user import UserService
from schemas.user import UserLogin, UserRegister

router = APIRouter(prefix="/user", tags=["user"])


@router.post("/register")
async def register(
    user: UserRegister = Body(),
    user_service: UserService = Depends(user_service)
):
    return await user_service.register(user)


@router.post("/login")
async def login(
    user: UserLogin = Body(),
    user_service: UserService = Depends(user_service)
):
    return await user_service.login(user)

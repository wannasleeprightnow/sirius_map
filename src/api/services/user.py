from fastapi import HTTPException

from models.user import UserModel
from schemas.user import User, UserLogin, UserRegister
from repositories.user import UserRepository


class UserService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo: UserRepository = user_repo()

    async def register(
        self, user: UserRegister
    ) -> dict:
        if await self.user_repo.select_one_user(user.username):
            raise HTTPException(
                status_code=400,
                detail="User already exists."
            )
        print(dict(user))
        user.password = UserModel.hash_password(user.password)
        await self.user_repo.insert_one(dict(user))
        return {"status": "successfull"}

    async def login(
        self, user: UserLogin
    ) -> User:
        user_from_db = await self.user_repo.select_one_user(user.username)
        if not user_from_db:
            raise HTTPException(
                status_code=400,
                detail="User doesnt exist."
            )
        elif UserModel.check_password(
            user.password, user_from_db.password
        ):
            return user_from_db
        else:
            raise HTTPException(
                status_code=400,
                detail="Incorrect username or password."
            )

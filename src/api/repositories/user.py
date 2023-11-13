import os
import sys

sys.path.append(os.path.join(os.getcwd(), ".."))

from sqlalchemy import and_, delete, insert, select, update

from db.database import async_session_maker
from models.user import UserModel
from utils.repository import Repository


class UserRepository(Repository):
    model = UserModel

    async def select_check_user(
        self, username: str
    ) -> bool:
        async with async_session_maker() as session:
            query = (select(UserModel)
                     .where(UserModel.username == username))
            result = await session.execute(query)
            return bool(result.scalars().one())

    async def select_one_user(
        self, username: str
    ) -> UserModel:
        async with async_session_maker() as session:
            query = (select(UserModel)
                     .where(UserModel.username == username))
            result = await session.execute(query)
            try:
                return result.scalars().one()
            except Exception:
                return False

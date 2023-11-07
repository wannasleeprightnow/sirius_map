import os
import sys

sys.path.append(os.path.join(os.getcwd(), ".."))

from sqlalchemy import and_, delete, insert, select, update

from db.database import async_session_maker
from models.location import LocationModel
from models.user_location import UserLocationModel
from utils.repository import Repository


class LocationRepository(Repository):
    model = LocationModel

    async def find_all_favorite_locations(
        self, user_id: int
    ) -> list[LocationModel]:
        async with async_session_maker() as session:
            query = (
                select(LocationModel)
                .where(LocationModel.id == UserLocationModel.location_id)
                .where(UserLocationModel.user_id == user_id)
            )
        result = await session.execute(query)
        return result.scalars().all()

    async def insert_one_to_favorite(
        self, location_id: int, user_id: int
    ) -> dict:
        async with async_session_maker() as session:
            stmt = (insert(UserLocationModel)
                    .values(user_id=user_id, location_id=location_id)
                    .returning(UserLocationModel))
            res = await session.execute(stmt)
            await session.commit()
            return res.scalar_one()

    async def delete_one(self, location_id: int) -> dict:
        async with async_session_maker() as session:
            stmt = (delete(LocationModel)
                    .where(LocationModel.id == location_id))
            await session.execute(stmt)
            stmt = (delete(UserLocationModel)
                    .where(UserLocationModel.location_id == location_id)
                    )
            await session.execute(stmt)
            await session.commit()
            return {"status": "success"}

    async def delete_one_from_favorite(
        self, location_id: int, user_id: int
    ) -> dict:
        async with async_session_maker() as session:
            stmt = (delete(UserLocationModel)
                    .where(
                        and_(
                            UserLocationModel.user_id == user_id,
                            UserLocationModel.location_id == location_id
                            )
                        ))
        await session.execute(stmt)
        await session.commit()
        return {"status": "success"}

    async def update_one(self, location: dict) -> dict:
        async with async_session_maker() as session:
            stmt = (update(LocationModel)
                    .where(LocationModel.title == location["title"])
                    .values(**location)
                    .returning(LocationModel))
            res = await session.execute(stmt)
            await session.commit()
            return res.scalar_one()

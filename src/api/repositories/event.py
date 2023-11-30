import os
import sys

sys.path.append(os.path.join(os.getcwd(), ".."))

from sqlalchemy import and_, delete, insert, select

from db.db import async_session_maker
from models.event import EventModel
from models.user_event import UserEventModel
from utils.repository import Repository


class EventRepository(Repository):
    model = EventModel

    async def find_all_favorite_events(
        self, user_id: int
    ) -> list[EventModel]:
        async with async_session_maker() as session:
            query = (
                select(EventModel)
                .where(EventModel.id == UserEventModel.event_id)
                .where(UserEventModel.user_id == user_id)
            )
        result = await session.execute(query)
        return result.scalars().all()

    async def insert_one_to_favorite(
        self, event_id: int, user_id: int
    ) -> UserEventModel:
        async with async_session_maker() as session:
            stmt = (insert(UserEventModel)
                    .values(user_id=user_id, event_id=event_id)
                    .returning(UserEventModel))
            res = await session.execute(stmt)
            await session.commit()
            return res.scalar_one()

    async def delete_one(self, event_id: int) -> EventModel:
        async with async_session_maker() as session:
            stmt = (delete(EventModel)
                    .where(EventModel.id == event_id)
                    .returning(EventModel))
            res = await session.execute(stmt)
            stmt = (delete(UserEventModel)
                    .where(UserEventModel.event_id == event_id))
            await session.execute(stmt)
            await session.commit()
            return res.scalar_one()

    async def delete_one_from_favorite(
        self, event_id: int, user_id: int
    ) -> UserEventModel:
        async with async_session_maker() as session:
            stmt = (delete(UserEventModel)
                    .where(
                        and_(
                            UserEventModel.user_id == user_id,
                            UserEventModel.event_id == event_id
                            )
                        ).returning(UserEventModel))
        res = await session.execute(stmt)
        await session.commit()
        return res.scalar_one()

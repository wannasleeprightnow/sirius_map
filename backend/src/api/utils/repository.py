from abc import ABC, abstractmethod

from sqlalchemy import insert, select

from db.database import async_session_maker


class AbstractRepository(ABC):
    @abstractmethod
    async def insert_one():
        raise NotImplementedError

    @abstractmethod
    async def find_all():
        raise NotImplementedError


class Repository(AbstractRepository):
    model = None

    async def find_all(self):
        async with async_session_maker() as session:
            query = (select(self.model))
            result = await session.execute(query)
            return result.scalars().all()

    async def insert_one(self, data: dict):
        async with async_session_maker() as session:
            stmt = (insert(self.model)
                    .values(**data).returning(self.model.id))
            res = await session.execute(stmt)
            await session.commit()
            return res.scalar_one()

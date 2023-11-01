from database import async_engine
from models import (
    Base,
    Comment,
    Event,
    GraphEdge,
    Location,
    Point,
    User,
)


class ORM:

    @staticmethod
    async def create_tables():
        async with async_engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

PATH_TO_DB = "db.sqlite"


class Base(DeclarativeBase):
    pass


async_engine = create_async_engine(
    f"sqlite+aiosqlite:///{PATH_TO_DB}",
    echo=True,
)

async_session_maker = async_sessionmaker(
    async_engine,
)


async def create_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

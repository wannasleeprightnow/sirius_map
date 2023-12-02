from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from settings import PATH_TO_DB


class Base(DeclarativeBase):

    def __repr__(self):
        cols = '\n'.join([f"{att=}" for att in self.__table__.columns.keys()])
        return f"<{self.__class__.__name__} {cols}>"


async_engine = create_async_engine(
    f"sqlite+aiosqlite:///{PATH_TO_DB}",
    echo=True,
)

async_session_maker = async_sessionmaker(
    async_engine, expire_on_commit=False
)


async def create_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

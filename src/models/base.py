import time
import datetime
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from settings import (
    POSTGRES_USER,
    POSTGRES_PASSWORD,
    POSTGRES_HOST,
    POSTGRES_PORT,
    POSTGRES_DB
)


class Base(DeclarativeBase):

    def __repr__(self):
        cols = '\n'.join([f"{att=}" for att in self.__table__.columns.keys()])
        return f"<{self.__class__.__name__} {cols}>"


async_engine = create_async_engine(
    f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}",
    echo=True,
)

async_session_maker = async_sessionmaker(
    async_engine, expire_on_commit=False
)

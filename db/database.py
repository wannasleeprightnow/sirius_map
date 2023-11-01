import os
import sys

sys.path.append(os.path.join(os.getcwd(), ".."))


from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from azimuth.config import PATH_TO_DB


async_engine = create_async_engine(
    f"sqlite+aiosqlite:///{PATH_TO_DB}",
    echo=True,
)

async_session_factory = async_sessionmaker(
    async_engine,
    expire_on_commit=False,
)

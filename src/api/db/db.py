import asyncio
import datetime
import time

import bcrypt
from sqlalchemy import LargeBinary, String, ForeignKey, Table, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship, selectinload
from sqlalchemy import select
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from settings import PATH_TO_DB

async_engine = create_async_engine(
    f"sqlite+aiosqlite:///{PATH_TO_DB}",
    echo=True,
)

async_session_maker = async_sessionmaker(
    async_engine, expire_on_commit=False
)


class Base(DeclarativeBase):
    pass


# class UserLocationModel(Base):
#     __tablename__ = "user_location"

#     user_id: Mapped[int] = mapped_column(primary_key=True)
#     location_id: Mapped[int] = mapped_column(primary_key=True)

#     def __repr__(self):
#         return f"{self.user_id=} {self.location_id=}"


# class UserEventModel(Base):
#     __tablename__ = "user_event"

#     user_id: Mapped[int] = mapped_column(primary_key=True)
#     event_id: Mapped[int] = mapped_column(primary_key=True)

#     def __repr__(self):
#         return f"{self.user_id=} {self.event_id=}"


# class UserModel(Base):
#     __tablename__ = "user"

#     id: Mapped[int] = mapped_column(primary_key=True)
#     username: Mapped[str] = mapped_column(String(50), unique=True)
#     password: Mapped[str] = mapped_column(String(25))
#     name: Mapped[str] = mapped_column(String(25))
#     phone_number: Mapped[str] = mapped_column(unique=True)
#     user_type: Mapped[str] = mapped_column(String(), default="user")
#     user_image: Mapped[bytes | None] = mapped_column(LargeBinary)


# class PointModel(Base):
#     __tablename__ = "point"

#     id: Mapped[int] = mapped_column(primary_key=True)
#     x_coordinate: Mapped[int]
#     y_coordinate: Mapped[int]

#     def __repr__(self):
#         return f"{self.id=} {self.x_coordinate=} {self.y_coordinate=}"


# class GraphEdge(Base):
#     __tablename__ = "graph_edge"

#     id: Mapped[int] = mapped_column(primary_key=True)
#     first_point_id: Mapped[int] = mapped_column(
#         ForeignKey("point.id", on_delete="CASCADE")
#     )
#     second_point_id: Mapped[int] = mapped_column(
#         ForeignKey("point.id", on_delete="CASCADE")
#     )


# class LocationModel(Base):
#     __tablename__ = "location"

#     id: Mapped[int] = mapped_column(primary_key=True)
#     title: Mapped[str]
#     description: Mapped[str | None]
#     image: Mapped[bytes | None] = mapped_column(LargeBinary)
#     point_id: Mapped[int] = mapped_column(ForeignKey("point.id", ondelete="CASCADE"))


# class EventModel(Base):
#     __tablename__ = "event"

#     id: Mapped[int] = mapped_column(primary_key=True)
#     title: Mapped[str] = mapped_column(String(100), unique=True)
#     description: Mapped[str]
#     start_time: Mapped[datetime.datetime]
#     finish_time: Mapped[datetime.datetime]
#     location_id: Mapped[int] = mapped_column(
#         ForeignKey("location.id", ondelete="CASCADE")
#     )


# class CommentModel(Base):
#     __tablename__ = "comment"

#     id: Mapped[int] = mapped_column(primary_key=True)
#     comment_text: Mapped[str] = mapped_column(String(150))
#     created_at: Mapped[int] = mapped_column(
#         default=time.time
#     )
#     point_id: Mapped[int] = mapped_column(
#         ForeignKey("point.id", ondelete="CASCADE")
#     )
#     user_id: Mapped[int] = mapped_column(
#         ForeignKey("user.id", ondelete="CASCADE")
#     )

#     def __repr__(self):
#         return f"{self.id=} {self.comment_text=} {self.created_at=} \
#             {self.point_id=} {self.user_id=}"


async def create_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

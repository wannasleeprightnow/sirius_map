import datetime

from sqlalchemy import (
    ForeignKey,
    LargeBinary,
    String,
)
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50), unique=True)
    password: Mapped[str] = mapped_column(String(25))
    name: Mapped[str] = mapped_column(String(25))
    phone_number: Mapped[str] = mapped_column(unique=True)
    user_type: Mapped[str]
    user_image: Mapped[str] = mapped_column(LargeBinary)


class Location(Base):
    __tablename__ = "location"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    description: Mapped[str | None]
    image: Mapped[str] = mapped_column(LargeBinary)


class Point(Base):
    __tablename__ = "point"

    id: Mapped[int] = mapped_column(primary_key=True)
    x_coordinate: Mapped[int]
    y_coordinate: Mapped[int]
    location_id: Mapped[int | None] = mapped_column(
        ForeignKey("location.id", on_delete="CASCADE")
    )


class GraphEdge(Base):
    __tablename__ = "graph_edge"

    id: Mapped[int] = mapped_column(primary_key=True)
    weight: Mapped[int]
    first_point_id: Mapped[int] = mapped_column(
        ForeignKey("point.id", on_delete="CASCADE")
    )
    second_point_id: Mapped[int] = mapped_column(
        ForeignKey("point.id", on_delete="CASCADE")
    )


class Comment(Base):
    __tablename__ = "comment"

    id: Mapped[int] = mapped_column(primary_key=True)
    comment_text: Mapped[str] = mapped_column(String(150))
    created_at: Mapped[datetime.datetime] = mapped_column(
        default=datetime.datetime.utcnow
    )
    point_id: Mapped[int] = mapped_column(
        ForeignKey("point.id", on_delete="CASCADE"))
    user_id: Mapped[int] = mapped_column(
        ForeignKey("user.id", on_delete="CASCADE"))


class Event(Base):
    __tablename__ = "event"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100), unique=True)
    description: Mapped[str]
    start_time: Mapped[datetime.datetime]
    finish_time: Mapped[datetime.datetime]
    location_id: Mapped[int] = mapped_column(
        ForeignKey("location.id", on_delete="CASCADE")
    )

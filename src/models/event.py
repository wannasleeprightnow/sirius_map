import datetime

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from models.base import Base


class EventModel(Base):
    __tablename__ = "event"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100), unique=True)
    description: Mapped[str]
    start_time: Mapped[datetime.datetime]
    finish_time: Mapped[datetime.datetime]
    location_id: Mapped[int] = mapped_column(
        ForeignKey("location.id", ondelete="CASCADE")
    )

from sqlalchemy.orm import Mapped, mapped_column

from db.database import Base


class UserEventModel(Base):
    __tablename__ = "user_event"

    user_id: Mapped[int] = mapped_column(primary_key=True)
    event_id: Mapped[int] = mapped_column(primary_key=True)

    def __repr__(self):
        return f"{self.user_id=} {self.event_id=}"

from sqlalchemy.orm import mapped_column, Mapped

from db.db import Base


class UserEventModel(Base):
    __tablename__ = "user_event"
    __table_args__ = {'extend_existing': True}

    user_id: Mapped[int] = mapped_column(primary_key=True)
    event_id: Mapped[int] = mapped_column(primary_key=True)

    def __repr__(self):
        return f"{self.user_id=} {self.event_id=}"

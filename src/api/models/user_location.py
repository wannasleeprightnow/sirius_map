from sqlalchemy.orm import mapped_column, Mapped

from db.db import Base


class UserLocationModel(Base):
    __tablename__ = "user_location"
    __table_args__ = {'extend_existing': True}

    user_id: Mapped[int] = mapped_column(primary_key=True)
    location_id: Mapped[int] = mapped_column(primary_key=True)

    def __repr__(self):
        return f"{self.user_id=} {self.location_id=}"

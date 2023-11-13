from sqlalchemy.orm import Mapped, mapped_column

from db.database import Base


class UserLocationModel(Base):
    __tablename__ = "user_location"

    user_id: Mapped[int] = mapped_column(primary_key=True)
    location_id: Mapped[int] = mapped_column(primary_key=True)

    def __repr__(self):
        return f"{self.user_id=} {self.location_id=}"

from sqlalchemy.orm import mapped_column, Mapped

from models.base import Base


class UserLocationModel(Base):
    __tablename__ = "user_location"
    __table_args__ = {'extend_existing': True}

    user_id: Mapped[int] = mapped_column(primary_key=True)
    location_id: Mapped[int] = mapped_column(primary_key=True)

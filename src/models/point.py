from sqlalchemy.orm import Mapped, mapped_column

from models.base import Base


class PointModel(Base):
    __tablename__ = "point"

    id: Mapped[int] = mapped_column(primary_key=True)
    x_coordinate: Mapped[float]
    y_coordinate: Mapped[float]

from sqlalchemy.orm import Mapped, mapped_column

from db.database import Base


class PointModel(Base):
    __tablename__ = "point"

    id: Mapped[int] = mapped_column(primary_key=True)
    x_coordinate: Mapped[int]
    y_coordinate: Mapped[int]

    def __repr__(self):
        return f"{self.id=} {self.x_coordinate=} {self.y_coordinate=}"

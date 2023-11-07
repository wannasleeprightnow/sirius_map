from sqlalchemy import ForeignKey, LargeBinary
from sqlalchemy.orm import Mapped, mapped_column

from db.database import Base


class LocationModel(Base):
    __tablename__ = "location"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    description: Mapped[str | None]
    image: Mapped[bytes | None] = mapped_column(LargeBinary)
    point_id: Mapped[int] = mapped_column(
        ForeignKey("point.id", ondelete="CASCADE")
    )

    def __repr__(self):
        return f"{self.id=} {self.title=} {self.description=} \
            self.image {self.point_id=}"

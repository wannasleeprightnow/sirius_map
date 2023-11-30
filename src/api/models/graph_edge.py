from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped

from db.db import Base


class GraphEdge(Base):
    __tablename__ = "graph_edge"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_point_id: Mapped[int] = mapped_column(
        ForeignKey("point.id", on_delete="CASCADE")
    )
    second_point_id: Mapped[int] = mapped_column(
        ForeignKey("point.id", on_delete="CASCADE")
    )

    def __repr__(self):
        return f"{self.id=} {self.first_point_id=}\
            {self.second_point_id=}"

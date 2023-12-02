from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped

from models.base import Base


class GraphEdge(Base):
    __tablename__ = "graph_edge"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_point_id: Mapped[int] = mapped_column(
        ForeignKey("point.id", on_delete="CASCADE")
    )
    second_point_id: Mapped[int] = mapped_column(
        ForeignKey("point.id", on_delete="CASCADE")
    )

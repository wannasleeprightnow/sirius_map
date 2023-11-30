import time

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from db.db import Base


class CommentModel(Base):
    __tablename__ = "comment"

    id: Mapped[int] = mapped_column(primary_key=True)
    comment_text: Mapped[str] = mapped_column(String(150))
    created_at: Mapped[int] = mapped_column(
        default=time.time
    )
    point_id: Mapped[int] = mapped_column(
        ForeignKey("point.id", ondelete="CASCADE")
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey("user.id", ondelete="CASCADE")
    )

    def __repr__(self):
        return f"{self.id=} {self.comment_text=} {self.created_at=} \
            {self.point_id=} {self.user_id=}"

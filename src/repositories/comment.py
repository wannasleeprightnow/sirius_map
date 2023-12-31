from sqlalchemy import delete

from models.base import async_session_maker
from models.comment import CommentModel
from utils.repository import Repository


class CommentRepository(Repository):
    model = CommentModel

    async def delete_one(self, comment_id: int) -> CommentModel:
        async with async_session_maker() as session:
            stmt = (delete(CommentModel)
                    .where(CommentModel.id == comment_id)
                    .returning(self.model))
            res = await session.execute(stmt)
            await session.commit()
            return res.scalar_one()

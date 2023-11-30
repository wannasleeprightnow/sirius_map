import time

from fastapi import HTTPException

from models.comment import CommentModel
from schemas.comment import CommentId, CommentAdd
from repositories.comment import CommentRepository


class CommentService:
    def __init__(self, comment_repo: CommentRepository):
        self.comment_repo: CommentRepository = comment_repo()

    async def get_comments(self) -> list[CommentModel]:
        comments = await self.comment_repo.find_all()
        for comment in comments:
            if time.time() - comment.created_at >= 3600:
                await self.comment_repo.delete_one(comment.id)
        comments = await self.comment_repo.find_all()
        return comments

    async def post_comment(
        self, comment: CommentAdd
    ):
        res = await self.comment_repo.insert_one(comment.model_dump())
        return res

    async def delete_comment(
        self, comment: CommentId
    ) -> dict:
        res = await self.comment_repo.delete_one(**comment.model_dump())
        return res

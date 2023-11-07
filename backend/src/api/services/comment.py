from models.comment import CommentModel
from schemas.comment import Comment, CommentId
from repositories.comment import CommentRepository


class CommentService:
    def __init__(self, comment_repo: CommentRepository):
        self.comment_repo: CommentRepository = comment_repo()

    async def get_comments(self) -> list[CommentModel]:
        comments = await self.comment_repo.find_all()
        return comments

    async def post_comment(
        self, comment: Comment
    ) -> CommentModel:
        comment = await self.comment_repo.insert_one(dict(comment))
        return comment

    async def delete_comment(
        self, comment: CommentId
    ) -> dict:
        return await self.comment_repo.delete_one(**dict(comment))

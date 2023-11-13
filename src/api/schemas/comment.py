from pydantic import BaseModel


class Comment(BaseModel):
    comment_text: str
    point_id: int
    user_id: int


class CommentId(BaseModel):
    comment_id: int

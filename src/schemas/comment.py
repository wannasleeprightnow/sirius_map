from pydantic import BaseModel


class Comment(BaseModel):
    id: int
    comment_text: str
    created_at: float
    point_id: int
    user_id: int


class CommentAdd(BaseModel):
    comment_text: str
    point_id: int
    user_id: int


class CommentId(BaseModel):
    comment_id: int

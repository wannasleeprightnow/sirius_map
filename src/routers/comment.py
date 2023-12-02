from fastapi import APIRouter, Body, Depends

from dependencies import comment_service
from services.comment import CommentService
from schemas.comment import Comment, CommentAdd, CommentId

router = APIRouter(prefix="/comment", tags=["comment"])


@router.get("", response_model=list[Comment])
async def get_comments(
    comment_service: CommentService = Depends(comment_service)
):
    comments = await comment_service.get_comments()
    return comments


@router.post("", response_model=Comment)
async def post_comment(
    comment: CommentAdd = Body(),
    comment_service: CommentService = Depends(comment_service)
):
    comment = await comment_service.post_comment(comment)
    return comment


@router.delete("", response_model=Comment)
async def delete_comment(
    comment: CommentId = Body(),
    comment_service: CommentService = Depends(comment_service)
):
    return await comment_service.delete_comment(comment)

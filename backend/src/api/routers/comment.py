from fastapi import APIRouter, Body, Depends

from config import API_VERSION
from dependencies import comment_service
from services.comment import CommentService
from schemas.comment import Comment, CommentId

router = APIRouter(prefix=API_VERSION + "comment", tags=["comment"])


@router.get("")
async def get_comments(
    comment_service: CommentService = Depends(comment_service)
):
    comments = await comment_service.get_comments()
    return comments


@router.post("")
async def post_comment(
    comment: Comment = Body(),
    comment_service: CommentService = Depends(comment_service)
):
    comment = await comment_service.post_comment(comment)
    return comment


@router.delete("")
async def delete_comment(
    comment: CommentId = Body(),
    comment_service: CommentService = Depends(comment_service)
):
    return await comment_service.delete_comment(comment)

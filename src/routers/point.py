from fastapi import APIRouter, Body, Depends

from dependencies import point_service
from services.point import PointService
from schemas.point import Point, PointAdd, PointId

router = APIRouter(prefix="/point", tags=["point"])


@router.get("", response_model=list[Point])
async def get_points(
    point_service: PointService = Depends(point_service)
):
    points = await point_service.get_points()
    return points


@router.post("", response_model=Point)
async def post_point(
    point: PointAdd = Body(),
    point_service: PointService = Depends(point_service)
):
    point = await point_service.post_point(point)
    return point


@router.delete("", response_model=Point)
async def delete_point(
    point: PointId = Body(),
    point_service: PointService = Depends(point_service)
):
    return await point_service.delete_point(point)

from models.point import PointModel
from schemas.point import PointId, PointAdd
from repositories.point import PointRepository


class PointService:
    def __init__(self, point_repo: PointRepository):
        self.point_repo: PointRepository = point_repo()

    async def get_points(self) -> list[PointModel]:
        points = await self.point_repo.find_all()
        return points

    async def post_point(
        self, point: PointAdd
    ):
        res = await self.point_repo.insert_one(point.model_dump())
        return res

    async def delete_point(
        self, point: PointId
    ) -> dict:
        res = await self.point_repo.delete_one(**point.model_dump())
        return res

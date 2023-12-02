from sqlalchemy import delete

from models.base import async_session_maker
from models.point import PointModel
from utils.repository import Repository


class PointRepository(Repository):
    model = PointModel

    async def delete_one(self, point_id: int) -> PointModel:
        async with async_session_maker() as session:
            stmt = (delete(PointModel)
                    .where(PointModel.id == point_id)
                    .returning(PointModel))
            res = await session.execute(stmt)
            await session.commit()
            return res.scalar_one()

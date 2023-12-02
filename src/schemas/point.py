from pydantic import BaseModel


class Point(BaseModel):
    id: int
    x_coordinate: float
    y_coordinate: float


class PointAdd(BaseModel):
    x_coordinate: float
    y_coordinate: float


class PointId(BaseModel):
    point_id: int

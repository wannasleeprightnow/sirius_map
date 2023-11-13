from pydantic import BaseModel


class Location(BaseModel):
    title: str
    description: str | None
    image: bytes | None
    point_id: int


class UserLocationId:
    user_id: int


class LocationId(BaseModel):
    location_id: int


class UserLocation(BaseModel):
    location_id: int
    user_id: int

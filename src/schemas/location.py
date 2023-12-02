from pydantic import BaseModel


class Location(BaseModel):
    id: int
    title: str
    description: str | None
    image: bytes | None
    point_id: int


class LocationAdd(BaseModel):
    title: str
    description: str | None
    image: bytes | None
    point_id: int


class UserLocationId(BaseModel):
    user_id: int


class LocationId(BaseModel):
    location_id: int


class UserLocation(BaseModel):
    location_id: int
    user_id: int

import datetime

from pydantic import BaseModel


class Event(BaseModel):
    id: int
    title: str
    description: str
    start_time: datetime.datetime
    finish_time: datetime.datetime
    location_id: int


class EventAdd(BaseModel):
    title: str
    description: str
    start_time: datetime.datetime
    finish_time: datetime.datetime
    location_id: int


class UserEventId(BaseModel):
    user_id: int


class EventId(BaseModel):
    event_id: int


class UserEvent(BaseModel):
    event_id: int
    user_id: int

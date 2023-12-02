from fastapi import APIRouter, Body, Depends

from dependencies import event_service
from services.event import EventService
from schemas.event import Event, EventAdd, EventId, UserEvent

router = APIRouter(prefix="/event", tags=["event"])


@router.get("", response_model=list[Event])
async def get_events(
    event_service: EventService = Depends(event_service)
):
    events = await event_service.get_events()
    return events


@router.get("/favorite/{user_id}/", response_model=list[Event])
async def get_favorite_user_events(
    user_id: int,
    event_service: EventService = Depends(event_service)
):
    events = await event_service.get_favorite_user_events(user_id)
    return events


@router.post("", response_model=Event)
async def post_event(
    event: EventAdd = Body(),
    event_service: EventService = Depends(event_service),
):
    event = await event_service.post_event(event)
    return event


@router.post("/favorite/", response_model=UserEvent)
async def post_event_to_user_favorite(
    event: UserEvent = Body(),
    event_service: EventService = Depends(event_service),
):
    event = await event_service.post_event_to_user_favorite(event)
    return event


@router.delete("/favorite/", response_model=UserEvent)
async def delete_event_from_favorite(
    event: UserEvent = Body(),
    event_service: EventService = Depends(event_service),
):
    return await event_service.delete_event_from_favorite(event)


@router.delete("", response_model=Event)
async def delete_event(
    event: EventId = Body(),
    event_service: EventService = Depends(event_service),
):
    return await event_service.delete_event(event)

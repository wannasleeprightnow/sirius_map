from fastapi import APIRouter, Body, Depends

from dependencies import event_service
from services.event import EventService
from schemas.event import Event, EventId, UserEvent

router = APIRouter(prefix="/event", tags=["event"])


@router.get("")
async def get_events(
    event_service: EventService = Depends(event_service)
):
    events = await event_service.get_events()
    return events


@router.get("/favorite/{user_id}/")
async def get_favorite_user_events(
    user_id: int,
    event_service: EventService = Depends(event_service)
):
    events = await event_service.get_favorite_user_events(user_id)
    return events


@router.post("")
async def post_event(
    event: Event = Body(),
    event_service: EventService = Depends(event_service),
):
    event = await event_service.post_event(event)
    return event


@router.post("/favorite/")
async def post_event_to_user_favorite(
    event: UserEvent = Body(),
    event_service: EventService = Depends(event_service),
):
    event = await event_service.post_event_to_user_favorite(event)
    return event


@router.delete("/favorite/")
async def delete_event_from_favorite(
    event: UserEvent = Body(),
    event_service: EventService = Depends(event_service),
):
    return await event_service.delete_event_from_favorite(event)


@router.delete("")
async def delete_event(
    event: EventId = Body(),
    event_service: EventService = Depends(event_service),
):
    return await event_service.delete_event(event)

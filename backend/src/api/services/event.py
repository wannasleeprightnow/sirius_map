from models.event import EventModel
from schemas.event import Event, UserEvent, EventId, UserEventId
from repositories.event import EventRepository


class EventService:
    def __init__(self, event_repo: EventRepository):
        self.event_repo: EventRepository = event_repo()

    async def get_events(self) -> list[EventModel]:
        events = await self.event_repo.find_all()
        return events

    async def get_favorite_user_events(
        self, user_id: int
    ) -> list[EventModel]:
        events = await self.event_repo.find_all_favorite_events(user_id)
        return events

    async def post_event(
        self, event: Event
    ) -> EventModel:
        event = await self.event_repo.insert_one(dict(event))
        return event

    async def post_event_to_user_favorite(
        self, event: UserEvent
    ) -> EventModel:
        event = await self.event_repo.insert_one_to_favorite(**dict(event))
        return event

    async def delete_event_from_favorite(
        self, event: UserEvent
    ) -> dict:
        return await self.event_repo.delete_one_from_favorite(**(dict(event)))

    async def delete_event(
        self, event: EventId
    ) -> dict:
        return await self.event_repo.delete_one(**(dict(event)))

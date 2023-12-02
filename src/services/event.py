from models.user_event import UserEventModel
from models.event import EventModel
from schemas.event import EventAdd, UserEvent, EventId
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
        self, event: EventAdd
    ) -> EventModel:
        return await self.event_repo.insert_one(event.model_dump())

    async def post_event_to_user_favorite(
        self, event: UserEvent
    ) -> UserEventModel:
        return await self.event_repo.insert_one_to_favorite(**event.model_dump())

    async def delete_event_from_favorite(
        self, event: UserEvent
    ) -> UserEventModel:
        return await self.event_repo.delete_one_from_favorite(**event.model_dump())

    async def delete_event(
        self, event: EventId
    ) -> EventModel:
        return await self.event_repo.delete_one(**event.model_dump())

from repositories.comment import CommentRepository
from repositories.event import EventRepository
from repositories.location import LocationRepository
from services.comment import CommentService
from services.event import EventService
from services.location import LocationService


def comment_service():
    return CommentService(CommentRepository)


def event_service():
    return EventService(EventRepository)


def location_service():
    return LocationService(LocationRepository)

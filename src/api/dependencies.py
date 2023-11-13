from repositories.comment import CommentRepository
from repositories.event import EventRepository
from repositories.location import LocationRepository
from repositories.user import UserRepository
from services.comment import CommentService
from services.event import EventService
from services.location import LocationService
from services.user import UserService


def comment_service():
    return CommentService(CommentRepository)


def event_service():
    return EventService(EventRepository)


def location_service():
    return LocationService(LocationRepository)


def user_service():
    return UserService(UserRepository)

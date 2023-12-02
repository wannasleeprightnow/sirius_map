from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers.comment import router as comment_router
from routers.event import router as event_router
from routers.location import router as location_router
from routers.point import router as point_router
from routers.user import router as user_router

app = FastAPI(title="sirius_map")
main_router = APIRouter()

origins = ["127.0.0.1:8000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS"],
    allow_headers=[
        "Content-Type",
        "Set-Cookie",
        "Access-Control-Allow-Headers",
        "Access-Control-Allow-Origin",
        "Authorization",
    ],
)


main_router.include_router(comment_router)
main_router.include_router(event_router)
main_router.include_router(location_router)
main_router.include_router(point_router)
main_router.include_router(user_router)
app.include_router(main_router)

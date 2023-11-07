import asyncio

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from routers.comment import router as comment_router
from routers.event import router as event_router
from routers.location import router as location_router

from db.database import create_tables

app = FastAPI(title="sirius_map")

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


def main():
    asyncio.run(create_tables())
    app.include_router(comment_router)
    app.include_router(event_router)
    app.include_router(location_router)
    uvicorn.run(app=app, host="127.0.0.1", port=8000)


if __name__ == "__main__":
    main()

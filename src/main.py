"""Main module for the FastAPI application."""

from contextlib import asynccontextmanager

from fastapi import FastAPI

from .dependencies import get_member_service, get_video_service
from .routers import health, member, video

member_service = get_member_service()
video_service = get_video_service()


@asynccontextmanager
async def lifespan(api: FastAPI):  # pylint: disable=unused-argument
    """Create the base paths for the video and member folders on startup."""
    video_service.create_base_path()
    member_service.create_base_path()
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(health.router)
app.include_router(video.router)
app.include_router(member.router)

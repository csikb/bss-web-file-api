"""Main module for the FastAPI application."""

from contextlib import asynccontextmanager

from fastapi import FastAPI

from .dependencies import get_settings
from .routers import health, member, video
from .services.member import MemberService
from .services.video import VideoService


@asynccontextmanager
async def lifespan(api: FastAPI):  # pylint: disable=unused-argument
    """Create the base paths for the video and member folders on startup."""
    settings = get_settings()
    member_service = MemberService(settings.server_base_path)
    video_service = VideoService(settings.server_base_path)
    video_service.create_base_path()
    member_service.create_base_path()
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(health.router)
app.include_router(video.router)
app.include_router(member.router)

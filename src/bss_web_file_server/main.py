"""Main module for the FastAPI application."""

from typing import Annotated

from fastapi import FastAPI

from .routers import health, member, video
from .services.member import MemberService
from .services.video import VideoService

app = FastAPI()

app.include_router(health.router)
app.include_router(video.router)
app.include_router(member.router)


@app.on_event("startup")
async def startup_event(
    member_service=MemberService(),
    video_service=VideoService(),
):
    """Create the base paths for the video and member folders on startup."""
    video_service.create_base_path()
    member_service.create_base_path()

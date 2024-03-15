"""Main module for the FastAPI application."""

from fastapi import FastAPI

from .routers import health, member, video
from .services.member import create_member_base_path
from .services.video import create_video_base_path

app = FastAPI()

app.include_router(health.router)
app.include_router(video.router)
app.include_router(member.router)


@app.on_event("startup")
async def startup_event():
    """Create the base paths for the video and member folders on startup."""
    create_video_base_path()
    create_member_base_path()

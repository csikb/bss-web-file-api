"""Main module for the FastAPI application."""

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from . import settings
from .routers import member, video
from .services.member import create_member_base_path
from .services.video import create_video_base_path

app = FastAPI()

app.include_router(video.router)
app.include_router(member.router)
app.mount(
    "/assets",
    StaticFiles(directory=settings.settings.server_base_path, check_dir=True),
    name="assets",
)


@app.on_event("startup")
async def startup_event():
    """Create the base paths for the video and member folders on startup."""
    create_video_base_path()
    create_member_base_path()

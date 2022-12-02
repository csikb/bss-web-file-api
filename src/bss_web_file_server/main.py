from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from . import config
from .routers import member, video

app = FastAPI()

app.include_router(video.router)
app.include_router(member.router)
app.mount(
    "/assets",
    StaticFiles(directory=config.settings.server_base_path, check_dir=True),
    name="assets",
)

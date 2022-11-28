from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from .routers import member, video

app = FastAPI()

app.include_router(video.router)
app.include_router(member.router)
app.mount("/assets", StaticFiles(directory="./assets", check_dir=True), name="assets")

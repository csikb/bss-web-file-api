from functools import lru_cache
from typing import Annotated

from fastapi import Depends

from .services.member import MemberService
from .services.video import VideoService
from .settings import Settings


@lru_cache
def get_settings():
    return Settings()


def get_member_service(settings: Annotated[Settings, Depends(get_settings)]):
    """Get the member service."""
    return MemberService(settings.server_base_path)


def get_video_service(settings: Annotated[Settings, Depends(get_settings)]):
    """Get the video service."""
    return VideoService(settings.server_base_path)

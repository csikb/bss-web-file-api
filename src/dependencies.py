from functools import lru_cache

from .services.member import MemberService
from .services.video import VideoService
from .settings import Settings


@lru_cache
def get_settings() -> Settings:
    return Settings()


def get_member_service(settings=get_settings()) -> MemberService:
    """Get the member service."""
    return MemberService(settings.server_base_path)


def get_video_service(settings=get_settings()) -> VideoService:
    """Get the video service."""
    return VideoService(settings.server_base_path)

from functools import lru_cache

from .services.member import MemberService
from .services.video import VideoService
from .settings import Settings


@lru_cache
def get_settings() -> Settings:
    print("Loading settings")
    return Settings()


@lru_cache
def get_member_service() -> MemberService:
    """Get the member service."""
    print("Loading member service")
    return MemberService(get_settings().server_base_path)


@lru_cache
def get_video_service() -> VideoService:
    """Get the video service."""
    print("Loading video service")
    return VideoService(get_settings().server_base_path)

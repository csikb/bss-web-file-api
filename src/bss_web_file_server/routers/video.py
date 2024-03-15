import re
from uuid import UUID

from fastapi import APIRouter, Response, UploadFile, status

from ..services.video import (
    Video,
    create_folder_structure,
    create_thumbnails,
    update_symlinks,
    to_id_path,
)

router = APIRouter(tags=["Video"], prefix="/api/v1/video")


@router.post("", response_model=Video)
def create_video_folder(video: Video):
    create_folder_structure(video, with_symlinks=True)
    return video


@router.put("", response_model=Video)
def update_video_folder(video: Video):
    if not to_id_path(video.id).exists():
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    update_symlinks(video)
    return video


@router.post("/{video_id}/poster", response_model=UUID)
async def upload_video_poster(video_id: UUID, file: UploadFile):
    if not re.match("image/.+", file.content_type):
        return Response(
            content="Mime is not an image format",
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
    content = await file.read()
    create_thumbnails(content, video_id)
    return video_id

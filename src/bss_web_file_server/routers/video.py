from uuid import UUID

from fastapi import APIRouter, UploadFile, status, Response

from bss_web_file_server.services.video import (
    Video,
    create_folder_structure,
    create_thumbnails,
    video_path,
    update_symlinks,
)

router = APIRouter(tags=["Video"])


@router.post("/api/v1/video", response_model=Video)
def create_video_folder(video: Video):
    long_path = video_path(video.id)
    if long_path.exists():
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    create_folder_structure(video, with_symlinks=True)
    return video


@router.put("/api/v1/video", response_model=Video)
def update_video_folder(video: Video):
    if not video_path(video.id).exists():
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    update_symlinks(video)
    return video


@router.post("/api/v1/video/{video_id}/poster", response_model=UUID)
async def upload_video_poster(video_id: UUID, file: UploadFile):
    content = await file.read()
    create_thumbnails(content, video_id)
    return video_id

from uuid import UUID
from fastapi import APIRouter, UploadFile
from starlette import status
from starlette.responses import Response
from app.services.video import Video, long_video_path, update_symlinks, create_thumbnails, create_folder_structure

router = APIRouter(tags=["Video"])


@router.post("/api/v1/video", response_model=Video)
def create_video_folder(video: Video):
    long_path = long_video_path(video.id)
    if long_path.exists():
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    create_folder_structure(video, with_symlinks=True)
    return video


@router.put("/api/v1/video", response_model=Video)
def update_video_folder(video: Video):
    if not long_video_path(video.id).exists():
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    update_symlinks(video)
    return video


@router.post("/api/v1/video/{video_id}/poster", response_model=UUID)
async def upload_video_poster(video_id: UUID, file: UploadFile):
    content = await file.read()
    create_thumbnails(content, video_id)
    return video_id
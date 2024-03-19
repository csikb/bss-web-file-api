"""Video endpoints"""

import re
from uuid import UUID

from fastapi import APIRouter, Response, UploadFile, status

from ..models.video import Video
from ..services.video import VideoService

router = APIRouter(tags=["Video"], prefix="/api/v1/video")
service: VideoService = VideoService()


@router.post("", response_model=Video)
def create_video_folder(video: Video):
    """
    Create a folder structure for a video and return the video object.
    :param video: Video object
    :return: 200 and the original video object
    """
    service.create_folder_structure(video)
    return video


@router.put("", response_model=Video)
def update_video_folder(video: Video):
    """
    Update the folder structure for a video and return the video object.
    If the video does not exist, return a 404.
    :param video: Video object
    :return: 200 and the original video object
    """
    if not service.to_id_path(video.id).exists():
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    service.update_symlinks(video)
    return video


@router.post("/{video_id}/thumbnail", response_model=UUID)
async def upload_video_poster(video_id: UUID, file: UploadFile):
    """
    Upload a picture for a video thumbnail to convert
    and store the thumbnail in different formats
    If the video does not exist, return a 404.
    If the file is not an image, return a 500.
    :param video_id: the id of the video
    :param file: the image file
    :return: 200 and the original video_id
    """
    # pylint: disable=duplicate-code
    if not service.to_id_path(video_id).exists():
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    if file.content_type is not None and not re.match("image/.+", file.content_type):
        return Response(
            content="Mime is not an image format",
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
    file_content = await file.read()
    # pylint: enable=duplicate-code
    service.create_thumbnails(file_content, video_id)
    return video_id

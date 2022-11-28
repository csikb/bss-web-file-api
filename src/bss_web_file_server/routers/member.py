import re
from uuid import UUID

from fastapi import APIRouter, Response, UploadFile, status

from src.bss_web_file_server.models.member import Member
from src.bss_web_file_server.services.member import (
    create_folder_structure,
    create_thumbnails,
    member_path,
    update_symlinks,
)

router = APIRouter(tags=["Member"])


@router.post("/api/v1/member", response_model=Member)
def create_member_folder(member: Member):
    long_path = member_path(member.id)
    if long_path.exists():
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    create_folder_structure(member, with_symlinks=True)
    return member


@router.put("/api/v1/member", response_model=Member)
def update_member_folder(member: Member):
    if not member_path(member.id).exists():
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    update_symlinks(member)
    return member


@router.post("/api/v1/member/{member_id}/image", response_model=UUID)
async def upload_member_picture(member_id: UUID, file: UploadFile):
    if not re.match("image/.+", file.content_type):
        return Response(
            "Mime is not an image format", status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    content = await file.read()
    create_thumbnails(content, member_id)

    return member_id

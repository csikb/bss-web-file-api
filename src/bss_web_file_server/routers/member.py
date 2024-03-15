import re
from uuid import UUID
from fastapi import APIRouter, Response, UploadFile, status
from ..models.member import Member
from ..services.member import (
    create_folder_structure,
    create_thumbnails,
    update_symlink,
    to_id_path,
)

router = APIRouter(tags=["Member"])


@router.post("/api/v1/member", response_model=Member)
def create_member_folder(member: Member):
    create_folder_structure(member, with_symlink=True)
    return member


@router.put("/api/v1/member", response_model=Member)
def update_member_folder(member: Member):
    if not to_id_path(member.id).exists():
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    update_symlink(member)
    return member


@router.post("/api/v1/member/{member_id}/image", response_model=UUID)
async def upload_member_picture(member_id: UUID, file: UploadFile):
    if not re.match("image/.+", file.content_type):
        return Response(
            content="Mime is not an image format",
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
    content = await file.read()
    create_thumbnails(content, member_id)

    return member_id

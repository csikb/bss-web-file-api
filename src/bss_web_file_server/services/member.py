from collections import namedtuple
from io import BytesIO
from pathlib import Path
from uuid import UUID

import pillow_avif  # type: ignore
from PIL import Image

from ..settings import settings
from ..models.member import Member

ImgFormat = namedtuple("ImgFormat", ["width", "height", "name"])
id_paths_base = Path(settings.server_base_path, "m")
url_paths_base = Path(settings.server_base_path, "member")
thumbnail_sizes = [
    ImgFormat(1920, 1080, "xl"),
    ImgFormat(1280, 720, "l"),
    ImgFormat(854, 480, "m"),
]
img_formats = ["avif", "webp", "jpeg"]


def create_folder_structure(member: Member, with_symlink=True):
    id_path = to_id_path(member.id)
    id_path.mkdir(parents=True, exist_ok=True)
    # create a folder for the thumbnails
    Path(id_path, "profile").mkdir(exist_ok=True)
    if with_symlink:
        update_symlink(member)


def create_thumbnails(content: bytes, member_id: UUID):
    # create a thumbnail folder in the id folder
    thumbnail_path = Path(to_id_path(member_id), "profile")
    with Image.open(BytesIO(content)) as image:
        for thumbnail in thumbnail_sizes:
            i = image.copy()
            i.thumbnail(size=(thumbnail.width, thumbnail.height))
            for img_format in img_formats:
                i.save(Path(thumbnail_path, thumbnail.name + "." + img_format))


def update_symlink(member: Member):
    # this method will first remove all references to the id folder
    id_path = to_id_path(member.id)
    # find any symlink folders that would point to the id_path
    for url_path in url_paths_base.glob("*/"):
        if url_path.is_symlink() and url_path.readlink().samefile(id_path):
            # and remove them
            url_path.unlink(missing_ok=True)
    # create a new symlink to the id path
    to_url_path(member.url).symlink_to(
        # use the absolute path to the id folder
        target=id_path.resolve(),
        target_is_directory=True
    )


def create_member_base_path():
    if not id_paths_base.exists():
        id_paths_base.mkdir(parents=True, exist_ok=True)
    if not url_paths_base.exists():
        url_paths_base.mkdir(parents=True, exist_ok=True)


def to_id_path(member_id: UUID):
    return Path(id_paths_base, str(member_id))


def to_url_path(member_url: str):
    return Path(url_paths_base, member_url)

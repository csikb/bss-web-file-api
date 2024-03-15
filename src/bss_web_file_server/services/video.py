from collections import namedtuple
from io import BytesIO
from pathlib import Path
from uuid import UUID

from PIL import Image

from src.bss_web_file_server.settings import settings
from src.bss_web_file_server.models.video import Video


Poster = namedtuple("Poster", ["width", "height", "name"])
id_paths_base = Path(settings.server_base_path, "v")
url_paths_base = Path(settings.server_base_path, "video")
poster_sizes = [
    Poster(1920, 1080, "fhd"),
    Poster(1280, 720, "hd"),
    Poster(854, 480, "sd"),
]
img_formats = ["avif", "webp", "jpeg"]


def create_folder_structure(video: Video, with_symlinks=True):
    to_id_path(video.id).mkdir(parents=True, exist_ok=True)
    # create a folder for the thumbnails
    Path(to_id_path(video.id), "poster").mkdir(exist_ok=True)
    if with_symlinks:
        update_symlinks(video)


def create_thumbnails(content: bytes, video_id: UUID):
    # create a poster folder in the id folder
    poster_path = Path(to_id_path(video_id), "poster")
    with Image.open(BytesIO(content)) as image:
        for poster in poster_sizes:
            i = image.copy()
            i.thumbnail(size=(poster.width, poster.height))
            for img_format in img_formats:
                i.save(Path(poster_path, poster.name + "." + img_format))


def update_symlinks(video: Video):
    # this method will first remove all references to the id folder
    id_path = to_id_path(video.id)
    # find any symlink folders that would point to the id_path
    for p in url_paths_base.glob("*/"):
        if p.is_symlink() and p.readlink().samefile(id_path):
            # and remove them
            p.unlink(missing_ok=True)
    # create a new symlink to the id path
    # for each url
    for url_path in [to_url_path(url) for url in video.urls]:
        url_path.symlink_to(
            # use the absolute path to the id folder
            target=id_path.resolve(),
            target_is_directory=True
        )


def create_video_base_path():
    if not id_paths_base.exists():
        id_paths_base.mkdir(parents=True, exist_ok=True)
    if not url_paths_base.exists():
        url_paths_base.mkdir(parents=True, exist_ok=True)


def to_id_path(video_id: UUID):
    return Path(id_paths_base, str(video_id))


def to_url_path(video_url: str):
    return Path(url_paths_base, video_url)

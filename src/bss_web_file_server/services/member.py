"""This module contains all member related service logic."""

from pathlib import Path
from uuid import UUID

from ..models.member import Member
from ..settings import settings
from .image import ImgFormat, create_images

id_paths_base = Path(settings.server_base_path, "m")
url_paths_base = Path(settings.server_base_path, "member")


def create_folder_structure(member: Member):
    """
    This method will create the folder structure for a member.
    /m/{member.id}/profile
    And a symlink to the id folder from the url folder
    /member/{member.url} -> /m/{member.id}
    :param member: the member object
    :return: None
    """
    id_path = to_id_path(member.id)
    id_path.mkdir(parents=True, exist_ok=True)
    # create a folder for the profile pictures
    Path(id_path, "profile").mkdir(exist_ok=True)
    update_symlink(member)


def create_profile_picture(img_file: bytes, member_id: UUID):
    """
    This method will create the profile picture in different formats
    /m/{member.id}/profile/{size}.{format}
    :param img_file: the image file
    :param member_id: the id of the member
    :return: None
    """
    profile_picture_path = Path(to_id_path(member_id), "profile")
    profile_picture_sizes = [
        ImgFormat(1920, 1080, "xl"),
        ImgFormat(1280, 720, "l"),
        ImgFormat(854, 480, "m"),
    ]
    create_images(img_file, profile_picture_path, profile_picture_sizes)


def update_symlink(member: Member):
    """
    This method will update the symlink to the id folder from the url folder
    First it will remove all references to the id folder
    Then it will create a new symlink to the id path
    :param member: the member object
    :return: None
    """
    id_path = to_id_path(member.id)
    for url_path in url_paths_base.glob("*/"):
        if url_path.is_symlink() and url_path.readlink().samefile(id_path):
            url_path.unlink(missing_ok=True)
    to_url_path(member.url).symlink_to(
        # use the absolute path to the id folder
        target=id_path.resolve(),
        target_is_directory=True,
    )


# pylint: disable=duplicate-code
def create_member_base_path():
    """This method will create the parent folder for all id and url folders."""
    if not id_paths_base.exists():
        id_paths_base.mkdir(parents=True, exist_ok=True)
    if not url_paths_base.exists():
        url_paths_base.mkdir(parents=True, exist_ok=True)


def to_id_path(member_id: UUID):
    """
    This method will return the base path
    where the id folders for members are located.
    """
    return Path(id_paths_base, str(member_id))


def to_url_path(member_url: str):
    """
    This method will return the base path
    where the url folders for members are located.
    """
    return Path(url_paths_base, member_url)


# pylint: enable=duplicate-code

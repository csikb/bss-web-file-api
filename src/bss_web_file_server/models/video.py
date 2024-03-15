""" A module for storing the video model. """

from uuid import UUID

from pydantic import BaseModel


class Video(BaseModel):
    """A class for storing video data."""

    id: UUID
    urls: list[str]

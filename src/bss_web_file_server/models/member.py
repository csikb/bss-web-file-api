from uuid import UUID

from pydantic import BaseModel


class Member(BaseModel):
    id: UUID
    url: str

from typing import List

from pydantic import BaseModel, Field


class BookMetadata(BaseModel):
    id: str
    title: str
    authors: List[str] = Field(default_factory=list)
    path: str
    filename: str

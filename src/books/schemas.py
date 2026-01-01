from pydantic import BaseModel
from typing import Optional

class Book(BaseModel):
    id: int
    title: str
    author: str
    year_published: int

class BookUpdateModel(BaseModel):
    title: str | None = None
    author: str | None = None
    year_published: Optional[int] = None

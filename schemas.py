# schemas.py
from pydantic import BaseModel

class BookBase(BaseModel):
    title: str
    author: str
    description: str
    year: int

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int

    class Config:  # ✅ Capital C
        from_attributes = True  # ✅ Pydantic v2 style

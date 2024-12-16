from typing import Any, Dict, Optional
from pydantic import BaseModel

class BookBase(BaseModel):
    title: str
    author: str

class BookCreate(BookBase):
    pass

class BookResponse(BookBase):
    id: int
    image_path: Optional[str] = None

    class Config:
        orm_mode = True
        from_attributes = True

class ResponeModel(BaseModel):
    status: str
    message: str
    data: Optional[Dict[str, Any]] = None

    class Config:
        orm_mode = True
        from_attributes = True
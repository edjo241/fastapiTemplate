from pydantic import BaseModel

class AuthorBase(BaseModel):
    name: str
    age: int

class AuthorCreate(AuthorBase):
    pass

class AuthorResponse(AuthorBase):
    id: int

    class Config:
        orm_mode = True 
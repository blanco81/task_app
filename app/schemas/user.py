from uuid import UUID
from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

class UserCreate(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    id: UUID
    username: str

    class Config:
        orm_mode = True

from typing import Optional
from pydantic import BaseModel
from datetime import datetime
from pydantic.networks import EmailStr

from app.models import User



class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

class PostResponse(PostBase):
    id: int
    published: bool
    created_at: datetime
    user_id: int
    owner: UserResponse

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token : str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None

from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class ArticleCreate(BaseModel):
    title: str
    content: str
    image_url: Optional[str] = None
    source_url: Optional[str] = None

class ArticleResponse(BaseModel):
    id: int
    title: str
    content: str
    image_url: Optional[str]
    source_url: Optional[str]
    created_at: datetime

    class Config:
        from_attributes = True

class UserResponse(BaseModel):
    id: int
    username: str

    class Config:
        from_attributes = True  
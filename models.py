from pydantic import BaseModel,Field,EmailStr
from typing import Optional
import datetime

class User(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    

class Note(BaseModel):
    title: str
    content: str
    tags: list[str] = []
    created_at: Optional[datetime.datetime] = Field(default=None)
    updated_at: Optional[datetime.datetime] = Field(default=None)
    reminder_date: Optional[datetime.datetime] = Field(default=None)

    class Config:
        json_encoders = {
            datetime.datetime: lambda v: v.isoformat()
        }
    




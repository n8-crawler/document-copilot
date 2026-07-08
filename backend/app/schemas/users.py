from datetime import datetime
from uuid import UUID

from pydantic import BaseModel,EmailStr,ConfigDict

class UserCreate(BaseModel):
    username:str
    email:EmailStr
    password:str

class UserUpdate(BaseModel):
    username:str | None = None
    password:str | None = None

# class UserLogin(BaseModel):
#     email: EmailStr
#     password: str

class Token(BaseModel):
    access_token:str
    token_type:str

class UserResponse(BaseModel):
    id : UUID
    username:str
    email:EmailStr
    # this creates a python dict of users data rather than db object which cant be understood to pydantic so its serialing db object data
    model_config = ConfigDict(from_attributes = True)

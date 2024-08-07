from pydantic import BaseModel, EmailStr
from typing import List

class Blog(BaseModel):
    title:str
    body:str
    id: int

    class Config:
        from_attributes = True

class User(BaseModel):
    name:str
    email:EmailStr
    password:str
    id: int

class ShowUser(BaseModel):
    name: str
    email: EmailStr
    blogs: List[Blog]= []

    class Config:
        from_attributes = True

class ShowBlog(BaseModel):
    title: str
    body: str
    creator: ShowUser

    class Config:
        from_attributes = True

    
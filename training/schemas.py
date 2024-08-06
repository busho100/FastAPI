from pydantic import BaseModel, EmailStr

class Blog(BaseModel):
    title:str
    body:str
    id: int

    class Config:
        from_attributes = True

class ShowBlog(BaseModel):
    title: str
    body: str

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

    class Config:
        from_attributes = True
    
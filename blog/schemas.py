from pydantic import BaseModel
from typing import List

class BlogClass(BaseModel):
    title : str
    body : str

class Blog(BlogClass):
    class Config:
        from_attributes = True


class User(BaseModel):
    name : str
    email : str
    password : str

class ShowUser(BaseModel):
    name : str
    email : str
    #if we want to see all the blogs for the user
    blogs : List[Blog] = []
    class Config:
        from_attributes = True
    # password : str

class ShowBlog(BaseModel):
    title : str
    body : str
    creator : ShowUser
    class Config:
        from_attributes = True
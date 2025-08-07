from pydantic import BaseModel

class BlogClass(BaseModel):
    title : str
    body : str

# class ShowBlog(BlogClass):
#     class Config:
#         from_attributes = True


class User(BaseModel):
    name : str
    email : str
    password : str

class ShowUser(BaseModel):
    name : str
    email : str
    class Config:
        from_attributes = True
    # password : str

class ShowBlog(BaseModel):
    title : str
    body : str
    creator : ShowUser
    class Config:
        from_attributes = True
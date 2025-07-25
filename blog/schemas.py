from pydantic import BaseModel

class BlogClass(BaseModel):
    title : str
    body : str

# class ShowBlog(BlogClass):
#     class Config:
#         from_attributes = True

class ShowBlog(BaseModel):
    title : str
    body : str
    class Config:
        from_attributes = True
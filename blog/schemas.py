from pydantic import BaseModel

class BlogClass(BaseModel):
    title : str
    body : str

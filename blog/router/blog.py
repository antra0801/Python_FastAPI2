from fastapi import APIRouter , status, Depends
from typing import List
from sqlalchemy.orm import Session
from .. import schemas, database, model


router = APIRouter()


@router.get('/get-all-blogs', status_code=status.HTTP_200_OK , response_model= List[schemas.ShowBlog] , tags=['blogs'])
def allBlogs(db : Session = Depends(database.get_db)):
    blogs = db.query(model.Blog).all()
    # print(blogs)
    return blogs
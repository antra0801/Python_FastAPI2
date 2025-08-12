from fastapi import APIRouter , status, Depends, Response , HTTPException
from typing import List
from sqlalchemy.orm import Session
from .. import schemas, database, model
from ..repository import blog

router = APIRouter(
    prefix="/blog",
    tags=['blogs']
)


@router.get('/get-all-blogs', status_code=status.HTTP_200_OK , response_model= List[schemas.ShowBlog] )
def allBlogs(db : Session = Depends(database.get_db)):
    # blogs = db.query(model.Blog).all()
    # # print(blogs)
    # return blogs
    return blog.get_all_blogs(db)


@router.post('/', status_code= status.HTTP_201_CREATED )
def create(request_body : schemas.BlogClass, db : Session = Depends(database.get_db)):
    return blog.create(request_body , db)


@router.delete('/{id}',status_code = status.HTTP_204_NO_CONTENT)
def deleteBlog(id, db : Session = Depends(database.get_db)):
   return blog.remove_blog(id , db)



@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED )
def update(id , request_body : schemas.BlogClass , db : Session = Depends(database.get_db)):
    # print(request_body)
   return blog.update_blog(id , request_body , db)

# @router.get('/get-all-blogs', status_code=status.HTTP_200_OK , response_model= List[schemas.ShowBlog] , tags=['blogs'])
# def allBlogs(db : Session = Depends(get_db)):
#     blogs = db.query(model.Blog).all()
#     # print(blogs)
#     return blogs


@router.get('/get-blogs-by-id/{id}' , status_code=200, response_model=schemas.ShowBlog )
def getData(id, response: Response, db : Session = Depends(database.get_db)):
    # data = db.query(model.Blog).filter(model.Blog.id == id).first().body✅
   return blog.get_blog_by_id(id , db)

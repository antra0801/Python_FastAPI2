from fastapi import APIRouter , status, Depends, Response , HTTPException
from typing import List
from sqlalchemy.orm import Session
from .. import schemas, database, model


router = APIRouter(
    tags=['blogs']
)


@router.get('/get-all-blogs', status_code=status.HTTP_200_OK , response_model= List[schemas.ShowBlog] )
def allBlogs(db : Session = Depends(database.get_db)):
    blogs = db.query(model.Blog).all()
    # print(blogs)
    return blogs


@router.post('/blog1', status_code= status.HTTP_201_CREATED )
def create(request_body : schemas.BlogClass, db : Session = Depends(database.get_db)):
    new_blog = model.Blog(title = request_body.title , body = request_body.body, userId = 1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog



@router.delete('/blog/{id}',status_code = status.HTTP_204_NO_CONTENT)
def deleteBlog(id, db : Session = Depends(database.get_db)):
    blogQuery = db.query(model.Blog).filter(model.Blog.id == id)
    if not blogQuery.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"blog with id {id} not found.")
    blogQuery.delete(synchronize_session=False)
    db.commit()
    return {'detail':'id has deleted.'} 




@router.put('/blogUpdate/{id}', status_code=status.HTTP_202_ACCEPTED )
def update(id , request_body : schemas.BlogClass , db : Session = Depends(database.get_db)):
    print(request_body)
    blogQuery = db.query(model.Blog).filter(model.Blog.id == id)
    if not blogQuery.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"blog with id {id} not found.")
    blogQuery.update(request_body.dict())
    print(request_body.dict())
    db.commit()
    return"updated"
    # except Exception as e:
    #     raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR , detail=f"Update failed: {str(e)}")

# @router.get('/get-all-blogs', status_code=status.HTTP_200_OK , response_model= List[schemas.ShowBlog] , tags=['blogs'])
# def allBlogs(db : Session = Depends(get_db)):
#     blogs = db.query(model.Blog).all()
#     # print(blogs)
#     return blogs


@router.get('/get-blogs-by-id/{id}' , status_code=200, response_model=schemas.ShowBlog )
def getData(id, response: Response, db : Session = Depends(database.get_db)):
    # data = db.query(model.Blog).filter(model.Blog.id == id).first().body✅
    data = db.query(model.Blog).filter(model.Blog.id == id).first()

    if not data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=  f'Blog with the {id} is not available'
        )
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail' : f'Blog with the {id} is nor available'}
    return data

from sqlalchemy.orm import Session
from fastapi import HTTPException , status
from .. import model , schemas


def get_all_blogs(db : Session):
    blogs = db.query(model.Blog).all()
    # print(blogs)
    return blogs


def create(request_body: schemas.BlogClass, db : Session):
    new_blog = model.Blog(title = request_body.title , body = request_body.body, userId = 1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def remove_blog(id: int , db : Session):
    blogQuery = db.query(model.Blog).filter(model.Blog.id == id)
    if not blogQuery.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"blog with id {id} not found.")
    blogQuery.delete(synchronize_session=False)
    db.commit()
    return {'detail':'id has deleted.'} 

def update_blog(id: int ,request_body : schemas.BlogClass , db : Session):
    blogQuery = db.query(model.Blog).filter(model.Blog.id == id)
    if not blogQuery.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"blog with id {id} not found.")
    blogQuery.update(request_body.dict())
    print(request_body.dict())
    db.commit()
    return"updated"
    # except Exception as e:
    #     raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR , detail=f"Update failed: {str(e)}")


def get_blog_by_id(id: int , db : Session):
    data = db.query(model.Blog).filter(model.Blog.id == id).first()

    if not data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=  f'Blog with the {id} is not available'
        )
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail' : f'Blog with the {id} is nor available'}
    return data
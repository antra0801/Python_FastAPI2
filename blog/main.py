from fastapi import FastAPI, Depends , status , Response , HTTPException
from . import schemas, model
from .database import engine, SessionLocal
from sqlalchemy.orm import Session
from typing import List

app = FastAPI()

model.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/blog1', status_code= status.HTTP_201_CREATED)
def create(request_body : schemas.BlogClass, db : Session = Depends(get_db)):
    new_blog = model.Blog(title = request_body.title , body = request_body.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.delete('/blog/{id}',status_code = status.HTTP_204_NO_CONTENT)
def deleteBlog(id, db : Session = Depends(get_db)):
    blogQuery = db.query(model.Blog).filter(model.Blog.id == id)
    if not blogQuery.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"blog with id {id} not found.")
    blogQuery.delete(synchronize_session=False)
    db.commit()
    return 'done' 

@app.put('/blogUpdate/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id , request_body : schemas.BlogClass , db : Session = Depends(get_db)):
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

@app.get('/get-all-blogs', status_code=status.HTTP_200_OK , response_model= List[schemas.ShowBlog])
def allBlogs(db : Session = Depends(get_db)):
    blogs = db.query(model.Blog).all()
    # print(blogs)
    return blogs


@app.get('/get-blogs-by-id/{id}' , status_code=200, response_model=schemas.ShowBlog)
def getData(id, response: Response, db : Session = Depends(get_db)):
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

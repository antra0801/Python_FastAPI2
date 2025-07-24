from fastapi import FastAPI, Depends
from . import schemas, model
from .database import engine, SessionLocal
from sqlalchemy.orm import Session
app = FastAPI()

model.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/blog1')
def create(request_body : schemas.BlogClass, db : Session = Depends(get_db)):
    new_blog = model.Blog(title = request_body.title , body = request_body.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog
   

@app.get('/get-all-blogs')
def allBlogs(db : Session = Depends(get_db)):
    blogs = db.query(model.Blog).all()
    return blogs


@app.get('/get-blogs-by-id/{id}')
def getData(id, db : Session = Depends(get_db)):
    # data = db.query(model.Blog).filter(model.Blog.id == id).first().body✅
    data = db.query(model.Blog).filter(model.Blog.id == id).first()
    return data

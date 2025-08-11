from fastapi import FastAPI, Depends , status , Response , HTTPException
from . import schemas, model
from .database import engine, SessionLocal , get_db
from sqlalchemy.orm import Session
from typing import List
from .hashing import Hash
# from passlib.context import CryptContext
from .router import blog

app = FastAPI()



model.Base.metadata.create_all(engine)

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

app.include_router(blog.router)


# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@app.post('/user' , response_model=schemas.ShowUser , tags=['users'])
def create_user(request_body : schemas.User , db : Session = Depends(get_db)): 
    # hashedPassword = pwd_context.hash(request_body.password)
    newUser = model.User(name=request_body.name , email = request_body.email , password = Hash.bcrpyt(request_body.password))
    db.add(newUser)
    db.commit()
    db.refresh(newUser)
    return newUser

@app.get('/user/{id}' , response_model=schemas.ShowUser, tags=['users'])
def get_user(id:int , db : Session = Depends(get_db)):
    user = db.query(model.User).filter(model.User.id == id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with {id} id not found.")
    
    return user

@app.get('/all-users' , tags=['users'])
def allUsers(db : Session=Depends(get_db)):
    all_users_from_db = db.query(model.User).all()
    return all_users_from_db 

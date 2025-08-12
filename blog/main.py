from fastapi import FastAPI, Depends , status , Response , HTTPException
from . import schemas, model
from .database import engine, SessionLocal , get_db
from sqlalchemy.orm import Session
from typing import List
from .hashing import Hash
# from passlib.context import CryptContext
from .router import blog  , user
 
app = FastAPI()



model.Base.metadata.create_all(engine)

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

app.include_router(blog.router)

app.include_router(user.router)


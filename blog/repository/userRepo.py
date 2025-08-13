from sqlalchemy.orm import Session
from fastapi import HTTPException , status
from .. import model , schemas
from ..hashing import Hash

def create_user(request_body : schemas.ShowUser , db: Session):
    print(request_body)
    newUser = model.User(name=request_body.name , email = request_body.email , password = Hash.bcrpyt(request_body.password))
    db.add(newUser)
    db.commit()
    db.refresh(newUser)
    return newUser

def get_user_by_id(id: int , db: Session ):
    user = db.query(model.User).filter(model.User.id == id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with {id} id not found.")
    
    return user

def get_all_users(db: Session):
    all_users_from_db = db.query(model.User).all()
    # print(all_users_from_db)
    return all_users_from_db
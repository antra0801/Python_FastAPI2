from fastapi import APIRouter , Depends , HTTPException , status
from sqlalchemy.orm import  Session 
from typing import List
from .. import schemas, database, model 
from ..hashing import Hash

# hash_pass = hashing.Hash()

router = APIRouter(
    prefix='/user',
     tags=['users']
)

get_db = database.get_db
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@router.post('/' , response_model=schemas.ShowUser)
def create_user(request_body : schemas.User , db : Session = Depends(get_db)): 
    # hashedPassword = pwd_context.hash(request_body.password)
    newUser = model.User(name=request_body.name , email = request_body.email , password = Hash.bcrpyt(request_body.password))
    db.add(newUser)
    db.commit()
    db.refresh(newUser)
    return newUser

@router.get('/{id}' , response_model=schemas.ShowUser)
def get_user(id:int , db : Session = Depends(get_db)):
    user = db.query(model.User).filter(model.User.id == id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with {id} id not found.")
    
    return user

@router.get('/all-users')
def allUsers(db : Session=Depends(get_db)):
    all_users_from_db = db.query(model.User).all()
    return all_users_from_db 

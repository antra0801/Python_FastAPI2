from fastapi import APIRouter , Depends , HTTPException , status
from sqlalchemy.orm import  Session 
from typing import List
from .. import schemas, database, model
from ..hashing import Hash
from ..repository import userRepo

# hash_pass = hashing.Hash()

router = APIRouter(
    prefix='/user',
     tags=['users']
)

get_db = database.get_db
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@router.post('/' , response_model=schemas.ShowUser)
def create_user(request_body : schemas.User , db : Session = Depends(get_db)): 
    print(request_body)
    # hashedPassword = pwd_context.hash(request_body.password)
    return userRepo.create_user(request_body , db)

@router.get('/all-users', response_model= List[schemas.UserDetails])
def allUsers(db : Session=Depends(get_db)):
    return userRepo.get_all_users(db) 

@router.get('/{id}' , response_model=schemas.ShowUser)
def get_user(id:int , db : Session = Depends(get_db)):
   return userRepo.get_user_by_id(id , db)



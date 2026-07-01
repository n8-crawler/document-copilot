from app.database import get_db
from sqlalchemy.orm import Session
from fastapi import APIRouter,HTTPException,Depends,status
from uuid import UUID
from app.models.users import User
from app.schemas.users import UserCreate,UserResponse,UserUpdate
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

router = APIRouter(prefix='/users',tags=['User'])

def hash_password(password:str):
    return pwd_context.hash(password)

@router.get('/',response_model=list[UserResponse])
def get_all_users(db:Session = Depends(get_db)):
    return db.query(User).all()

@router.get('/{user_id}',response_model=UserResponse)
def get_user(user_id:UUID,db: Session = Depends(get_db)):
    try:
        return db.query(User).filter(User.id == user_id).first()
    except:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail='User not found')
    
@router.post('/',response_model = UserResponse,status_code=status.HTTP_201_CREATED,)
def create_user(request : UserCreate ,db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == request.email).first()
    if existing_user:
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST,detail='User already exists')
    
    user = User (
        username = request.username,
        password_hash = hash_password(request.password),
        email = request.email,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@router.put('/{user_id}',response_model=UserResponse,status_code=status.HTTP_201_CREATED)
def update_user(user_id : UUID,request:UserUpdate,db:Session=Depends(get_db)):

    existing_user = db.query(User).filter(User.id == user_id).first()
    print(existing_user)


    if not existing_user: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='User not found')

    if request.username is not None:
        existing_user.username = request.username
    if request.email is not None:
        existing_user.email = request.email
    
    db.commit()
    db.refresh(existing_user)

    return existing_user

@router.delete('/{user_id}')
def delete_user(user_id : UUID,db: Session= Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return {'message':'User already deleted'}
    db.delete(user)
    db.commit()
    return {'message':'User deleted Successfully'}

    



    







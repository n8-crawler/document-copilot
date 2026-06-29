from app.database import get_db
from sqlalchemy.orm import session
from fastapi import APIRouter,HTTPException,Depends,status
from uuid import UUID
from app.models.users import Users
from app.schemas.users import UserCreate,UserResponse,UserUpdate

router = APIRouter(prefix='/users',tags=['Users'])

@router.get('/',response_model='list[UserResponse]')
def get_all_users(db:session = Depends(get_db)):
    return db.query(Users).all()

@router.get('/{user_id}',response_model=UserResponse)
def get_user(user_id:UUID,db: session = Depends(get_db)):
    try:
        return db.query(Users).filter(Users.id == user_id).first()
    except:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail='User not found')
    
@router.post('/',response_model = UserResponse,status_code=status.HTTP_201_CREATED,)
def create_user(request = UserCreate ,db: session = Depends(get_db)):
    existing_user = db.query(Users).filter(Users.email == request.email).first()
    if existing_user:
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST,detail='User already exists')
    
    user = Users (
        username = request.username,
        password_hash = request.password,
        email = request.email,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@router.post('/{user_id}',response_model=UserResponse,status_code=status.HTTP_201_CREATED)
def update_user(user_id = UUID,db:session=Depends(get_db),request=UserUpdate):

    existing_user = db.query(Users).filter(Users.id == user_id).first()

    if existing_user: 
        HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='User not found')

    if request.username is not None:
        existing_user.username = request.username
    if request.email is not None and existing_user.id == request.id:
        existing_user.email = request.email
    else:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail='user with same email already exists')
    
    db.commit()

    return existing_user

@router.delete('/{user_id}')
def delete_user(user_id = UUID,db: session= Depends(get_db)):
    user = db.query(Users).filter(Users.id == user_id).first()
    if not user:
        return {'message':'User already deleted'}
    db.delete(user)
    db.commit()
    return {'message':'User deleted Successfully'}
 

    

    



    







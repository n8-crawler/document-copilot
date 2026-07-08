from app.database import get_db
from sqlalchemy.orm import Session
from fastapi import APIRouter,HTTPException,Depends,status
from uuid import UUID
from app.models.users import User
from app.schemas.users import UserCreate,UserResponse,UserUpdate
from app.services.authservice import AuthService
from app.routers.dependencies import get_current_user
from app.services.authservice import AuthService

router = APIRouter(prefix='/users',tags=['User'])

@router.get('/me',status_code=status.HTTP_200_OK)
def get_user(current_user:User=Depends(get_current_user)):
    return current_user

@router.put('/update_me',response_model=UserResponse,status_code=status.HTTP_201_CREATED)
def update_user(request:UserUpdate,current_user:User=Depends(get_current_user),db:Session=Depends(get_db)):

    if request.username is not None:
        current_user.username = request.username
    if request.password is not None :
        current_user.password_hash = AuthService(db).hash_password(request.password)
    
    db.commit()
    db.refresh(current_user)

    return current_user

@router.delete('/delete_me',status_code=status.HTTP_410_GONE)
def delete_user(current_user:User=Depends(get_current_user),db: Session= Depends(get_db)):
    db.delete(current_user)
    db.commit()
    return {'message':'User deleted Successfully'}



    







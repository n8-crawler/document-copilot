from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy import or_
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.users import UserCreate, UserResponse
from app.models.users import User
from fastapi.security import OAuth2PasswordRequestForm
from app.services.authservice import AuthService
from app.routers.jwt import JWTmanager

router = APIRouter(prefix='/auth',tags=['auth'])

@router.post('/register',response_model = UserResponse,status_code=status.HTTP_201_CREATED,)
def user_registration(request:UserCreate,db:Session=Depends(get_db)):
    service = AuthService(db)
    return service.register_user(request)

@router.post('/login')
def user_login(form_data: OAuth2PasswordRequestForm = Depends(),db:Session=Depends(get_db)):
    service = AuthService(db)
    return service.login(form_data)




    


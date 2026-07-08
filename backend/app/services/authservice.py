from sqlalchemy import or_
from fastapi import Depends, status,HTTPException
from app.routers.jwt import JWTmanager
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordRequestForm
from app.models.users import User
from app.schemas.users import UserCreate

class AuthService:

    def __init__(self,db:Session):
        self.db = db
        self.jwt = JWTmanager


    @staticmethod
    def hash_password(password: str):
        pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        return pwd_context.hash(password)

    
    def login (self,form_data:OAuth2PasswordRequestForm):
        user = self.db.query(User).filter(User.email == form_data.username).first()
        if user:
            if CryptContext(schemes=["bcrypt"], deprecated="auto").verify(form_data.password,user.password_hash):
                token = JWTmanager().createtoken(user_id = str(user.id))
                return {"access_token":token,"token_type":"bearer"}
            else:
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='Invalid credentials password')
        else: raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='Invalid credentials email')

    
    def register_user(self, request : UserCreate):
        existing_user = self.db.query(User).filter(User.email == request.email).first()
        if existing_user:
            raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST,detail='User already exists')
        
        user = User (
            username = request.username,
            password_hash = AuthService.hash_password(request.password),
            email = request.email,
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user



        
        
        



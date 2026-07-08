from fastapi.security import OAuth2PasswordBearer
from app.database import get_db
from app.models.users import User
from app.routers.jwt import JWTmanager
from  app.services.authservice import AuthService
from fastapi import HTTPException,Depends,status
from sqlalchemy.orm import Session

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/auth/login')

def get_current_user(token:str=Depends(oauth2_scheme),db:Session=Depends(get_db)):
    try:
        user_id = JWTmanager().verifytoken(token=token)
        user = db.query(User).filter(User.id == user_id).first()
        return user
    except:
        HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="INVALID TOKEN",headers={"WWW-Authenticate": "Bearer"})

    






from jose import jwt
from app.config import settings

class JWTmanager:
    def createtoken(self,user_id:str):
        payload = {'user_id':user_id}

        token = jwt.encode(payload,key=settings.JWT_SECRET_KEY,algorithm=settings.ALGORITHM)
        return token
    

    def verifytoken(self,token:str):
        payload = jwt.decode(token=token,key=settings.JWT_SECRET_KEY,algorithms=settings.ALGORITHM)
        user_id = payload.get('user_id',None)
        if not user_id:
            raise ValueError('invalid token')
        return user_id

from uuid import UUID

from sqlalchemy.orm import Session
from app.services.chatservice import Chatservice
from app.schemas.messages import MessageResponse,MessageCreate
from fastapi import APIRouter,HTTPException,status,Depends
from app.database import get_db
from app.models.users import User
from app.routers.dependencies import get_current_user


router = APIRouter(prefix='/my_assistant',tags=["ai_assistant"])

@router.post("/{thread_id}",response_model=MessageResponse,status_code=status.HTTP_200_OK)
def chat(thread_id:UUID,request:MessageCreate,current_user:User=Depends(get_current_user),db:Session=Depends(get_db)):
    return Chatservice(db).chat(thread_id=thread_id,current_user=current_user,request=request)
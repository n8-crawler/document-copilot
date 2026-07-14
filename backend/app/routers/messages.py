from app.database import get_db
from sqlalchemy.orm import Session
from fastapi import APIRouter,HTTPException,Depends,status
from uuid import UUID
from app.models.users import User
from app.schemas.messages import MessageCreate,MessageResponse
from app.services.messageservice import MessageService
from app.routers.dependencies import get_current_user
router = APIRouter(prefix='/messages',tags=['messages'])

@router.get("/{thread_id}",response_model=list[MessageResponse],status_code=status.HTTP_200_OK)
def get_messages(thread_id:UUID,db:Session=Depends(get_db),current_user : User=Depends(get_current_user)):
    return MessageService(db).get_messages(thread_id=thread_id,current_user=current_user)

@router.post("/usermessage/{thread_id}",response_model=MessageResponse,status_code=status.HTTP_201_CREATED)
def create_user_message(request:MessageCreate,thread_id:UUID,db:Session=Depends(get_db),current_user : User=Depends(get_current_user)):
    return MessageService(db).createusermessage(request=request,thread_id=thread_id,current_user=current_user)

# didnt create a route for ai message because it will be created by the system and not by the user so endpoint neednot be exposed to the user
# def create_ai_message(content:str,thread_id:UUID,db:Session=Depends(get_db)):
#     return MessageService(db).createassistantmessage(thread_id=thread_id,content=content)



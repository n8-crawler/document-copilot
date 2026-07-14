from uuid import UUID

from fastapi import status,HTTPException
from sqlalchemy.orm import Session
from app.schemas.messages import MessageCreate,MessageResponse
from app.services.threadservice import ThreadService
from app.models.chatmessage import ChatMessage
from app.models.users import User

class MessageService:
    def __init__(self,db:Session):
        self.db = db

    def createusermessage(self,thread_id:UUID,current_user:User,request:MessageCreate):
        current_thread = ThreadService(self.db).get_thread(thread_id=thread_id,current_user=current_user)
        if not current_thread:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Thread not found')
        chat = ChatMessage(
            thread_id = current_thread.id,
            role = 'user',
            messages = request.messages
        )
        self.db.add(chat)
        self.db.commit()
        self.db.refresh(chat)
        return chat
    
    #chat assistant will only store ai messages for 1 perticular message thread
    def createassistantmessage(self,thread_id:UUID,content:str):
            ai_chat = ChatMessage(
                thread_id=thread_id,
                role = 'AI assistant',
                messages = content
            )
            self.db.add(ai_chat)
            self.db.commit()
            self.db.refresh(ai_chat)
            return ai_chat

    def get_messages(self,thread_id:UUID,current_user:User):
        current_thread = ThreadService(self.db).get_thread(thread_id=thread_id,current_user=current_user)
        all_messages = self.db.query(ChatMessage).filter(ChatMessage.thread_id==current_thread.id).order_by(ChatMessage.created_at).all()
        return all_messages




from fastapi import Depends
from fastapi import Depends, status,HTTPException
from app.schemas.threads import ChatCreate,ChatUpdate
from sqlalchemy.orm import Session
from app.models.chatthreads import ChatThread
from app.models.users import User

class ThreadService:
    def __init__(self,db:Session):
        self.db = db
    
    def create_thread(self,current_user:User,request:ChatCreate):
        thread = ChatThread(
            user_id = current_user.id,
            title = request.title
        )
        self.db.add(thread)
        self.db.commit()
        self.db.refresh(thread)
        return thread

    def get_threads(self,current_user:User):
        threads = self.db.query(ChatThread).filter(ChatThread.user_id ==current_user.id).order_by(ChatThread.updated_at.desc()).all()
        return threads
    
    def get_thread(self,thread_id,current_user:User):
        thread = self.db.query(ChatThread).filter(ChatThread.id == thread_id,ChatThread.user_id==current_user.id).first()
        return thread
    
    def update_thread(self,thread_id,current_user:User,request:ChatUpdate):
        thread = self.get_thread(thread_id=thread_id,current_user=current_user)
        if thread.title is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Thread not found')
        thread.title = request.title
        self.db.commit()
        self.db.refresh(thread)
        return thread
        
    def delete_thread(self,thread_id,current_user:User):
        thread = self.get_thread(thread_id=thread_id,current_user=current_user)
        title = thread.title
        if thread.title is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Thread not found')
        self.db.delete(thread)
        self.db.commit()
        return {"message":"Your chat with title: {title} deleted successfully"}



from datetime import datetime
from uuid import uuid4

from sqlalchemy import Column, DateTime, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.database import base
from sqlalchemy.dialects.postgresql import UUID

class ChatThread(base):
    __tablename__ = "chat_threads"

    id = Column(UUID(as_uuid=True),primary_key=True,default=uuid4)
    user_id = Column(UUID(as_uuid=True),ForeignKey('users.id',ondelete='CASCADE'),nullable=False)
    title = Column(String(100),nullable=False)
    created_at = Column(DateTime,default=datetime.now)
    updated_at = Column(DateTime,default=datetime.now)

    user = relationship('User',back_populates='chatthreads')
    messages = relationship('ChatMessage',back_populates='thread',cascade='all, delete-orphan',order_by='ChatMessage.created_at')

from datetime import datetime
from uuid import uuid4

from sqlalchemy import Column, DateTime, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.database import base
from sqlalchemy.dialects.postgresql import UUID

class Chatthreads(base):
    __tablename__ = "chat_threads"

    id = Column(UUID(as_uuid=True),primary_key=True)
    user_id = Column(UUID(as_uuid=True),ForeignKey('users.id',ondelete='CASCADE'),nullable=False)
    title = Column(String(100),nullable=False)
    created_at = Column(DateTime,default=datetime.now)
    updated_at = Column(DateTime,default=datetime.now)

    user = relationship('Users',back_populates='chat_threads')
    messages = relationship('ChatMessage',back_populates='threads',cascade='all, delete-orphan',order_by='ChatMessage.created_at')

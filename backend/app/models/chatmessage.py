from datetime import datetime
from uuid import uuid4

from sqlalchemy import Column, DateTime, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.database import base
from sqlalchemy.dialects.postgresql import UUID

class ChatMessage(base):
    __tablename__ = "chat_messages"

    id = Column(UUID(as_uuid=True),primary_key=True)
    thread_id = Column(UUID(as_uuid=True),ForeignKey('chat_threads.id',ondelete='CASCADE'),nullable=False)
    role = Column(String(20),nullable=False)
    messages = Column(Text,nullable=False)
    prompt_tokens = Column(Integer)
    completion_tokens = Column(Integer)
    created_at = Column(DateTime,default = datetime.now)

    thread = relationship('ChatThread',back_populates='messages')

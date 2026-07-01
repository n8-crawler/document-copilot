from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID
from app.database import base
from sqlalchemy import Column,DateTime,Boolean,String
from sqlalchemy.orm import relationship
from uuid import uuid4


class User(base):
    __tablename__ = 'users'
    id = Column(UUID(as_uuid=True),primary_key=True,default=uuid4)
    username = Column(String,nullable=False)
    password_hash = Column(String,nullable=False)
    email = Column(String,unique=True,index=True,nullable=False)
    created_on = Column(DateTime,default=datetime.now)

    documents = relationship('SourceDocument',back_populates='user', cascade="all, delete-orphan")
    chatthreads = relationship('ChatThread',back_populates='user', cascade="all, delete-orphan")


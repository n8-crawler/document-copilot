from datetime import datetime
from uuid import uuid4

from sqlalchemy import Column, DateTime, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import base
from sqlalchemy.dialects.postgresql import UUID

class SourceDocuments(base):
    __tablename__ = 'source_documents'
    id = Column(UUID(as_uuid=True),primary_key=True,default=uuid4)
    user_id = Column(UUID(as_uuid=True),ForeignKey('users.id',ondelete='CASCADE'),nullable=False)
    filename = Column(String,nullable=False)
    filepath = Column(String,nullable=False)
    total_chunks = Column(Integer,default=0)
    status = Column(String,default='processing')  # pending, processing, completed
    created_on = Column(DateTime,default=datetime.now)

    user = relationship('Users' ,back_populates='sourcedocuments')
    chunks = relationship('DocumentChunk',back_populates='sourcedocument')
    



from datetime import datetime
from uuid import uuid4

from sqlalchemy import Column, DateTime, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.database import base
from sqlalchemy.dialects.postgresql import UUID

class DocumentChunk(base):
    __tablename__ = 'document_chunks'
    id = Column(UUID(as_uuid=True),primary_key=True,default=uuid4)
    document_id = Column(UUID(as_uuid=True),ForeignKey('source_documents.id',ondelete='CASCADE'),nullable=False)
    chunk_index = Column(Integer,nullable = False)
    content = Column(Text,nullable=False)
    embedding_model = Column(String(100))
    token_count = Column(Integer)
    created_at = Column(DateTime,default=datetime.now)

    document_chunk = relationship('SourceDocuments',back_populates='chunks')





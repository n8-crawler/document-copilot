from datetime import datetime
from uuid import uuid4

from sqlalchemy import Column, DateTime, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import base
from sqlalchemy.dialects.postgresql import UUID

class SourceDocument(base):
    __tablename__ = 'source_documents'
    id = Column(UUID(as_uuid=True),primary_key=True,default=uuid4)
    user_id = Column(UUID(as_uuid=True),ForeignKey('users.id',ondelete='CASCADE'),nullable=False)
    ticker = Column(String,index=True,nullable=False)
    cik = Column(String,index=True,nullable=False)
    accession_number = Column(String,index=True,unique=True,nullable=False)
    form = Column(String,nullable=False)
    filing_date = Column(DateTime,index=True,nullable=False)
    report_date = Column(DateTime,nullable=False)
    source_url = Column(String,nullable=False)
    filename = Column(String,nullable=False)
    filepath = Column(String,nullable=False)
    created_on = Column(DateTime,default=datetime.now)

    user = relationship('User' ,back_populates='documents')
    chunks = relationship('DocumentChunk',back_populates='document_chunk')
    



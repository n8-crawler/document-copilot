from sqlalchemy.orm import Session
from app.models.documentchunks import DocumentChunk

class Embeddingloader:
    def __init__(self,db:Session):
        self.db = db
    def save_embedding(self,chunk:DocumentChunk,embedding:list[float],embedding_model:str):
        chunk.embedding = embedding
        print('embedding saved to chunk')
        
        


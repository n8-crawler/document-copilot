from sqlalchemy.orm import Session
from app.models.documentchunks import DocumentChunk

class Retriver:
    def __init__(self,db:Session):
        self.db = db
    def retriver(self,query_embedding:list[float],top_k = 5):
        # we need to get embeddings vectors  nearesrt to user qns input and output result will sqlAlchemy obj so we can get result.content,result.id etc...
        result = self.db.query(DocumentChunk).filter(DocumentChunk.embedding != None ).order_by(DocumentChunk.embedding.cosine_distance(query_embedding)).limit(top_k).all()
        return result


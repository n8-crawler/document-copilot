from sqlalchemy.orm import Session
from app.models.documentchunks import DocumentChunk
from app.retrieval.reranker import Reranker
class Retriver:
    def __init__(self,db:Session):
        self.db = db
    def retrive(self,query:str,query_embedding:list[float],top_k = 30):
        # we need to get embeddings vectors  nearesrt to user qns input and output result will sqlAlchemy obj so we can get result.content,result.id etc...
        #vector search
        result = self.db.query(DocumentChunk).filter(DocumentChunk.embedding != None ).order_by(DocumentChunk.embedding.cosine_distance(query_embedding)).limit(top_k).all()
        chunks = Reranker().rerank(query=query,chunks=result)
        return chunks


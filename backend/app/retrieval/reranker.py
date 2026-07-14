from sentence_transformers import CrossEncoder

class Reranker:
    def __init__(self):
        self.model = CrossEncoder("BAAI/bge-reranker-base")
    def rerank(self,query:str,chunks:list,top_k:int=10):
        if not chunks:return []
        pairs = [(query,chunk.content) for chunk in chunks]
        scores = self.model.predict(inputs=pairs)
        # sort on basis of scores (key=lambda x: x[0],reverse=True) and return top_k
        ranks = sorted(zip(scores,chunks),key = lambda x: x[0],reverse=True) 
        return [chunk for _ , chunk in ranks[:top_k]]

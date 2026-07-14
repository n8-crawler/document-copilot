from app.config import settings
from app.cache.embedding_cache import EmbeddingCache
from sentence_transformers import SentenceTransformer
# using open source hugging face transformers
class EmbeddingGenerator:
    def __init__(self):
        self.model = SentenceTransformer(model_name_or_path=settings.EMBEDDING_MODEL)
        print('model loaded')

    def generate_embeddings(self,text:str):
        # receives text and create embeddings [0.021,-0.119,...]
        #cache
        embedding = EmbeddingCache.get(text)
        if embedding:
            print('got from embedding cache')
            return embedding

        embedding = self.model.encode(text,normalize_embeddings=True,convert_to_numpy=True,device="cpu") 
        #saved to cache
        EmbeddingCache.set(text,embedding)
        print('embedding generated')
        return embedding.tolist()
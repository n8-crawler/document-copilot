from app.config import settings
from sentence_transformers import SentenceTransformer
# using open source hugging face transformers
class EmbeddingGenerator:
    def __init__(self):
        self.model = SentenceTransformer(model_name_or_path=settings.EMBEDDING_MODEL)
        print('model loaded')

    def generate_embeddings(self,text:str):
        # receives text and create embeddings [0.021,-0.119,...]
        embedding = self.model.encode(text,normalize_embeddings=True,convert_to_numpy=True,device="cpu") 
        print('embedding generated')
        return embedding.tolist()
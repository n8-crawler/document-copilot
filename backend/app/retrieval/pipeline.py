from app.database import sessionlocal
from app.embeddings.generator import EmbeddingGenerator
from app.retrieval.retriever import Retriver


def retrieval_pipeline(user_query:str):
    db = sessionlocal()
    # user_query = "products sold by apple"
    generator = EmbeddingGenerator()
    embeddings = generator.generate_embeddings(user_query)
    
    matching_chunks = Retriver(db=db).retrive(query=user_query,query_embedding=embeddings)
    context_builder = [chunk for chunk in matching_chunks] # all chunk is a sql Alchemy object so we retrive its id,document,uuid,content etc..
    return context_builder

if __name__ == "__main__":
    retrieval_pipeline()

from app.embeddings.generator import EmbeddingGenerator
from app.embeddings.loader import Embeddingloader
from app.models.documentchunks import DocumentChunk
from app.config import settings
from uuid import UUID
from sqlalchemy.orm import Session
from app.database import sessionlocal

USER_ID = UUID("109d8916-16b9-42a9-ad93-e73ab8ced4de")  

def run_pipeline():
    db: Session = sessionlocal()
    all_rows = db.query(DocumentChunk).filter(DocumentChunk.embedding == None).all()
    load_model =EmbeddingGenerator()

    for rows in all_rows:
        content_text = rows.content
        embeddings = load_model.generate_embeddings(content_text)
        # here rows are actual sqlalchemy objects having DocumentChunk.embedding == None only those are processed
        Embeddingloader(db).save_embedding(chunk=rows,embedding=embeddings,embedding_model=settings.EMBEDDING_MODEL)
        
    db.commit()
    print('Embeddings saved to Db')
    db.close()

if __name__== "__main__":
    
    run_pipeline()








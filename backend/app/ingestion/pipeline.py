from app.ingestion.manifest import Manifest_reader
from app.ingestion.parser import HTMLParser
from app.ingestion.loader import DocumentLoader
from app.ingestion.chunker import Chunker
from app.database import sessionlocal
from pathlib import Path
from uuid import UUID

USER_ID = UUID("109d8916-16b9-42a9-ad93-e73ab8ced4de")  
PROJECT_ROOT = Path(__file__).resolve().parents[3]
def run_pipeline():
    db = sessionlocal()
    manifest = Manifest_reader(PROJECT_ROOT / "data" / "downloads" / "manifest.json")
    filings = manifest.read_filings()
    for filing in filings:
        print(filing)
        parsing_doc = HTMLParser().docling_parser(filing.local_path)
        print(type(parsing_doc))
        chunk = Chunker().create_chunks(document=parsing_doc)
        load_document = DocumentLoader(db).savedocument(filings=filing,user_id=USER_ID)
        DocumentLoader(db).save_document_chunks(document=load_document,document_chunks = chunk)
        
if __name__ == "__main__":

    run_pipeline()
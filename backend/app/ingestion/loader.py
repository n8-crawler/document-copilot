from datetime import datetime
from pathlib import Path
from sqlalchemy.orm import Session
from app.models.sourcedocuments import SourceDocument
from app.models.documentchunks import DocumentChunk
from app.ingestion.manifest import Filings
from app.ingestion.chunker import Chunker
from docling.chunking import HybridChunker

class DocumentLoader:
    PROJECT_ROOT = Path(__file__).resolve().parents[3]


    def __init__(self,db:Session):
        self.db = db


    def savedocument(self,filings:Filings,user_id):
        document = SourceDocument(
            user_id = user_id,
            ticker = filings.ticker,
            cik = filings.cik,
            accession_number = filings.accession_number,
            form = filings.form,
            filing_date = datetime.fromisoformat(filings.filing_date),
            report_date = datetime.fromisoformat(filings.report_date),
            source_url = filings.source_url,
            filename = filings.local_path.name,
            filepath = str(filings.local_path),
        )
        self.db.add(document)
        self.db.commit()
        self.db.refresh(document)
        return document

    def save_document_chunks(self,document : SourceDocument,document_chunks):
        chunker = HybridChunker()

        for index,chunks in enumerate(document_chunks):
            enriched_text = chunker.contextualize(chunk=chunks)
            document_chunk = DocumentChunk(
                document_id = document.id,
                chunk_index = index,
                content = enriched_text,
                token_count = None
            )
            self.db.add(document_chunk)
        self.db.commit()
        self.db.refresh(document_chunk)








from docling.chunking import HybridChunker

class Chunker:
    def create_chunks(self,document):
        chunker = HybridChunker()
        chunk_iter = chunker.chunk(dl_doc=document)
        return chunk_iter


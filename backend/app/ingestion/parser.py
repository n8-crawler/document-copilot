from pathlib import Path

from bs4 import BeautifulSoup
from docling.document_converter import DocumentConverter


class HTMLParser:
    
    def docling_parser(self,html_path):

        source = html_path 
        if not html_path.exists():
            raise FileNotFoundError(f"{html_path} not found")
        converter = DocumentConverter()
        result = converter.convert(source)
        docling_doc = result.document
        markdown = result.document.export_to_markdown()
        # downloads -> markdown

        PROJECT_ROOT = Path(__file__).resolve().parents[3]
        download_root = PROJECT_ROOT/"data"/"downloads"
        markdown_root = PROJECT_ROOT/"data"/"markdown"
        relative_path = html_path.relative_to(download_root)
        markdown_path = (markdown_root / relative_path).with_suffix(".md")

        # Create folders if they don't exist

        markdown_path.parent.mkdir(parents=True,exist_ok=True)
        # Save markdown
        with open(markdown_path, "w", encoding="utf-8") as f:
            f.write(markdown)

        return docling_doc
       
# obj = HTMLParser()
# print(obj.docling_parser(Path('data/downloads/2021/googl_10-k_2022-02-02_0001652044-22-000019.htm')))
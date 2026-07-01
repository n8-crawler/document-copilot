import json
from pathlib import Path
from dataclasses import dataclass
@dataclass
class Filings:
    ticker: str
    cik: str
    form: str
    filing_date: str
    report_date: str
    accession_number: str
    primary_document: str
    source_url: str
    local_path: Path

class Manifest_reader:
    def __init__(self,manifest_path:Path):
        self.manifest = manifest_path

    def read_filings(self):


        if not self.manifest.exists():
            raise FileNotFoundError(f"manifest.json not found in this path {self.manifest}")
        
        with open(self.manifest,'r',encoding='utf-8') as f:
            data = json.load(f)

        data_root_path = self.manifest.parent
        
        fillings = []
        for item in data['filings']:
            local_path = data_root_path / item['local_path']
            print(local_path)
            fillings.append(Filings(
                ticker=item['ticker'],
                cik=item['cik'],
                form=item['form'],
                filing_date=item['filing_date'],
                report_date=item['report_date'],
                accession_number=item['accession_number'],
                primary_document=item['primary_document'],
                source_url=item['source_url'],
                local_path=local_path
            ))
        return fillings

        

# obj = Manifest_reader(Path("data/downloads/manifest.json"))
# print(obj.read_fillings())
from dataclasses import dataclass

@dataclass
class Paper:
    name: str
    doi: str
    url: str
    publication_date: str
    authors: str
    quotations: int  

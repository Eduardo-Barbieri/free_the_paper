from dataclasses import dataclass
from typing import List


@dataclass
class Paper:
    name: str
    url: str
    publication_date: str
    authors: List[str]
    quotations: int

from typing import List
import requests


from utils.paper import Paper


class SchoolarGoogle:
    def __init__(self, session: requests.Session):
        self.session = session

    def get_papers(self, keyword: str) -> List[Paper]:
        url = f"https://scholar.google.com/scholar?hl=en-US&as_sdt=0%2C5&q={keyword}&btnG="
        response = self.session.get(url=url)
        ...

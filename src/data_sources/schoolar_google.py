import requests

import bs4

from utils.exceptions import PapersNotFoundError
from data_sources.data_source import DataSource


class SchoolarGoogle(DataSource):
    def __init__(self, session: requests.Session):
        self.session = session

    def get_papers(self, keyword: str):
        url = f"https://scholar.google.com/scholar?hl=en-US&as_sdt=0%2C5&q={keyword}&btnG="
        response = self.session.get(url=url)
        try:
            assert response.ok
        except AssertionError:
            raise PapersNotFoundError("Error querying google schoolar")
        return response

    def _parse_response_html(self, response: requests.Response):
        ...

import requests
import bs4

from data_sources.data_source import DataSource
from utils.paper import Paper
from utils.exceptions import NoUrlAvailableError


class SciHub(DataSource):

    def __init__(self, session: requests.Session):
        self.session = session

    @staticmethod
    def _get_mirrors():
        return 'sci-hub.se', 'sci-hub.st', 'sci-hub.ru'

    def get_html(self, paper: Paper):
        mirrors = self._get_mirrors()
        body = {
                "request": paper.url
                }
        for mirror in mirrors:
            try:
                response = self.session.get(url=f"https://{mirror}/{body['request']}")
                return response
            except Exception:
                raise NoUrlAvailableError

    def parse_html(self, response: requests.Response):
        soup = bs4.BeautifulSoup(response.content, "html.parser")
        pdf_path = soup.find("embed").get("src")
        pdf_path = pdf_path[:pdf_path.find("#")]
        pdf = self.session.get(url=f"https:{pdf_path}")
        ...


    def get_paper_content(self):
        ...

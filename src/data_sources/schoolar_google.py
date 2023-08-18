import requests

import bs4

from data_sources.data_source import DataSource
from utils.exceptions import PapersNotFoundError
from utils.paper import Paper


class SchoolarGoogle(DataSource):
    def __init__(self, session: requests.Session):
        self.session = session

    # TODO:
    # * implement as list to get more than a single page;
    # * improve headers in url;
    def get_html(self, keyword: str):
        url = f"https://scholar.google.com/scholar?hl=en-US&as_sdt=0%2C5&q={keyword}&btnG="
        response = self.session.get(url=url)
        try:
            assert response.ok
        except AssertionError:
            raise PapersNotFoundError("Error querying google schoolar")
        return response

    def parse_html(self, response: requests.Response):
        soup = bs4.BeautifulSoup(response.content, 'html.parser')
        papers_div = soup.find_all("div", {"class": "gs_r gs_or gs_scl"})
        papers = []
        for paper_div in papers_div:
            autor_date = paper_div.find("div", {"class": "gs_a"}).get_text()
            date = autor_date[
                autor_date.rfind('-') - 5:autor_date.rfind('-') - 1
            ]
            autors = autor_date[:autor_date.find('-')].replace(u'\xa0', '').split(',')
            # TODO:
            for extra_refs in paper_div.find("div",{"class": "gs_fl"}):
                ...
            paper = Paper(
                    name=paper_div.find("h3", {"class": "gs_rt"}).get_text(),
                    url=str(paper_div.find("a").get("href")),
                    publication_date=date,
                    authors=autors,
                    quotations=1,
                )
            papers.append(paper)
        return papers

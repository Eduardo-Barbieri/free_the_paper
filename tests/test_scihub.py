import unittest

from data_sources.scihub import SciHub
from utils.session import create_session
from utils.paper import Paper


HEADERS = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:27.0) Gecko/20100101 Firefox/27.0'
            }
session = create_session(HEADERS)
sci = SciHub(session)
paper = Paper(
        name="test",
        url="https://www.bmj.com/content/328/7447/1073.short",
        publication_date="",
        authors=[""],
        quotations=1
        )


class TestingSchoolarGoogle(unittest.TestCase):
    def test_scihub_get(self):
        self.assertEqual(sci.get_html(paper).status_code, 200)

    def test_scihub_parse_html(self):
        sci.parse_html(sci.get_html(paper))
        ...

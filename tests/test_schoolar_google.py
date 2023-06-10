import unittest

from data_sources.schoolar_google import SchoolarGoogle
from utils.session import create_session

# TODO test proxy implementation;

HEADERS = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:27.0) Gecko/20100101 Firefox/27.0'
            }
session = create_session(HEADERS)
scg = SchoolarGoogle(session)
request1 = scg.get_html("test")
request2 = scg.get_html("jumping mice")


class TestingSchoolarGoogle(unittest.TestCase):

    def test_get_html_request(self):
        self.assertEqual(request1.status_code, 200)
        self.assertEqual(request2.status_code, 200)

    def test_parse_html(self):
        self.assertEqual(len(scg.parse_html(request1)), 10)

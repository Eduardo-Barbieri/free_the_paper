import requests
from typing import Dict


def create_session(headers: dict, **kwargs) -> requests.Session:
    session = requests.Session()  
    session.headers.update(headers)
    session.proxies.update(kwargs.get('proxies'))
    return session

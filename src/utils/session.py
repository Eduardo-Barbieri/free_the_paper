import requests


def create_session(headers: dict, **kwargs) -> requests.Session:
    session = requests.Session()
    session.headers.update(headers)
    proxies = kwargs.get('proxies')
    if proxies:
        session.proxies.update(proxies)
    return session

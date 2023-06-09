from abc import ABC, abstractmethod
from typing import List

import requests

from utils.paper import Paper


class DataSource(ABC):
    @abstractmethod
    def get_papers(self, *args, **kwargs) -> requests.Response:
        ...

    @abstractmethod
    def _parse_response_html(self, *args, **kwargs) -> List[Paper]:
        ...

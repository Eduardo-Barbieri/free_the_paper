from abc import ABC, abstractmethod
from typing import List

import requests

from utils.paper import Paper


class DataSource(ABC):
    @abstractmethod
    def get_html(self, *args, **kwargs) -> requests.Response:
        ...

    @abstractmethod
    def parse_html(self, *args, **kwargs) -> List[Paper]:
        ...

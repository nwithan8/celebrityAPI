from bs4 import BeautifulSoup

from models.base import BaseObject


class CelebrityBrief(BaseObject):
    def __init__(self, name: str, imdb_id: str = None, tmdb_id: str = None):
        super().__init__()
        self.name = name
        self.imdb_id = imdb_id
        self.tmdb_id = tmdb_id


class Celebrity(CelebrityBrief):
    def __init__(self, name: str, **kwargs):
        super().__init__(name=name)
        self.__dict__.update(kwargs)

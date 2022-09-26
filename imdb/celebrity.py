from bs4 import BeautifulSoup

from imdb.imdb_object import ImdbObject


class CelebrityBrief(ImdbObject):
    def __init__(self, imdb_id: str, name: str):
        super().__init__()
        self.imdb_id = imdb_id
        self.name = name


class Celebrity(CelebrityBrief):
    def __init__(self, imdb_id: str, name: str, **kwargs):
        super().__init__(imdb_id=imdb_id, name=name)
        self.__dict__.update(kwargs)


def make_celebrity_brief_from_list_entry(celebrity: BeautifulSoup) -> CelebrityBrief:
    imdb_id: str = celebrity.find("a").get("href").split("/")[2].strip()
    name: str = celebrity.find("a").text.strip()

    return CelebrityBrief(imdb_id=imdb_id, name=name)

from typing import List, Union

import requests
from bs4 import BeautifulSoup
from objectrest import get
from datetime import datetime

from models.celebrity import CelebrityBrief, Celebrity
from connectors import tmdb_person_id_from_imdb_id
from utils import yyyy_mm_dd, today, clean_date_string


async def _get_all_imdb_list_items(url: str, params: dict) -> List[BeautifulSoup]:
    items = []

    has_more = True
    while has_more:
        response: requests.Response = get(url=url, params=params)
        soup: BeautifulSoup = BeautifulSoup(response.text, "html.parser")
        item_list_data: list = soup.find_all("div", {"class": "lister-item-content"})
        items.extend(item_list_data)
        has_more_tag = soup.find("a", {"class": "lister-page-next next-page"})
        if has_more_tag is None:
            has_more = False
        params["start"] += 50

    return items


def make_celebrity_brief_from_imdb_list_entry(celebrity: BeautifulSoup) -> CelebrityBrief:
    imdb_id: str = celebrity.find("a").get("href").split("/")[2].strip()
    name: str = celebrity.find("a").text.strip()

    return CelebrityBrief(imdb_id=imdb_id, name=name)


async def get_celebrity_deaths(start_date: datetime, end_date: datetime = None, single_day: bool = False) \
        -> Union[List[CelebrityBrief], None]:
    end_date = end_date if end_date else (start_date if single_day else today())

    url: str = f"https://www.imdb.com/search/name/"
    params: dict = {
        "death_date": f"{yyyy_mm_dd(start_date)},{yyyy_mm_dd(end_date)}",
        "has": "death-date",
        "sort": "death_date,desc",
        "start": 1
    }

    items: List[BeautifulSoup] = await _get_all_imdb_list_items(url=url, params=params)

    if len(items) == 0:
        return None

    celebrities: List[CelebrityBrief] = [make_celebrity_brief_from_imdb_list_entry(item) for item in items]

    return celebrities


async def get_celebrity_details(imdb_id: str, tmdb_api_key: str) -> Celebrity:
    url: str = f"https://www.imdb.com/name/{imdb_id}/"
    response: requests.Response = get(url=url)
    soup: BeautifulSoup = BeautifulSoup(response.text, "html.parser")

    celebrity_details: dict = {}

    # Name
    name: str = soup.find_all("span", {"class": "itemprop"})[0].text.strip()

    # Position
    celebrity_details["type"]: str = soup.find_all("span", {"class": "itemprop"})[1].text.strip()

    # Birth date
    try:
        birth_date: Union[str, None] = soup.find("div", {"id": "name-born-info"}).find("time")["datetime"].strip()
        birth_date = clean_date_string(date_string=birth_date)
    except:
        birth_date: Union[str, None] = None
    celebrity_details["birth_date"]: Union[str, None] = birth_date

    # Death date
    try:
        death_date: Union[str, None] = soup.find("div", {"id": "name-death-info"}).find("time")["datetime"].strip()
        death_date = clean_date_string(date_string=death_date)
    except:
        death_date: Union[str, None] = None
    celebrity_details["death_date"]: Union[str, None] = death_date

    # TMDB ID
    tmdb_id: str = tmdb_person_id_from_imdb_id(imdb_id=imdb_id, tmdb_api_key=tmdb_api_key)
    celebrity_details["tmdb_id"]: Union[str, None] = tmdb_id

    return Celebrity(imdb_id=imdb_id, name=name, **celebrity_details)

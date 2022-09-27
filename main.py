import os
from typing import Dict, List

from fastapi import FastAPI

from connectors import imdb
from models.celebrity import Celebrity, CelebrityBrief
from utils import *

app = FastAPI()

tmdb_api_key = os.environ.get("TMDB_API_KEY")


@app.get("/")
async def root():
    return {"message": "The princess is in another castle!"}


@app.get("/celebrity/details/{imdb_id}")
async def celebrity_details(imdb_id: str):
    celebrity: Celebrity = await imdb.get_celebrity_details(imdb_id=imdb_id, tmdb_api_key=tmdb_api_key)
    return celebrity.to_json()


@app.get("/celebrity/deaths/this_week")
async def celebrity_deaths_this_week() -> Dict:
    start_of_week_date = start_of_this_week()
    end_of_week_date = end_of_this_week()
    deaths: List[CelebrityBrief] = await imdb.get_celebrity_deaths(start_date=start_of_week_date,
                                                                   end_date=end_of_week_date)

    return {"message": f"Hello Deaths"}


@app.get("/celebrity/deaths/this_month")
async def celebrity_deaths_this_month() -> Dict:
    start_of_month_date = start_of_this_month()
    end_of_month_date = end_of_this_month()
    deaths: List[CelebrityBrief] = await imdb.get_celebrity_deaths(start_date=start_of_month_date,
                                                                   end_date=end_of_month_date)

    return {"message": f"Hello Deaths 2"}


@app.get("/celebrity/deaths/last_week")
async def celebrity_deaths_last_week() -> Dict:
    start_of_week_date = start_of_week_offset(offset=-1)
    end_of_week_date = end_of_week_offset(offset=-1)
    deaths: List[CelebrityBrief] = await imdb.get_celebrity_deaths(start_date=start_of_week_date,
                                                                   end_date=end_of_week_date)

    return {"message": f"Hello Deaths 3"}

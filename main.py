from typing import Dict

from fastapi import FastAPI

from imdb.celebrity import Celebrity
from utils import *
from imdb.imdb_connector import *

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "The princess is in another castle!"}


@app.get("/celebrity/details/{imdb_id}")
async def celebrity_details(imdb_id: str):
    celebrity: Celebrity = await get_celebrity_details(imdb_id=imdb_id)
    return celebrity.to_json()


@app.get("/celebrity/deaths/this_week")
async def celebrity_deaths_this_week() -> Dict:
    start_of_week_date = start_of_this_week()
    end_of_week_date = end_of_this_week()
    deaths: List[CelebrityBrief] = await get_celebrity_deaths(start_date=start_of_week_date, end_date=end_of_week_date)

    return {"message": f"Hello Deaths"}


@app.get("/celebrity/deaths/this_month")
async def celebrity_deaths_this_month() -> Dict:
    start_of_month_date = start_of_this_month()
    end_of_month_date = end_of_this_month()
    deaths: List[CelebrityBrief] = await get_celebrity_deaths(start_date=start_of_month_date,
                                                              end_date=end_of_month_date)

    return {"message": f"Hello Deaths 2"}


@app.get("/celebrity/deaths/last_week")
async def celebrity_deaths_last_week() -> Dict:
    start_of_week_date = start_of_week_offset(offset=-1)
    end_of_week_date = end_of_week_offset(offset=-1)
    deaths: List[CelebrityBrief] = await get_celebrity_deaths(start_date=start_of_week_date, end_date=end_of_week_date)

    return {"message": f"Hello Deaths 3"}

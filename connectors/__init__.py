from objectrest import get_json


def tmdb_person_from_imdb_id(imdb_id: str, tmdb_api_key: str) -> dict:
    """Get the TMDB Person entry from the IMDB ID"""

    url = f"https://api.themoviedb.org/3/find/{imdb_id}?api_key={tmdb_api_key}&external_source=imdb_id"
    data = get_json(url)
    return data.get("person_results", [{}])[0]


def tmdb_person_id_from_imdb_id(imdb_id: str, tmdb_api_key: str) -> str:
    """Get the TMDB Person ID from the IMDB ID"""

    person = tmdb_person_from_imdb_id(imdb_id=imdb_id, tmdb_api_key=tmdb_api_key)
    return person.get("id", None)


def imdb_id_from_tmdb_id(tmdb_id: str, tmdb_api_key: str) -> str:
    """Get the IMDB ID from the TMDB ID"""

    url = f"https://api.themoviedb.org/3/person/{tmdb_id}/external_ids?api_key={tmdb_api_key}"
    data = get_json(url)
    return data.get("imdb_id", None)

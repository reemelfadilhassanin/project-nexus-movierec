import os
import requests
from django.core.cache import cache

TMDB_API_KEY = os.getenv("TMDB_API_KEY")
BASE_URL = "https://api.themoviedb.org/3"

def fetch_trending(media_type="movie", time_window="week"):
    cache_key = f"tmdb_trending_{media_type}_{time_window}"
    cached_data = cache.get(cache_key)
    if cached_data:
        return cached_data

    url = f"{BASE_URL}/trending/{media_type}/{time_window}"
    params = {"api_key": TMDB_API_KEY}
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()
    cache.set(cache_key, data, timeout=60*15)  # 15 minutes caching
    return data

def fetch_recommendations(movie_id):
    cache_key = f"tmdb_recommendations_{movie_id}"
    cached_data = cache.get(cache_key)
    if cached_data:
        return cached_data

    url = f"{BASE_URL}/movie/{movie_id}/recommendations"
    params = {"api_key": TMDB_API_KEY}
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()
    cache.set(cache_key, data, timeout=60*15)
    return data

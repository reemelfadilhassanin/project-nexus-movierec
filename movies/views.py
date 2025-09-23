# movies/views.py
import requests
from django.conf import settings
from django.core.cache import cache
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

TMDB_API_KEY = settings.TMDB_API_KEY
CACHE_TTL = getattr(settings, "TMDB_CACHE_TTL", {"trending": 3600, "recommendations": 1800})

def _fetch_tmdb(url):
    resp = requests.get(url, timeout=5)
    resp.raise_for_status()
    return resp.json()

class TrendingMoviesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        cache_key = "movies:trending"
        data = cache.get(cache_key)
        if data is not None:
            return Response(data, headers={"X-Cache": "HIT"})

        try:
            url = f"https://api.themoviedb.org/3/trending/movie/week?api_key={TMDB_API_KEY}"
            raw = _fetch_tmdb(url)
            data = [
                {
                    "id": m["id"],
                    "title": m.get("title"),
                    "poster_path": m.get("poster_path"),
                    "release_date": m.get("release_date"),
                    "vote_average": m.get("vote_average"),
                }
                for m in raw.get("results", [])
            ]
            cache.set(cache_key, data, timeout=CACHE_TTL["trending"])
            return Response(data, headers={"X-Cache": "MISS"})
        except requests.RequestException as e:
            # fallback: return cached stale data if present, otherwise 503
            stale = cache.get(cache_key)
            if stale:
                return Response(stale, headers={"X-Cache": "STALE", "Warning": str(e)})
            return Response({"detail": "Failed to fetch trending movies"}, status=status.HTTP_503_SERVICE_UNAVAILABLE)

class MovieRecommendationsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, movie_id):
        cache_key = f"movies:recommendations:{movie_id}"
        data = cache.get(cache_key)
        if data is not None:
            return Response(data, headers={"X-Cache": "HIT"})

        try:
            url = f"https://api.themoviedb.org/3/movie/{movie_id}/recommendations?api_key={TMDB_API_KEY}"
            raw = _fetch_tmdb(url)
            data = [
                {
                    "id": m["id"],
                    "title": m.get("title"),
                    "poster_path": m.get("poster_path"),
                    "release_date": m.get("release_date"),
                    "vote_average": m.get("vote_average"),
                }
                for m in raw.get("results", [])
            ]
            cache.set(cache_key, data, timeout=CACHE_TTL["recommendations"])
            return Response(data, headers={"X-Cache": "MISS"})
        except requests.RequestException as e:
            stale = cache.get(cache_key)
            if stale:
                return Response(stale, headers={"X-Cache": "STALE", "Warning": str(e)})
            return Response({"detail": "Failed to fetch recommendations"}, status=status.HTTP_503_SERVICE_UNAVAILABLE)

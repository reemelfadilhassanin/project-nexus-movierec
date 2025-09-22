import requests
from django.core.management.base import BaseCommand
from django.conf import settings
from movies.models import Movie

class Command(BaseCommand):
    help = "Fetch popular movies from TMDb and save to database"

    def handle(self, *args, **kwargs):
        api_key = settings.TMDB_API_KEY
        url = f"https://api.themoviedb.org/3/movie/popular?api_key={api_key}&language=en-US&page=1"

        response = requests.get(url)
        if response.status_code != 200:
            self.stderr.write(self.style.ERROR("Failed to fetch movies from TMDb"))
            return

        data = response.json()
        for item in data.get("results", []):
            movie, created = Movie.objects.get_or_create(
                tmdb_id=item["id"],   # تأكدي إن عندك field اسمه tmdb_id في model Movie
                defaults={
                    "title": item["title"],
                    "overview": item.get("overview", ""),
                    "release_date": item.get("release_date", None),
                    "poster_path": item.get("poster_path", ""),
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Added movie: {movie.title}"))
            else:
                self.stdout.write(f"Movie already exists: {movie.title}")

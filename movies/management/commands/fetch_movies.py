import requests
from django.core.management.base import BaseCommand
from django.conf import settings
from movies.models import Movie

class Command(BaseCommand):
    help = "Fetch popular, top-rated, and upcoming movies from TMDb and save to database"

    def handle(self, *args, **kwargs):
        api_key = settings.TMDB_API_KEY
        categories = ["popular", "top_rated", "upcoming"]
        total_added = 0

        for category in categories:
            page = 1
            self.stdout.write(self.style.NOTICE(f"Fetching '{category}' movies..."))

            while True:
                url = f"https://api.themoviedb.org/3/movie/{category}?api_key={api_key}&language=en-US&page={page}"
                response = requests.get(url)

                if response.status_code != 200:
                    self.stderr.write(self.style.ERROR(f"Failed to fetch {category} movies, page {page}"))
                    break

                data = response.json()
                results = data.get("results", [])

                if not results:
                    break

                for item in results:
                    movie, created = Movie.objects.get_or_create(
                        tmdb_id=item["id"],
                        defaults={
                            "title": item["title"],
                            "overview": item.get("overview", ""),
                            "release_date": item.get("release_date", None),
                            "poster_path": item.get("poster_path", ""),
                        }
                    )
                    if created:
                        total_added += 1
                        self.stdout.write(self.style.SUCCESS(f"[{category}] Added: {movie.title}"))

                page += 1

        self.stdout.write(self.style.SUCCESS(f"Finished fetching movies. Total new movies added: {total_added}"))

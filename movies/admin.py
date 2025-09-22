from django.contrib import admin
from movies.models import Movie
from users.models import FavoriteMovie

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'tmdb_id', 'release_date')
    search_fields = ("title",)


@admin.register(FavoriteMovie)
class FavoriteMovieAdmin(admin.ModelAdmin):
    list_display = ("id", "movie_title", "user", "created_at")
    search_fields = ("movie__title", "user__username")

    def movie_title(self, obj):
        return obj.movie.title
    movie_title.admin_order_field = "movie__title"
    movie_title.short_description = "Movie Title"

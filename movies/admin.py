from django.contrib import admin
from .models import Movie
from users.models import FavoriteMovie

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'tmdb_id', 'release_date')
    search_fields = ("title",)

@admin.register(FavoriteMovie)
class FavoriteMovieAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "user", "created_at")
    search_fields = ("title", "user__username")

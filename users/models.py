from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class FavoriteMovie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="favorites")
    movie_id = models.IntegerField()  # TMDb movie ID
    title = models.CharField(max_length=255)
    poster_path = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "movie_id")  # عشان ما يتكرر نفس الفيلم للمستخدم

    def __str__(self):
        return f"{self.title} ({self.user.username})"

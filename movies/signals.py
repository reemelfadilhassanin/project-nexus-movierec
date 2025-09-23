
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache
from .models import Movie

@receiver(post_save, sender=Movie)
def movie_saved(sender, instance, **kwargs):
    # invalidate trending and recommendations related to this movie
    cache.delete("movies:trending")
    # if using django-redis you can delete patterns; otherwise delete specific recommendation keys you know
    try:
        # only works with django-redis backend:
        from django_redis import get_redis_connection
        conn = get_redis_connection("default")
        conn.delete_pattern("movies:recommendations:*")
    except Exception:
        pass

@receiver(post_delete, sender=Movie)
def movie_deleted(sender, instance, **kwargs):
    cache.delete("movies:trending")
    try:
        from django_redis import get_redis_connection
        conn = get_redis_connection("default")
        conn.delete_pattern("movies:recommendations:*")
    except Exception:
        pass

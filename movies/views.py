from rest_framework import generics
from .serializers import UserRegistrationSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
import requests
from django.conf import settings
from django.core.cache import cache
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

TMDB_API_KEY = settings.TMDB_API_KEY
# Registration endpoint
class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer

# Optional: customize token response
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['username'] = user.username
        return token

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
class TrendingMoviesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        cache_key = "trending_movies"
        data = cache.get(cache_key)

        if not data:
            url = f"https://api.themoviedb.org/3/trending/movie/week?api_key={TMDB_API_KEY}"
            response = requests.get(url)
            data = response.json()
            cache.set(cache_key, data, timeout=60*60)  # 1 ساعة

        return Response(data)


class MovieRecommendationsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, movie_id):
        cache_key = f"recommendations_{movie_id}"
        data = cache.get(cache_key)

        if not data:
            url = f"https://api.themoviedb.org/3/movie/{movie_id}/recommendations?api_key={TMDB_API_KEY}"
            response = requests.get(url)
            data = response.json()
            cache.set(cache_key, data, timeout=60*60)

        return Response(data)

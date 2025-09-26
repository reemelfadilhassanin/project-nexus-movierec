from django.urls import path
from .views import (
   
 
    TrendingMoviesView,
    MovieRecommendationsView,   MovieSearchView
    
)
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
     # Movie endpoints
    path('trending/', TrendingMoviesView.as_view(), name='trending_movies'),
    path('recommendations/<int:movie_id>/', MovieRecommendationsView.as_view(), name='movie_recommendations'),
 path('search/', MovieSearchView.as_view(), name='movie_search'),
]

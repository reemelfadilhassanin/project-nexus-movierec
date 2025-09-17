from django.urls import path
from .views import (
    UserRegistrationView,
    CustomTokenObtainPairView,
    TrendingMoviesView,
    MovieRecommendationsView,
)
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # Movie endpoints
    path('trending/', TrendingMoviesView.as_view(), name='trending_movies'),
    path('recommendations/<int:movie_id>/', MovieRecommendationsView.as_view(), name='movie_recommendations'),

]

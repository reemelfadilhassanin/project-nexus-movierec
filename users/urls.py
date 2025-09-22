from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', views.UserRegistrationView.as_view(), name='user-register'),
    path('login/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/', views.UserProfileView.as_view(), name='user-profile'),
    path("favorites/", views.FavoriteMovieListCreateView.as_view(), name="favorites-list-create"),
    path("favorites/<int:pk>/", views.FavoriteMovieDetailView.as_view(), name="favorites-detail"),

]

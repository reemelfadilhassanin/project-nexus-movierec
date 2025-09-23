from django.contrib import admin
from django.urls import path, include, re_path
from django.http import JsonResponse

# --- Swagger imports ---
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

def home(request):
    return JsonResponse({"message": "Welcome to MovieRec API"})

# إعدادات Swagger Schema
schema_view = get_schema_view(
    openapi.Info(
        title="Movie Recommendation API",
        default_version="v1",
        description="API documentation for Project Nexus Movie Recommendation system",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="support@projectnexus.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("", home),
    path("admin/", admin.site.urls),
    path("api/users/", include("users.urls")),
    path("api/movies/", include("movies.urls")),

    # --- Swagger & Redoc ---
    re_path(r"^api/docs(?P<format>\.json|\.yaml)$",
            schema_view.without_ui(cache_timeout=0), name="schema-json"),
    path("api/docs/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("api/redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]

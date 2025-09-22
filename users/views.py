from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import FavoriteMovie
from .serializers import FavoriteMovieSerializer, UserRegistrationSerializer


# -----------------------
# تسجيل مستخدم جديد
# -----------------------
class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer


# -----------------------
# تعديل التوكن لتضمين اسم المستخدم
# -----------------------
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["username"] = user.username
        return token


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


# -----------------------
# عرض بيانات المستخدم الحالي
# -----------------------
class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            "username": user.username,
            "email": user.email,
        })


# -----------------------
# قائمة المفضلات (إضافة + عرض)
# -----------------------
class FavoriteMovieListCreateView(generics.ListCreateAPIView):
    serializer_class = FavoriteMovieSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return FavoriteMovie.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# -----------------------
# تفاصيل فيلم مفضل (عرض/تعديل/حذف)
# -----------------------
class FavoriteMovieDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FavoriteMovieSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return FavoriteMovie.objects.filter(user=self.request.user)
class FavoriteMovieCreateView(generics.CreateAPIView):
    serializer_class = FavoriteMovieSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

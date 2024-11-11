from rest_framework import generics
from .models import CustomUser
from .serializers import UserRegistrationSerializer
from .permissions import IsManagerOrReadOnly
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer

class UserListView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [IsManagerOrReadOnly]

    def perform_create(self, serializer):
        if self.request.user.role == "Менеджер":
            serializer.save()


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
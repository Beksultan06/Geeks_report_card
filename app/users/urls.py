from django.urls import path
from .views import CustomTokenObtainPairView, UserListView

urlpatterns = [
    path('api/users/', UserListView.as_view(), name='user-list'),
    path('api/login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
]

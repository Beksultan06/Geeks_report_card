from django.shortcuts import render
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers
from django_filters.rest_framework import DjangoFilterBackend

from app.lesson.models import Lesson
from app.lesson.serializers import LessonSerializer
from app.users.permissions import IsManagerOrReadOnly

class LessonAPI(GenericViewSet,
                mixins.CreateModelMixin,
                mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin,):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsManagerOrReadOnly]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

    def perform_create(self, serializer):
        user_id = self.request.data.get('user')
        if user_id:
            # Проверяем, является ли текущий пользователь менеджером
            if self.request.user.is_staff:  # или другое условие для проверки менеджера
                serializer.save(user_id=user_id)
            else:
                raise serializers.ValidationError("Вы не можете создать урок для другого пользователя.")
        else:
            serializer.save(user=self.request.user)

class ListLesson(GenericViewSet, mixins.ListModelMixin):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]  # Доступ для всех пользователей
    queryset = Lesson.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['direction', 'user', 'data', 'audience']  # Поля для фильтрации
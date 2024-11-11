from django.shortcuts import render
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers
from django_filters.rest_framework import DjangoFilterBackend

from app.lesson.models import Lesson
from app.lesson.serializers import LessonSerializer
from app.users.models import CustomUser
from app.users.permissions import IsManagerOrReadOnly

class LessonAPI(GenericViewSet,
                mixins.CreateModelMixin,
                mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    # permission_classes = [IsManagerOrReadOnly]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

    def perform_create(self, serializer):
        user_id = self.request.data.get('user')
        
        # Если указан user_id и текущий пользователь является менеджером
        if user_id and self.request.user.is_staff:
            try:
                # Убеждаемся, что пользователь с указанным user_id существует
                user = CustomUser.objects.get(id=user_id)
                serializer.save(user=user)
            except CustomUser.DoesNotExist:
                raise serializers.ValidationError("Пользователь с таким ID не найден.")
        else:
            # Если user_id не указан или пользователь не является менеджером, используем текущего пользователя
            serializer.save(user=self.request.user)

class ListLesson(GenericViewSet, mixins.ListModelMixin):
    serializer_class = LessonSerializer
    # permission_classes = [IsAuthenticated]
    queryset = Lesson.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['direction', 'user', 'data', 'audience']
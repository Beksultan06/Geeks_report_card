from django.urls import path
from rest_framework.routers import DefaultRouter

from app.lesson.views import LessonAPI, ListLesson

router = DefaultRouter()
router.register("api-lesson", LessonAPI, basename='api-lesson')
router.register("api-lesson-list", ListLesson, basename='api-lesson-list')

urlpatterns = [

]

urlpatterns += router.urls
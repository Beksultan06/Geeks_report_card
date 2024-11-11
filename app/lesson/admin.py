from django.contrib import admin
from app.lesson.models import Lesson
# Register your models here.
@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("id", 'direction', 'type_lesson', 'user', 'audience')
    list_filter = ("id", 'direction', 'type_lesson', 'user', 'audience')
    search_fields = ("id", 'direction', 'type_lesson', 'user', 'audience')
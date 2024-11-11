from django.contrib import admin
from app.lesson.models import Lesson, Triallesson
# Register your models here.
@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("id", 'direction', 'type_lesson', 'user', 'audience')
    list_filter = ("id", 'direction', 'type_lesson', 'user', 'audience')
    search_fields = ("id", 'direction', 'type_lesson', 'user', 'audience')


@admin.register(Triallesson)
class TriallessonAdmin(admin.ModelAdmin):
    list_display = ("teacher", "direction", "invited", "its_arrived", "total", "lessons_last_week")
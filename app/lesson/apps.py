from django.apps import AppConfig


class LessonConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app.lesson'
    verbose_name='Уроки'
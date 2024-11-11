from django.db import models
from app.users.models import CustomUser
from app.users.constant import DIRECTION, AUDIENCE
# Create your models here.
class Lesson(models.Model):
    direction = models.CharField(
        max_length=155,
        verbose_name='Направление',
        choices=DIRECTION
    )
    type_lesson = models.CharField(
        max_length=155,
        verbose_name='Тип урока'
    )
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )
    data = models.CharField(
        max_length=50,
        verbose_name='Начала урока'
    )
    audience = models.CharField(
        max_length=155,
        verbose_name='Aудитория',
        choices=AUDIENCE
    )

    def __str__(self):
        return self.type_lesson

    class Meta:
        verbose_name_plural = "Уроки"
from django.contrib.auth.models import AbstractUser
from django.db import models
from app.users.constant import ROLE, DIRECTION, MONTH

class CustomUser(AbstractUser):
    role = models.CharField(
        choices=ROLE,
        verbose_name='Роль пользователя',
        max_length=155,
    )
    direction = models.CharField(
        max_length=155,
        verbose_name='Направление',
        choices=DIRECTION,
        blank=True, null=True
    )
    month = models.CharField(
        max_length=50,
        verbose_name='Преподователь для',
        choices=MONTH
    )

    def __str__(self):
        return f"Преподаватель {self.username} для {self.month}."

    class Meta:
        verbose_name_plural = 'Преподователи и Менеджеры'

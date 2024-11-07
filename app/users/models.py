from django.contrib.auth.models import AbstractUser
from django.db import models
from app.users.constant import ROLE

class CustomUser(AbstractUser):
    role = models.CharField(
        choices=ROLE,
        verbose_name='Роль пользователя',
        max_length=155,
    )

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = 'Пользователи'

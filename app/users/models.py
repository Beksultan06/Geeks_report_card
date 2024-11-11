from django.contrib.auth.models import AbstractUser
from django.db import models
from app.users.constant import ROLE, DIRECTION

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

    def __str__(self):
        return self.username or self.role

    class Meta:
        verbose_name_plural = 'Пользователи'

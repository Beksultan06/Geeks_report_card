from django.db.models import Sum
from django.utils import timezone
from datetime import timedelta
from django.db import models
from app.users.models import CustomUser
from app.users.constant import DIRECTION, AUDIENCE

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
        verbose_name='Преподаватель'
    )
    data = models.CharField(
        max_length=155,
        verbose_name='Начало урока'
    )
    audience = models.CharField(
        max_length=155,
        verbose_name='Аудитория',
        choices=AUDIENCE
    )

    def __str__(self):
        return self.type_lesson

    class Meta:
        verbose_name_plural = "Уроки"


class Triallesson(models.Model):
    teacher = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        verbose_name='Преподаватель'
    )
    direction = models.CharField(
        max_length=155,
        verbose_name='Направление',
        choices=DIRECTION
    )
    invited = models.CharField(
        max_length=155,
        verbose_name='Приглашено'
    )
    its_arrived = models.IntegerField(
        verbose_name='Пришло'
    )
    total = models.IntegerField(
        verbose_name='Общий пришло за последние 7 дней',
        blank=True, null=True
    )
    lessons_last_week = models.IntegerField(
        verbose_name='Уроков за последние 7 дней',
        blank=True, null=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )

    def save(self, *args, **kwargs):
        last_week = timezone.now() - timedelta(days=7)
        total_for_direction = Triallesson.objects.filter(
            direction=self.direction,
            created_at__gte=last_week
        ).aggregate(Sum('its_arrived'))['its_arrived__sum'] or 0
        self.total = total_for_direction

        lessons_count = Triallesson.objects.filter(
            teacher=self.teacher,
            created_at__gte=last_week
        ).count()
        self.lessons_last_week = lessons_count

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Приглашено {self.invited}, пришло из них {self.its_arrived}"

    class Meta:
        verbose_name_plural = 'Недельный отчёт пробных уроков'
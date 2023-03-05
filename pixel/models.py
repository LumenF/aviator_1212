from django.db import models
from django.db.models import Count


class CountModel(models.Model):
    class Meta:
        verbose_name = 'Нажатие'
        verbose_name_plural = 'Нажатие'

    count = models.DateTimeField(
        verbose_name='Нажатие',
        auto_now_add=True
    )

    team = models.CharField(
        verbose_name='Тема',
        max_length=255,
    )

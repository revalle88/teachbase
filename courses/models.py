from django.db import models

import datetime


class Course(models.Model):
    teachbase_id = models.IntegerField(unique=True, verbose_name='id в teachbase')
    name = models.CharField(max_length=200, verbose_name='наименование')
    description = models.TextField(blank=True, default='', verbose_name="описание")
    duration = models.IntegerField(blank=True, null=True, default=None, verbose_name='продолжительность (сек.)')
    # duration = models.DurationField(default=datetime.timedelta(minutes=60), verbose_name='продолжительность (мин.)')
    bg_url = models.URLField(
        blank=True,
        null=True,
        default="",
        verbose_name="bg_url",
    )
    video_url = models.URLField(
        blank=True,
        null=True,
        default="",
        verbose_name="URL video",
    )

    class Meta:
        verbose_name = 'Курс Teachbase'
        verbose_name_plural = 'Курсы Teachbase'

    def __str__(self):
        return f'{self.name}'

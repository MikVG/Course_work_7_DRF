from django.conf import settings
from django.db import models


class Habit(models.Model):

    ACTION_CHOICES = [
        ('walk', 'гулять'),
        ('drink', 'пить воду'),
        ('workout', 'заниматься спортом'),
        ('learn', 'изучать новое'),
    ]

    PERIOD_CHOICES = [
        ('two_hours', 'каждые 2 часа'),
        ('dayly', 'ежедневно'),
        ('weekly', 'еженедельно'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True,
                              verbose_name='создатель привычки')
    place = models.CharField(max_length=100, verbose_name='место')
    time = models.DateTimeField(verbose_name='время выполнения привычки')
    action = models.CharField(max_length=100, choices=ACTION_CHOICES, verbose_name='действие')
    good_habit = models.BooleanField(default=False, verbose_name='признак приятной привычки')
    related_habit = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True,
                                      verbose_name='связанная привычка')
    period = models.CharField(max_length=30, choices=PERIOD_CHOICES, default='weekly', verbose_name='периодичность выполнения')
    award = models.CharField(max_length=150, verbose_name='вознаграждение', null=True, blank=True)
    lead_time = models.IntegerField(verbose_name='время на выполнение')
    is_public = models.BooleanField(default=False, verbose_name='признак публичности')

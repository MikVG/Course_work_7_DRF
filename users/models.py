from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='почта')
    phone = models.CharField(max_length=35, blank=True, null=True, verbose_name='телефон')
    tg_nick = models.CharField(max_length=50, blank=True, null=True, verbose_name='ник в телеграмclear')
    tg_chat_id = models.CharField(max_length=100, blank=True, null=True, verbose_name='телеграм chat_id')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self):
        return f'{self.email}'

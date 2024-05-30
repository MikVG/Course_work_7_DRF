from datetime import timedelta

from celery import shared_task
from django.utils import timezone

from habits.models import Habit

from habits.services import send_telegram_message

@shared_task
def task_send_reminder():
    """Функция выполняет отправку напоминаний в телеграм и обновляет дату следующего действия"""
    time_now = timezone.now()
    habits = Habit.objects.all()

    for habit in habits:
        chat_id = habit.user.tg_chat_id
        if habit.time >= time_now:
            message = f'Вам пора {habit.action} в {habit.place}'
            send_telegram_message(chat_id, message)

        if habit.period == 'daily':
            habit.time = time_now + timedelta(days=1)
        elif habit.period == 'two_days':
            habit.time = time_now + timedelta(days=2)
        else:
            habit.time = time_now + timedelta(days=7)
        habit.save()

import requests
from config import settings


def send_telegram_message(chat_id, message):
    """сервисная функция для отправки сообщения в телеграм"""
    params = {
        'text': message,
        'chat_id': chat_id,
    }
    requests.post(f'{settings.TELEGRAM_URL}{settings.TELEGRAM_TOKEN}/sendMessage', params=params)

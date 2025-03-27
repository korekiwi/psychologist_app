import asyncio
from django.db.models.signals import post_save
from django.dispatch import receiver

from core.models import Question, Appointment
from core.telegram_bot import send_telegram_message
from psychologist.settings import TELEGRAM_BOT_TOKEN, PERSONAL_CHAT_ID


@receiver(post_save, sender=Appointment)
def send_telegram_notification(sender, instance, created, **kwargs):
    if created:
        message = f"""
-------------------------------------------------------------
*Новая запись на прием*

*Проблема:* {instance.title}
*Имя:* {instance.adult_name}
*Имя ребенка:* {instance.child_name}
*Возраст ребенка:* {instance.child_age}
*Телефон:* {instance.phone}
*Email:* {instance.email or 'не указан'}
*Телефон:* {instance.phone or 'не указан'}
*Описание проблемы:* {instance.problem}
-------------------------------------------------------------
"""
        asyncio.run(send_telegram_message(TELEGRAM_BOT_TOKEN, PERSONAL_CHAT_ID, message))


@receiver(post_save, sender=Question)
def send_telegram_notification(sender, instance, created, **kwargs):
    if created:
        message = f"""
-------------------------------------------------------------
*Был задан вопрос:*

*Проблема:* {instance.title}
*Имя:* {instance.name}
*Телефон:* {instance.phone or 'не указан'}
*Email:* {instance.email or 'не указан'}
*Телефон:* {instance.phone or 'не указан'}
*Описание проблемы:* {instance.question}
-------------------------------------------------------------
"""
        asyncio.run(send_telegram_message(TELEGRAM_BOT_TOKEN, PERSONAL_CHAT_ID, message))

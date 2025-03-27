import os
import telegram
import asyncio
import logging

logging.basicConfig(level=logging.DEBUG)


async def send_telegram_message(token, chat_id, message, parse_mode="Markdown"):
    try:
        bot = telegram.Bot(token=token)
        await bot.send_message(chat_id=chat_id, text=message, parse_mode=parse_mode)
        logging.info(f'Сообщение "{message}" отправлено в чат {chat_id}')
    except Exception as e:
        logging.error(f"Ошибка отправки сообщения в чат {chat_id}: {e}")
        raise
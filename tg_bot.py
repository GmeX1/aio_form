from os import getenv
from dotenv import load_dotenv
from aiogram import Bot

import models

load_dotenv()
TOKEN = getenv('BOT_TOKEN')
CHAT_ID = getenv('CHAT_ID')

bot = Bot(TOKEN)


async def alert_user(user: models.User):
    await bot.send_message(
        chat_id=CHAT_ID,
        text='\n'.join([
            "New user registered! Here's some info:",
            f'Name: {user.name}',
            f'Telegram: {user.tg}',
            f'Specialty: {user.specialty}'
        ]))

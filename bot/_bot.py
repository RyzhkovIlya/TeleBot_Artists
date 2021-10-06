import os
import logging
import time

from dotenv import load_dotenv
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from api.main import recommender
from api.static import START, INFO

# Логирование
logging.basicConfig(filename='log.log',
                    level=logging.INFO)

# Загрузка токена через env
load_dotenv()
TOKEN = os.getenv('TOKEN_TELEGRAM')

# Инициализация бота
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.full_name
    logging.info(f'{user_id} запустил бота в {time.asctime()}')
    await message.reply(START % user_name, parse_mode='Markdown')


@dp.message_handler(commands=['info'])
async def process_help_command(message: types.Message):
    await message.reply(INFO)


@dp.message_handler()
async def echo_message(message: types.Message):
    txt = message.text
    user_id = message.from_user.id
    user_name = message.from_user.full_name
    if message.content_type != 'text' :
        await bot.send_message(user_id, 'Пришлите текст - одно слово, другие типы данных не поддерживаются')
    else:
        logging.info(f'Нам написал {user_name}, его id = {user_id}')
        await bot.send_message(user_id, recommender(txt))

if __name__ == '__main__':
    executor.start_polling(dp)
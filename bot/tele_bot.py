import os
import logging
import time
import pandas as pd
from dotenv import load_dotenv
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from api.main import recommender
from api.static import START, INFO
from api.checkers.name_checker import name_checker
from api.checkers.input_checker import input_checker
from api.core.recommendation import recommendation
from api.static import STICKER, NOT_FIND

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

        name = input_checker(txt)
        name = name_checker(name)

        df = pd.read_csv('bot/api/database/artist_names.csv', sep='\t')

        if name in df['authors'].to_list():
            recommend = recommendation(name)
            await bot.send_message(user_id, recommend)
        else:
            await bot.send_sticker(user_id, STICKER)
            if recommender(name) != 'False':
                await bot.send_message(user_id, recommender(name))
            else:
                await bot.send_message(user_id, NOT_FIND)

if __name__ == '__main__':
    executor.start_polling(dp)


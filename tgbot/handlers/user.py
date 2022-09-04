from aiogram import Dispatcher
from aiogram.types import Message

from tgbot.keyboards.inline import start_bot_keyboard
from tgbot.services.db import Database


async def user_start(message: Message):
    db = Database('database.db')
    if db.user_exists(message.from_user.id):
        await message.answer('Ты уже проходил исследование)')
    else:
        await message.answer("""Привет!

Сегодня с тобой Гуля, Никита, Яна и Тимур :)
Мы очень рады видеть тебя на нашем обучающем исследовании “В поисках углеродного следа”. Давай вместе искать углеродный след

Жми «Начать» и погнали!""", parse_mode='HTML', reply_markup=start_bot_keyboard)

    # await message.answer_photo(photo, caption='желаемый текст')

    # await  message.answer('Привет! выбери язык/Hi! choose a language', parse_mode='HTML')
    # await message.reply("Hello, user!")


def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"], state="*")

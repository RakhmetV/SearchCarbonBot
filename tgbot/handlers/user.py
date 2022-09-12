from aiogram import Dispatcher
from aiogram.types import Message

from tgbot.keyboards.inline import start_bot_keyboard
from tgbot.services.db import Database

db = Database('database.db')


async def user_start(message: Message):
    if db.user_exists(message.from_user.id):
        await message.answer('Ты уже проходил исследование)')
    else:
        await message.answer('Привет!\n\n'
                             'Сегодня с тобой команда Всероссийского образовательного проекта “Образ. будущего” ✨\n\n'
                             'Мы очень рады видеть тебя на нашем обучающем исследовании “В поисках углеродного следа”'
                             'Давай вместе искать углеродный след🕵️🕵️‍♀️', parse_mode='HTML',
                             reply_markup=start_bot_keyboard)


async def user_start(message: Message):
    db.del_user(message.from_user.id)
    await message.answer('Ваши данные были удалены из БД')


def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"], state="*")
    dp.register_message_handler(user_start, commands=["del_user"], state="*")

from aiogram import Dispatcher
from aiogram.types import Message

from tgbot.keyboards.inline import language_keyboard


async def admin_start(message: Message):
    await  message.answer('Привет! выбери язык/Hi! choose a language', parse_mode='HTML', reply_markup=language_keyboard)
    #await  message.answer('Привет! выбери язык/Hi! choose a language', parse_mode='HTML')
    #await message.reply("Hello, admin!")


def register_admin(dp: Dispatcher):
    dp.register_message_handler(admin_start, commands=["start"], state="*", is_admin=True)
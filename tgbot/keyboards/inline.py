from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

language_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Русский', callback_data='lang:rus:1')
        ],
        [
            InlineKeyboardButton(text='English', callback_data='lang:eng:1')
        ]
    ],
    row_width=1
)

personal_account_keyboard_rus = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Войти в ЛК', url='https://ams.rusoil.net/pcs/aut')
        ],
    ],
    row_width=1
)
personal_account_keyboard_eng = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Sign in', url='https://ams.rusoil.net/pcs/aut')
        ],
    ],
    row_width=1
)

use_keyboard_rus = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Калькулятор ЕГЭ', url='http://www.pk.rusoil.net/egechoice')
        ],
    ],
    row_width=1
)
use_keyboard_eng = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='USE Calculator', url='http://www.pk.rusoil.net/egechoice')
        ],
    ],
    row_width=1
)
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start_bot_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Начать', callback_data='start')
        ]
    ],
    row_width=1
)

likeTheSet = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Вау', callback_data='likeSet')
        ],
        [
            InlineKeyboardButton(text='Прикольно', callback_data='likeSet')
        ],
        [
            InlineKeyboardButton(text='Красиво', callback_data='likeSet')
        ],
        [
            InlineKeyboardButton(text='Нормально', callback_data='likeSet')
        ]
    ],
    row_width=1
)

researchesStart = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Давай', callback_data='researchesStart')
        ],
        [
            InlineKeyboardButton(text='Да', callback_data='researchesStart')
        ],
        [
            InlineKeyboardButton(text='Жду!', callback_data='researchesStart')
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


from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

district_rt = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Бавлинский район', callback_data='district:Bavlinsk')
        ],
        [
            InlineKeyboardButton(text='Азнакаевский район', callback_data='district:Aznakaevo')
        ],
        [
            InlineKeyboardButton(text='Лениногорский район', callback_data='district:Lenigorod')
        ],
        [
            InlineKeyboardButton(text='Бугульминский район', callback_data='district:Bugulma')
        ],
        [
            InlineKeyboardButton(text='Нижнекамский район', callback_data='district:Nijnekamsk')
        ],
        [
            InlineKeyboardButton(text='Заинский район', callback_data='district:Zainsk')
        ],
        [
            InlineKeyboardButton(text='Альметьевский район', callback_data='district:Almetevsk')
        ]
    ],
    row_width=1
)
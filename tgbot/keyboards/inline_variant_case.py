from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

inline_variant_case_one = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Давайте уже начнем', callback_data='inlineVarCaseOne')
        ],
        [
            InlineKeyboardButton(text='Да', callback_data='inlineVarCaseOne')
        ]
    ],
    row_width=1
)
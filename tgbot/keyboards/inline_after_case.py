from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

inline_after_case_one = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Удостоверение получено', callback_data='AfterCaseOne')
        ]
    ],
    row_width=1
)

inline_after_case_two = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='До новых встреч!', callback_data='AfterCaseTwo')
        ]
    ],
    row_width=1
)
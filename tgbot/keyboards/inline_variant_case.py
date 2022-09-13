from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

inline_variant_case_one = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Давай', callback_data='inlineVarCaseOne')
        ]
    ],
    row_width=1
)

inline_variant_case_two = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Начать', callback_data='inlineVarCaseTwo')
        ]
    ],
    row_width=1
)

inline_variant_case_three = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Начать', callback_data='inlineVarCaseThree')
        ]
    ],
    row_width=1
)

inline_variant_case_four = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Да', callback_data='inlineVarCaseFour')
        ]
    ],
    row_width=1
)

inline_variant_case_five = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Готов', callback_data='inlineVarCaseFive')
        ]
    ],
    row_width=1
)

inline_variant_case_six = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='😍', callback_data='inlineVarCaseSix')
        ],
        [
            InlineKeyboardButton(text='🙂', callback_data='inlineVarCaseSix')
        ]
    ],
    row_width=1
)
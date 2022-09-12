from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

inline_case_pass_one = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Да', callback_data='CasePasswordOne')
        ],
        [
            InlineKeyboardButton(text='Еще жду', callback_data='CasePasswordOne')
        ]
    ],
    row_width=1
)

inline_case_pass_two = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Да, нашел👌', callback_data='CasePasswordTwo:yes')
        ],
        [
            InlineKeyboardButton(text='Еще в поиске👀', callback_data='CasePasswordTwo')
        ],
        [
            InlineKeyboardButton(text='Надо сверить формулу с организатором', callback_data='CasePasswordTwo')
        ]
    ],
    row_width=1
)

inline_case_pass_three = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Получить жизненную ситуацию', callback_data='CasePasswordThree')
        ]
    ],
    row_width=1
)
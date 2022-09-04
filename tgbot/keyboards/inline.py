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
            InlineKeyboardButton(text='Давай', callback_data='resStart')
        ],
        [
            InlineKeyboardButton(text='Да', callback_data='resStart')
        ],
        [
            InlineKeyboardButton(text='Жду!', callback_data='resStart')
        ]
    ],
    row_width=1
)

carbon_footprint = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Да', callback_data='carbonfootprint')
        ],
        [
            InlineKeyboardButton(text='Нет', callback_data='carbonfootprint')
        ]
    ],
    row_width=1
)

carbonFootprintTest = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='CO2', callback_data='carbonTest')
        ],
        [
            InlineKeyboardButton(text='H2O', callback_data='carbonTest')
        ],
        [
            InlineKeyboardButton(text='CH4', callback_data='carbonTest')
        ],
        [
            InlineKeyboardButton(text='N2O', callback_data='carbonTest')
        ],
        [
            InlineKeyboardButton(text='H2S', callback_data='carbonTesAnswer')
        ]
    ],
    row_width=1
)

carbonFootprintAnswer = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Да!', callback_data='carbonAnswer')
        ],
        [
            InlineKeyboardButton(text='100%', callback_data='carbonAnswer')
        ]
    ],
    row_width=1
)

carbonInlineOne = {
    0: InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='😍', callback_data='carbonInOne')
            ],
            [
                InlineKeyboardButton(text='👍', callback_data='carbonInOne')
            ]
        ],
        row_width=1
    )
}

carbonInlineTwo = {
    0: InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='👍', callback_data='carbonInTwo')
            ],
            [
                InlineKeyboardButton(text='👎', callback_data='carbonInTwo')
            ]
        ],
        row_width=1
    )
}
carbonInlineThree = {
    0: InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Да, но буду менять свою привычку!', callback_data='carbonInThree')
            ],
            [
                InlineKeyboardButton(text='Нет, не оставляю', callback_data='carbonInThree')
            ]
        ],
        row_width=1
    )
}
carbonInlineFour = {
    0: InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='👍', callback_data='carbonInFour')
            ],
            [
                InlineKeyboardButton(text='👌', callback_data='carbonInFour')
            ],
            [
                InlineKeyboardButton(text='👎', callback_data='carbonInFour')
            ]
        ],
        row_width=1
    )
}

# --------------------------------------------------------------------------------------------------------------

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

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start_bot_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Начать', callback_data='start')
        ]
    ],
    row_width=1
)

inline_password_one = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Да', callback_data='inlinePassOne')
        ],
        [
            InlineKeyboardButton(text='Еще жду', callback_data='inlinePassOne')
        ]
    ],
    row_width=1
)

inline_password_two = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Да, нашел👌', callback_data='inlinePassTwo')
        ],
        [
            InlineKeyboardButton(text='Еще в поиске👀', callback_data='inlinePassTwo')
        ],
        [
            InlineKeyboardButton(text='Надо сверить формулу с организатором', callback_data='inlinePassTwo')
        ]
    ],
    row_width=1
)


inline_password_three = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Да, нашел👌', callback_data='inlinePassThree')
        ],
        [
            InlineKeyboardButton(text='Был в этой команде изначально🤟🏻', callback_data='inlinePassThree')
        ]
    ],
    row_width=1
)

inline_interaction_one = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Получил', callback_data='inlineInteractOne')
        ],
        [
            InlineKeyboardButton(text='Жду своей очереди', callback_data='inlineInteractOne')
        ]
    ],
    row_width=1
)

inline_interaction_two = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Вау', callback_data='likeSet')
        ],
        [
            InlineKeyboardButton(text='Прикольно', callback_data='likeSet')
        ],
        [
            InlineKeyboardButton(text='Красиво', callback_data='likeSet')
        ]
    ],
    row_width=1
)

inline_interaction_three = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Обожаю делать распаковки', callback_data='inlineInteractThree')
        ],
        [
            InlineKeyboardButton(text='Давай', callback_data='inlineInteractThree')
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
                InlineKeyboardButton(text='🤗', callback_data='carbonInOne')
            ],
            [
                InlineKeyboardButton(text='👍', callback_data='carbonInOne')
            ]
        ],
        row_width=1
    ),
    1: InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='🤗', callback_data='carbonInOne')
            ],
            [
                InlineKeyboardButton(text='👍', callback_data='carbonInOne')
            ]
        ],
        row_width=1
    ),
    2: InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='😍', callback_data='carbonInOne')
            ],
            [
                InlineKeyboardButton(text='🙂', callback_data='carbonInOne')
            ]
        ],
        row_width=1
    ),
    3: InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='😍', callback_data='carbonInOne')
            ],
            [
                InlineKeyboardButton(text='🙂', callback_data='carbonInOne')
            ]
        ],
        row_width=1
    ),
    4: InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='🤗', callback_data='carbonInOne')
            ],
            [
                InlineKeyboardButton(text='👍', callback_data='carbonInOne')
            ]
        ],
        row_width=1
    ),
    5: InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='🤗', callback_data='carbonInOne')
            ],
            [
                InlineKeyboardButton(text='👍', callback_data='carbonInOne')
            ]
        ],
        row_width=1
    ),
    6: InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='😍', callback_data='carbonInOne')
            ],
            [
                InlineKeyboardButton(text='🙂', callback_data='carbonInOne')
            ]
        ],
        row_width=1
    ),
    7: InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='🤗', callback_data='carbonInOne')
            ],
            [
                InlineKeyboardButton(text='👍', callback_data='carbonInOne')
            ]
        ],
        row_width=1
    ),
    8: InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='🤗', callback_data='carbonInOne')
            ],
            [
                InlineKeyboardButton(text='👍', callback_data='carbonInOne')
            ]
        ],
        row_width=1
    ),
    9: InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='🤗', callback_data='carbonInOne')
            ],
            [
                InlineKeyboardButton(text='👍', callback_data='carbonInOne')
            ]
        ],
        row_width=1
    ),
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
    ),
    1: InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='👍', callback_data='carbonInTwo')
            ],
            [
                InlineKeyboardButton(text='👎', callback_data='carbonInTwo')
            ]
        ],
        row_width=1
    ),
    2: InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='👍', callback_data='carbonInTwo')
            ],
            [
                InlineKeyboardButton(text='👎', callback_data='carbonInTwo')
            ]
        ],
        row_width=1
    ),
    3: InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='👍', callback_data='carbonInTwo')
            ],
            [
                InlineKeyboardButton(text='👎', callback_data='carbonInTwo')
            ]
        ],
        row_width=1
    ),
    4: InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Да!', callback_data='carbonInTwo')
            ],
            [
                InlineKeyboardButton(text='Редко', callback_data='carbonInTwo')
            ],
            [
                InlineKeyboardButton(text='Никогда не ездил', callback_data='carbonInTwo')
            ]
        ],
        row_width=1
    ),
    5: InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='👍', callback_data='carbonInTwo')
            ],
            [
                InlineKeyboardButton(text='👎', callback_data='carbonInTwo')
            ]
        ],
        row_width=1
    ),
    6: InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='👍', callback_data='carbonInTwo')
            ],
            [
                InlineKeyboardButton(text='👎', callback_data='carbonInTwo')
            ]
        ],
        row_width=1
    ),
    7: InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='😍', callback_data='carbonInTwo')
            ],
            [
                InlineKeyboardButton(text='🙂', callback_data='carbonInTwo')
            ]
        ],
        row_width=1
    ),
    8: InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='😍', callback_data='carbonInTwo')
            ],
            [
                InlineKeyboardButton(text=' 🙂', callback_data='carbonInTwo')
            ]
        ],
        row_width=1
    ),
    9: InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='👍', callback_data='carbonInTwo')
            ],
            [
                InlineKeyboardButton(text='👎', callback_data='carbonInTwo')
            ]
        ],
        row_width=1
    ),
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
    ),
    1: InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Ого, впервые слышу!', callback_data='carbonInThree')
            ],
            [
                InlineKeyboardButton(text='Да, нам рассказывали в школе!', callback_data='carbonInThree')
            ]
        ],
        row_width=1
    ),
    2: InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Пока еще не участвовал, но впредь буду!', callback_data='carbonInThree')
            ],
            [
                InlineKeyboardButton(text='Да, я стараюсь каждый раз участвовать в таких акциях', callback_data='carbonInThree')
            ]
        ],
        row_width=1
    ),
    3: InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Да, но буду менять свою привычку!', callback_data='carbonInThree')
            ],
            [
                InlineKeyboardButton(text='Нет, не оставляю', callback_data='carbonInThree')
            ]
        ],
        row_width=1
    ),
    4: InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='😍!', callback_data='carbonInThree')
            ],
            [
                InlineKeyboardButton(text='🙂', callback_data='carbonInThree')
            ]
        ],
        row_width=1
    ),
    5: InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Да, каждый год!', callback_data='carbonInThree')
            ],
            [
                InlineKeyboardButton(text='Нет, у меня бабушка сажает огород и я ей помогаю', callback_data='carbonInThree')
            ]
        ],
        row_width=1
    ),
    6: InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Да, стараюсь пластиковые бутылки сдавать в специальные контейнеры!', callback_data='carbonInThree')
            ],
            [
                InlineKeyboardButton(text='Нет, но теперь постараюсь', callback_data='carbonInThree')
            ]
        ],
        row_width=1
    ),
    7: InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Да, но буду менять свою привычку!', callback_data='carbonInThree')
            ],
            [
                InlineKeyboardButton(text='Нет, не оставляю', callback_data='carbonInThree')
            ]
        ],
        row_width=1
    ),
    8: InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Да, но буду менять свою привычку!', callback_data='carbonInThree')
            ],
            [
                InlineKeyboardButton(text='Нет, не оставляю', callback_data='carbonInThree')
            ]
        ],
        row_width=1
    ),
    9: InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Да, конечно, это очень важно ', callback_data='carbonInThree')
            ],
            [
                InlineKeyboardButton(text='Cтараюсь!', callback_data='carbonInThree')
            ]
        ],
        row_width=1
    )
}
carbonInlineFour = {
    0: InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='😉', callback_data='carbonInFour')
            ],
            [
                InlineKeyboardButton(text='🤔', callback_data='carbonInFour')
            ],
            [
                InlineKeyboardButton(text='🙃', callback_data='carbonInFour')
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

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start_bot_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Начать', callback_data='start')
        ]
    ],
    row_width=1
)

# ---------------------------------------------
acquaintance_bot = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Давай', callback_data='acquaintance')
        ]
    ],
    row_width=1
)

description_Nikita = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Привет, Никита', callback_data='helloNikita')
        ]
    ],
    row_width=1
)
description_Gulya = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Привет, Гуля', callback_data='helloGulya')
        ]
    ],
    row_width=1
)

description_Yana = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Привет, Яна', callback_data='helloYana')
        ]
    ],
    row_width=1
)

description_Timyr = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Приятно познакомиться, Тимур', callback_data='helloTimyr')
        ]
    ],
    row_width=1
)

description_add_hero = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Вступить в команду', callback_data='AddUserInComand')
        ]
    ],
    row_width=1
)

description_eco = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Очень, я следую многим эко-привычкам', callback_data='ecoSearch:1')
        ],
        [
            InlineKeyboardButton(text='Да, мне интересно', callback_data='ecoSearch:2')
        ],
        [
            InlineKeyboardButton(text='Еще не доводилось интересоваться', callback_data='ecoSearch:3')
        ],
        [
            InlineKeyboardButton(text='Не интересуюсь', callback_data='ecoSearch:4')
        ]
    ],
    row_width=1
)
# ---------------------------------------------
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

# ---------------------------------------------

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

# ---------------------------------------------

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
            InlineKeyboardButton(text='Да', callback_data='carbonfootprint:Да')
        ],
        [
            InlineKeyboardButton(text='Нет', callback_data='carbonfootprint:Нет')
        ]
    ],
    row_width=1
)
carbon_heard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Да, нам говорили на уроках химии', callback_data='carbonheard')
        ],
        [
            InlineKeyboardButton(text='Еще не слышал', callback_data='carbonheard')
        ]
    ],
    row_width=1
)

carbon_greenhouse_effect = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Позволяет поддерживать комфортную температуру для жизни на Земле',
                                 callback_data='greenhouse:true')
        ],
        [
            InlineKeyboardButton(text='Чтобы не запариваться по пустякам', callback_data='greenhouse:false')
        ],
        [
            InlineKeyboardButton(text='Для выделения пара из чайника', callback_data='greenhouse:false')
        ],
        [
            InlineKeyboardButton(text='Он регулирует приливы и отливы в водоемах Земли',
                                 callback_data='greenhouse:false')
        ]
    ],
    row_width=1
)

carbonFootprintTest = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='CO2', callback_data='carbonTest:CO2')
        ],
        [
            InlineKeyboardButton(text='H2O', callback_data='carbonTest:H2O')
        ],
        [
            InlineKeyboardButton(text='CH4', callback_data='carbonTest:CH4')
        ],
        [
            InlineKeyboardButton(text='N2O', callback_data='carbonTest:N2O')
        ],
        [
            InlineKeyboardButton(text='H2S', callback_data='carbonTest:true')
        ]
    ],
    row_width=1
)
carbon_bulochka = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Производство булочек с корицей', callback_data='bulochka:true')
        ],
        [
            InlineKeyboardButton(text='Покупка булочек с корицей местного производства', callback_data='bulochka:false')
        ]
    ],
    row_width=1
)

carbon_understand = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Да', callback_data='carbonundestand:Да')
        ],
        [
            InlineKeyboardButton(text='Не особо', callback_data='carbonundestand:Не особо')
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
                InlineKeyboardButton(text='да!', callback_data='carbonInTwo')
            ],
            [
                InlineKeyboardButton(text='редко', callback_data='carbonInTwo')
            ],
            [
                InlineKeyboardButton(text='никогда не ездил', callback_data='carbonInTwo')
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
                InlineKeyboardButton(text='👍', callback_data='carbonInTwo')
            ],
            [
                InlineKeyboardButton(text='👎', callback_data='carbonInTwo')
            ]
        ],
        row_width=1
    ),
    8: InlineKeyboardMarkup(
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
                InlineKeyboardButton(text='Да, но буду менять свою привычку!', callback_data='carbonInThree')
            ],
            [
                InlineKeyboardButton(text='Нет, не оставляю', callback_data='carbonInThree')
            ]
        ],
        row_width=1
    ),
    2: InlineKeyboardMarkup(
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
                InlineKeyboardButton(text='Да, но буду менять свою привычку!', callback_data='carbonInThree')
            ],
            [
                InlineKeyboardButton(text='Нет, не оставляю', callback_data='carbonInThree')
            ]
        ],
        row_width=1
    ),
    5: InlineKeyboardMarkup(
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
    6: InlineKeyboardMarkup(
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

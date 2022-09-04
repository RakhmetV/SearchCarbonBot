from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Пройти интерактив'),
        ],
        [
            KeyboardButton(text='Выгрузить данные Exel')
        ]
    ],
    resize_keyboard=True
)

interactive_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Начать'),
        ],
        [
            KeyboardButton(text='Удалить меня из БД')
        ],
        [
            KeyboardButton(text='Назад')
        ]
    ],
    resize_keyboard=True
)

exel_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='За сегодня'),
        ],
        [
            KeyboardButton(text='За все время')
        ],
        [
            KeyboardButton(text='Назад')
        ]
    ],
    resize_keyboard=True
)

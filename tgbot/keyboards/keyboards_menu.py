from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Пройти интерактив'),
        ],
        [
            KeyboardButton(text='Выгрузить данные Exel')
        ],
        [
            KeyboardButton(text='БД')
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

interactive_db = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Установить для всех статус'),
        ],
        [
            KeyboardButton(text='Удалить всех из бд')
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

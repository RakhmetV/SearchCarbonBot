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

inline_after_case_three = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Я тоже рад', callback_data='AfterCaseThree')
        ]
    ],
    row_width=1
)

inline_after_case_four = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Хорошо', callback_data='AfterCaseFour')
        ]
    ],
    row_width=1
)

inline_after_case_video = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Ванные процедуры', callback_data='AfterCaseVideo:4')
        ],
        [
            InlineKeyboardButton(text='Поездка в школу', callback_data='AfterCaseVideo:8')
        ],
        [
            InlineKeyboardButton(text='Школьные уроки', callback_data='AfterCaseVideo:5')
        ],
        [
            InlineKeyboardButton(text='Экскурсия на предприятие', callback_data='AfterCaseVideo:2')
        ],
        [
            InlineKeyboardButton(text='Увлечение, хобби', callback_data='AfterCaseVideo:10')
        ],
        [
            InlineKeyboardButton(text='Питание, продукты', callback_data='AfterCaseVideo:7')
        ],
        [
            InlineKeyboardButton(text='Уборка по дому', callback_data='AfterCaseVideo:6')
        ],
        [
            InlineKeyboardButton(text='Покупка вещей', callback_data='AfterCaseVideo:3')
        ],
        [
            InlineKeyboardButton(text='Здоровый сон', callback_data='AfterCaseVideo:9')
        ],
        [
            InlineKeyboardButton(text='Поход, путешествие', callback_data='AfterCaseVideo:1')
        ]
    ],
    row_width=1
)
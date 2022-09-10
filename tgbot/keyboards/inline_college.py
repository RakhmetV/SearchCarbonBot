from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

district_rt = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Бавлинский район', callback_data='district:Bavlinsk')

        ],
        [
            InlineKeyboardButton(text='Азнакаевский район', callback_data='district:Aznakaevo')
        ],
        [
            InlineKeyboardButton(text='Лениногорский район', callback_data='district:Lenigorod')
        ],
        [
            InlineKeyboardButton(text='Бугульминский район', callback_data='district:Bugulma')
        ],
        [
            InlineKeyboardButton(text='Нижнекамский район', callback_data='district:Nijnekamsk')
        ],
        [
            InlineKeyboardButton(text='Заинский район', callback_data='district:Zainsk')
        ],
        [
            InlineKeyboardButton(text='Альметьевский район', callback_data='district:Almetevsk')
        ]
    ],
    row_width=1
)

college_inline_keyboard = {
    'Bavlinsk': InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Гимназия №4', callback_data='college:Гимназия №4')

            ],
            [
                InlineKeyboardButton(text='СОШ №6', callback_data='college:СОШ №6')
            ],
            [
                InlineKeyboardButton(text='СОШ №2 с УИОП', callback_data='college:СОШ №2 с УИОП')
            ],
            [
                InlineKeyboardButton(text='ООШ №1', callback_data='college:ООШ №1')
            ],
            [
                InlineKeyboardButton(text='МАОУ «СОШ №5»', callback_data='college:МАОУ «СОШ №5»')
            ],
            [
                InlineKeyboardButton(text='СОШ №3', callback_data='college:СОШ №3')
            ],
            [
                InlineKeyboardButton(text='СОШ №7', callback_data='college:СОШ №7')
            ]
        ],
        row_width=1
    ),
    'Aznakaevo': InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Гимназия г. Азнакаево', callback_data='college:Гимназия г. Азнакаево')

            ],
            [
                InlineKeyboardButton(text='СОШ №2', callback_data='college:СОШ №2')
            ],
            [
                InlineKeyboardButton(text='Лицей №4', callback_data='college:Лицей №4')
            ],
            [
                InlineKeyboardButton(text='СОШ№7', callback_data='college:СОШ №7')
            ],
            [
                InlineKeyboardButton(text='СОШ  №5', callback_data='college:СОШ №5')
            ],
            [
                InlineKeyboardButton(text='СОШ №3', callback_data='college:СОШ №3')
            ]
        ],
        row_width=1
    ),
    'Lenigorod': InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='СОШ №8', callback_data='college:СОШ №8')

            ],
            [
                InlineKeyboardButton(text='СОШ №6', callback_data='college:СОШ №6')
            ],
            [
                InlineKeyboardButton(text='СОШ №10', callback_data='college:СОШ №10')
            ],
            [
                InlineKeyboardButton(text='СОШ №2', callback_data='college:СОШ №2')
            ],
            [
                InlineKeyboardButton(text='Гимназия №11»', callback_data='college:Гимназия №11')
            ],
            [
                InlineKeyboardButton(text='Лицей №12', callback_data='college:Лицей №12')
            ]
        ],
        row_width=1
    ),
    'Bugulma': InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='СОШ №1', callback_data='college:СОШ №1'),
                InlineKeyboardButton(text='СОШ №4', callback_data='college:СОШ №4'),
                InlineKeyboardButton(text='СОШ №9', callback_data='college:СОШ №9')

            ],
            [
                InlineKeyboardButton(text='Лицей №2', callback_data='college:Лицей №2'),
                InlineKeyboardButton(text='ООШ №8', callback_data='college:ООШ №8'),
                InlineKeyboardButton(text='ООШ №12', callback_data='college:ООШ №12')
            ],
            [
                InlineKeyboardButton(text='лицей-интернат им. М. Онджеля', callback_data='college:лицей-интернат им. М. Онджеля'),
                InlineKeyboardButton(text='СОШ №3', callback_data='college:СОШ №3')
            ],
            [
                InlineKeyboardButton(text='СОШ №11', callback_data='college:СОШ №11'),
                InlineKeyboardButton(text='СОШ №13', callback_data='college:СОШ №13'),
                InlineKeyboardButton(text='Акбашская ООШ', callback_data='college:Акбашская ООШ'),
            ],
            [
                InlineKeyboardButton(text='Восточная ООШ»', callback_data='college:Восточная ООШ'),
                InlineKeyboardButton(text='З.Рощинская ООШ»', callback_data='college:З.Рощинская ООШ'),
                InlineKeyboardButton(text='Карабашская ООШ №1»', callback_data='college:Карабашская ООШ №1'),
            ],
            [
                InlineKeyboardButton(text='Карабашская СОШ №2', callback_data='college:Карабашская СОШ №2'),
                InlineKeyboardButton(text='Кудашевская ООШ', callback_data='college:Кудашевская ООШ'),
                InlineKeyboardButton(text='М.Бугульминская СОШ', callback_data='college:М.Бугульминская СОШ')
            ],
            [
                InlineKeyboardButton(text='Наратлинская ООШ', callback_data='college:Наратлинская ООШ'),
                InlineKeyboardButton(text='Подгорненская ООШ', callback_data='college:Подгорненская ООШ'),
                InlineKeyboardButton(text='Сокольская ООШ', callback_data='college:Сокольская ООШ')
            ],
            [
                InlineKeyboardButton(text='Тат.Дымская ООШ', callback_data='college:Тат.Дымская ООШ'),
                InlineKeyboardButton(text='СОШ №5', callback_data='college:СОШ №5'),
                InlineKeyboardButton(text='СОШ №6', callback_data='college:СОШ №6')
            ],
            [
                InlineKeyboardButton(text='Татарская гимназия №14', callback_data='college:татарская гимназия №14'),
                InlineKeyboardButton(text='Гимназия №7', callback_data='college:гимназия №7')
            ],
            [
                InlineKeyboardButton(text='ООШ №18', callback_data='college:ООШ №18'),
                InlineKeyboardButton(text='ГБОУ КШИ', callback_data='college:ГБОУ КШИ')
            ]
        ],
        row_width=1
    ),
    'Nijnekamsk': InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Лицей-интернат № 24', callback_data='college:Лицей-интернат № 24'),
                InlineKeyboardButton(text='Школа № 2', callback_data='college:Школа № 2')

            ],
            [
                InlineKeyboardButton(text='СОШ № 28', callback_data='college:СОШ № 28'),
                InlineKeyboardButton(text='СОШ № 26', callback_data='college:СОШ № 26')
            ],
            [
                InlineKeyboardButton(text='СОШ №36', callback_data='college:СОШ №36'),
                InlineKeyboardButton(text='СОШ №29', callback_data='college:СОШ №29')
            ],
            [
                InlineKeyboardButton(text='СОШ №9', callback_data='college:СОШ №9'),
                InlineKeyboardButton(text='СОШ №11', callback_data='college:СОШ №11')
            ],
            [
                InlineKeyboardButton(text='СОШ №12»', callback_data='college:СОШ №12'),
                InlineKeyboardButton(text='СОШ №16»', callback_data='college:СОШ №16')
            ],
            [
                InlineKeyboardButton(text='Лицей №35', callback_data='college:Лицей №35'),
                InlineKeyboardButton(text='Школа №27', callback_data='college:школа №27')
            ],
            [
                InlineKeyboardButton(text='Гимназия №32', callback_data='college:гимназия №32'),
                InlineKeyboardButton(text='СОШ №10', callback_data='college:СОШ №10')
            ],
            [
                InlineKeyboardButton(text='СОШ №33', callback_data='college:СОШ №33'),
                InlineKeyboardButton(text='Лицей №14', callback_data='college:Лицей №14')
            ]
        ],
        row_width=1
    ),
    'Zainsk': InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='ЗСОШ № 2', callback_data='college:ЗСОШ № 2')

            ],
            [
                InlineKeyboardButton(text='ЗСОШ № 3', callback_data='college:ЗСОШ № 3')
            ],
            [
                InlineKeyboardButton(text='ЗСОШ № 7 с УИОП', callback_data='college:ЗСОШ № 7 с УИОП')
            ]
        ],
        row_width=1
    ),
    'Almetevsk': InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='СОШ №25', callback_data='college:СОШ №25'),
                InlineKeyboardButton(text='СОШ №21', callback_data='college:СОШ №21'),
                InlineKeyboardButton(text='СОШ №24', callback_data='college:СОШ №24')

            ],
            [
                InlineKeyboardButton(text='Лицей-интернат №1', callback_data='college:Лицей-интернат №1'),
                InlineKeyboardButton(text='СОШ №3', callback_data='college:СОШ №3')
            ],
            [
                InlineKeyboardButton(text='Гимназия №5', callback_data='college:Гимназия №5'),
                InlineKeyboardButton(text='Гимназия №1', callback_data='college:Гимназия №1')
            ],
            [
                InlineKeyboardButton(text='СОШ №7', callback_data='college:СОШ №7'),
                InlineKeyboardButton(text='СОШ №4', callback_data='college:СОШ №4'),
                InlineKeyboardButton(text='СОШ №10', callback_data='college:СОШ №10')
            ],
            [
                InlineKeyboardButton(text='СОШ №11»', callback_data='college:СОШ №11'),
                InlineKeyboardButton(text='СОШ №12»', callback_data='college:СОШ №12'),
                InlineKeyboardButton(text='СОШ №15»', callback_data='college:СОШ №15')
            ],
            [
                InlineKeyboardButton(text='СОШ №16', callback_data='college:СОШ №16'),
                InlineKeyboardButton(text='СОШ №20', callback_data='college:СОШ №20'),
                InlineKeyboardButton(text='Лицей №2', callback_data='college:Лицей №2')
            ],
            [
                InlineKeyboardButton(text='СОШ №6', callback_data='college:СОШ №6'),
                InlineKeyboardButton(text='СОШ №1', callback_data='college:СОШ №1'),
                InlineKeyboardButton(text='СОШ №17', callback_data='college:СОШ №17')
            ],
            [
                InlineKeyboardButton(text='СОШ №2', callback_data='college:СОШ №2'),
                InlineKeyboardButton(text='СОШ №13', callback_data='college:СОШ №13')
            ],
            [
                InlineKeyboardButton(text='Инженерный лицей', callback_data='college:Инженерный лицей')
            ]
        ],
        row_width=1
    )
}

from aiogram import Dispatcher
from aiogram.types import Message
import pandas as pd
from datetime import datetime
from openpyxl import load_workbook
from tgbot.handlers.message import team_name
from tgbot.keyboards.inline import start_bot_keyboard
from tgbot.keyboards.keyboards_menu import start_menu, interactive_menu, exel_menu
from tgbot.services.db import Database


async def admin_start(message: Message):
    await message.answer(f'Здравствуйте, {message.from_user.first_name}', reply_markup=start_menu)


async def admin_menu(message: Message):
    db = Database('database.db')
    # ---------------------
    if message.text == 'Пройти интерактив':
        await message.answer('Ты уже проходил исследование)', reply_markup=interactive_menu)

    # ---------------------
    elif message.text == 'Выгрузить данные Exel':
        await message.answer('Выберите вариант выгрузки', reply_markup=exel_menu)

    # ---------------------
    elif message.text == 'Начать':
        if db.user_exists(message.from_user.id):
            await message.answer('Ты уже проходил исследование)')
        else:
            await message.answer("""Привет!

Сегодня с тобой Гуля, Никита, Яна и Тимур :)
Мы очень рады видеть тебя на нашем обучающем исследовании “В поисках углеродного следа”. Давай вместе искать углеродный след

Жми «Начать» и погнали!""", parse_mode='HTML', reply_markup=start_bot_keyboard)

    # ---------------------
    elif message.text == 'Удалить меня из БД':
        db.del_user(message.from_user.id)
        await message.answer('Ваши данные были удалены из БД')

    # ---------------------
    elif message.text == 'Назад':
        await message.answer('Основное меню', reply_markup=start_menu)

    # ---------------------
    elif message.text == 'За сегодня':
        nowdate = datetime.now()
        newdate = nowdate.strftime("%d/%m/%Y")  # Не готово еще
        if bool(len(db.get_user_today(newdate))):
            await message.answer('Данные за сегодня')

            users_today = db.get_user_today(newdate)
            name = []
            college = []
            date = []
            variant = []
            answer_one = []
            answer_two = []
            feedback = []
            for user in users_today:
                name.append(user[0])
                college.append(user[1])
                date.append(user[2])
                variant.append(team_name[user[3]])
                answer_one.append(user[4])
                answer_two.append(user[5])
                feedback.append(user[6])

            df = pd.DataFrame({'Имя': name,
                               'Место учебы': college,
                               'Дата': date,
                               'Вариант': variant,
                               'Ответ на первый вопрос': answer_one,
                               'Ответ на второй вопрос': answer_two,
                               'Отзыв': feedback})
            df.to_excel('./database_exel.xlsx', index=False)
            exel_file = open('database_exel.xlsx', 'rb')
            await message.answer_document(exel_file)
            exel_file.close()
        else:
            await message.answer('Сегодня никто не проходил интерактив')

     # ---------------------
    elif message.text == 'За все время':  # Не готово еще
        if bool(len(db.get_user_all())):
            await message.answer('Данные за все время')
            users_all = db.get_user_all()
            name = []
            college = []
            date = []
            variant = []
            answer_one = []
            answer_two = []
            feedback = []
            for user in users_all:
                name.append(user[0])
                college.append(user[1])
                date.append(user[2])
                variant.append(team_name[user[3]])
                answer_one.append(user[4])
                answer_two.append(user[5])
                feedback.append(user[6])

            df = pd.DataFrame({'Имя': name,
                               'Место учебы': college,
                               'Дата': date,
                               'Вариант': variant,
                               'Ответ на первый вопрос': answer_one,
                               'Ответ на второй вопрос': answer_two,
                               'Отзыв': feedback})
            df.to_excel('./database_exel.xlsx', index=False)
            exel_file = open('database_exel.xlsx', 'rb')
            await message.answer_document(exel_file)
            exel_file.close()
        else:
            await message.answer('Никто не проходил интерактив')

    # await message.answer_photo(photo, caption='желаемый текст')


def register_admin(dp: Dispatcher):
    dp.register_message_handler(admin_start, commands=["start"], state="*", is_admin=True)
    dp.register_message_handler(admin_menu, state=None, is_admin=True)

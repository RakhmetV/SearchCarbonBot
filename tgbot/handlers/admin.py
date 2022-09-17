from aiogram import Dispatcher
from aiogram.types import Message, InputFile, ContentTypes
import pandas as pd
from datetime import datetime
from openpyxl import load_workbook
from tgbot.handlers.message import team_name
from tgbot.keyboards.inline import start_bot_keyboard
from tgbot.keyboards.keyboards_menu import start_menu, interactive_menu, exel_menu, interactive_db
from tgbot.services.db import Database

db = Database('database.db')


async def send_video(message: Message):
    print(1)
    await message.answer_video(video='BAACAgIAAxkBAAJS9GMh1Uzs_b45tPyyZC8Zq-KEv2TPAAKfHAACEHURSchjJ3fKot6MKQQ')
    print(2)


async def drop(message: Message):
    db.del_all_users()


async def admin_start(message: Message):
    await message.answer(f'Здравствуйте, {message.from_user.first_name}', reply_markup=start_menu)


async def admin_menu(message: Message):
    # ---------------------
    if message.text == 'Пройти интерактив':
        await message.answer('Интерактив', reply_markup=interactive_menu)

    # ---------------------
    elif message.text == 'Выгрузить данные Exel':
        await message.answer('Выберите вариант выгрузки', reply_markup=exel_menu)

    # ---------------------
    elif message.text == 'Начать':
        if db.user_exists(message.from_user.id):
            await message.answer('Ты уже проходил исследование)')
        else:
            await message.answer('Привет!\n\n'
                                 'Сегодня с тобой команда Всероссийского образовательного проекта “Образ. будущего” ✨\n\n'
                                 'Мы очень рады видеть тебя на нашем обучающем исследовании “В поисках углеродного следа”'
                                 'Давай вместе искать углеродный след🕵️🕵️‍♀️', parse_mode='HTML',
                                 reply_markup=start_bot_keyboard)

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
                if bool(user[3]):
                    variant.append(team_name[user[3]])
                else:
                    variant.append('-1')
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
    elif message.text == 'БД':
        await message.answer('Основное меню', reply_markup=interactive_db)
    elif message.text == 'Установить для всех статус':
        db.set_status_all()
        await message.answer('Для всех установлен статус завершения')
    elif message.text == 'Удалить всех из бд':
        db.del_all_users()
        await message.answer('Все пользователи были удалены')
    # ---------------------
    elif message.text == 'За все время':  # Не готово еще
        if bool(len(db.get_user_all())):
            await message.answer('Данные за все время')
            users_all = db.get_user_all()
            name = []
            district = []
            college = []
            hobby = []
            favorite_subject = []
            interest_ecology = []
            studying_topic_one = []
            studying_topic_two = []
            studying_topic_three = []
            studying_topic_four = []
            date = []
            variant = []
            answer_one = []
            answer_two = []
            sum = []
            feedback = []
            for user in users_all:
                date.append(user[0])
                name.append(user[1])
                district.append(user[2])
                college.append(user[3])
                hobby.append(user[4])
                favorite_subject.append(user[5])
                interest_ecology.append(user[6])
                studying_topic_one.append(user[7])
                studying_topic_two.append(user[8])
                studying_topic_three.append(user[9])
                studying_topic_four.append(user[10])
                if bool(user[11]):
                    variant.append(team_name[user[11]])
                else:
                    variant.append('-1')
                answer_one.append(user[12])
                answer_two.append(user[13])
                feedback.append(user[14])

            df = pd.DataFrame({'Дата': date,
                               'Имя': name,
                               'Район': district,
                               'Место учебы': college,
                               'Увлечения': hobby,
                               'Любимый предмет': favorite_subject,
                               'Интересуется экологией?': interest_ecology,
                               'Слышал об углеродном следе?': studying_topic_one,
                               'Вопрос про лишний газ': studying_topic_two,
                               'Что относится к углеродному следу?': studying_topic_three,
                               'Понял что такое углеродный след?': studying_topic_four,
                               'Вариант': variant,
                               'Ответ на первый вопрос': answer_one,
                               'Ответ на второй вопрос': answer_two,
                               'Отзыв': feedback})
            df.to_excel('./database_exel.xlsx', index=False)

            with open('database_exel.xlsx', 'rb') as exel_file:
                await message.answer_document(exel_file)
                exel_file.close()
        else:
            await message.answer('Никто не проходил интерактив')

    # await message.answer_photo(photo, caption='желаемый текст')


async def video_id(message: Message):
    await message.reply(message.video.file_id)


def register_admin(dp: Dispatcher):
    dp.register_message_handler(admin_start, commands=["start"], state="*", is_admin=True)
    dp.register_message_handler(send_video, commands=["video"], state="*", is_admin=True)
    dp.register_message_handler(drop, commands=["drop_all"], state="*", is_admin=True)
    dp.register_message_handler(admin_menu, state=None, is_admin=True)
    dp.register_message_handler(video_id, content_types=ContentTypes.VIDEO, is_admin=True)

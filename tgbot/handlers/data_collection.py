import asyncio
import random
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from datetime import datetime

from tgbot.handlers.message import team_selection, team_name
from tgbot.keyboards.inline import likeTheSet
from tgbot.services.db import Database
from tgbot.states.test import Data

async def start_bot(call: CallbackQuery):
    await call.answer(cache_time=5)
    await call.message.answer('Для начала давай познакомимся!')
    await asyncio.sleep(1)
    await call.message.answer('Как тебя зовут?')
    await Data.Name.set()


async def answer_name(message: types.Message, state: FSMContext):
    answer = message.text

    # записываем ответ в state
    await state.update_data(name=answer)

    # записываем ответ в state Вариант 2
    # await state.update_data(
    #     {'answear1':answer}
    # )

    # записываем ответ в state Вариант 3
    # async with state.proxy() as data:
    #     data['answer1'] = answer
    # Удобно, если нужно сделать data['answer1']+=1
    # или data['list'].append(1), т.к не нужно сначала доставать из стейта. а потом задавать

    await message.answer(f'Приятно познакомиться, {answer}!')
    await asyncio.sleep(1)
    await message.answer("""Из какого ты учебного заведения? Напиши название учебного заведения
    
Например, Школа №2, Инженерный лицей, Гимназия №39""")
    await Data.next()


async def answer_education(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(college=answer)
    await asyncio.sleep(1)
    await message.answer('На ваших столах вы можете найти листок с паролем')
    await asyncio.sleep(1)
    await message.answer('Введи пароль')
    await Data.next()


async def answer_case_password(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(password=answer)
    db = Database('database.db')
    nowdate = datetime.now()
    newdate = nowdate.strftime("%d/%m/%Y")
    if answer in team_selection:
        data = await state.get_data()  # тут хранится весь словарь состояний
        name = data.get('name')
        college = data.get('college')
        db.add_user(message.from_user.id,
                    name,
                    college,
                    newdate,
                    team_selection[answer]
                    )
        variant = random.randint(0, 9)
        while db.check_variant(newdate, team_selection[answer], variant):
            variant = random.randint(0, 9)
        db.set_variant(message.from_user.id, variant)
        await message.answer(f'Вы в команда под номером {team_selection[answer]}')
        await message.answer(f'Супер, ты получаешь исследование по теме <b>{team_name[variant]}</b>', parse_mode='HTML')

        await state.finish()

        await asyncio.sleep(1)
        await message.answer('Назови тему исследования организатору. Он выдаст тебе набор для исследования')
        await asyncio.sleep(3)
        await message.answer('Как тебе набор?', reply_markup=likeTheSet)
    else:
        await message.answer('Вы ввели неправильный пароль. Введите пароль снова')

    # await Test.next()


def register_data_collection(dp: Dispatcher):
    dp.register_callback_query_handler(start_bot, text_contains='start', state=None)
    dp.register_message_handler(answer_name, state=Data.Name)
    dp.register_message_handler(answer_education, state=Data.EducationalInstitution)
    dp.register_message_handler(answer_case_password, state=Data.PasswordCase)

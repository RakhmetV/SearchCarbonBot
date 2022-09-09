import asyncio
import random
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from datetime import datetime

from tgbot.handlers.message import team_selection, team_name
from tgbot.keyboards.inline import inline_password_one, inline_password_two, inline_password_three, \
    inline_interaction_one, inline_interaction_two
from tgbot.services.db import Database
from tgbot.states.test import Data


async def start_bot(call: CallbackQuery):
    await call.answer(cache_time=5)
    await call.message.answer('Для начала давай познакомимся✌🏻')
    await asyncio.sleep(1)
    await call.message.answer('Как тебя зовут?')
    await Data.Name.set()


async def answer_name(message: types.Message, state: FSMContext):
    data = await state.get_data()  # тут хранится весь словарь состояний
    if not bool(data.get('name')):
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

        await message.answer(f'Приятно познакомиться, {answer}🥰')
        await asyncio.sleep(1)
        await message.answer(
            'Из какого ты учебного заведения?\n'
            '(Напиши название учебного заведения)\n\n'
            'Например, Школа №2, Инженерный лицей, Гимназия №39')
        await Data.next()


async def answer_education(message: types.Message, state: FSMContext):
    data = await state.get_data()  # тут хранится весь словарь состояний
    if not bool(data.get('college')):
        answer = message.text
        if len(answer) > 60:
            await message.answer(f'Количество допустимых символов: 60\nКоличество ваших символов: {len(answer)}')
            await asyncio.sleep(1)
            await message.answer(f'Сократите название')
        else:
            await state.update_data(college=answer)
            await asyncio.sleep(1)

            await message.answer('Перед тем, как начать исследование, мы разделимся на команды')
            await asyncio.sleep(1)

            await message.answer('Попроси у организатора пароль')
            await asyncio.sleep(1)

            await message.answer('Получил?', reply_markup=inline_password_one)
            await asyncio.sleep(1)


async def inlinePasswordOne(call: CallbackQuery, state: FSMContext):
    await call.message.answer('Ты получил название химического вещества⚛')
    await asyncio.sleep(1)

    await call.message.answer('Теперь найди формулу данного вещества, покажи модератору данную формулу и сверься')
    await asyncio.sleep(1)

    await call.message.answer('Нашел формулу данного вещества?', reply_markup=inline_password_two)
    await asyncio.sleep(1)


async def inlinePasswordTwo(call: CallbackQuery, state: FSMContext):
    await call.message.answer('Данная формула вещества будет являться паролем')
    await asyncio.sleep(1)

    await call.message.answer('Введи пароль (Заглавными буквами и английским шрифтом)')
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
                    )  # добавляем нового пользователя

        variant = random.randint(0, 9)
        if db.counting_variant_case(team_selection[answer], newdate)[0][0] > 10:
            await message.answer(f'Количество людей в этой команде превысило 10\nПожалуйста, попробуйте другой пароль')
        else:
            check = False
            while db.check_variant(newdate, team_selection[answer], variant):
                if db.counting_variant_case(team_selection[answer], newdate)[0][0] > 10:
                    check = True
                    break
                else:
                    variant = random.randint(0, 9)

            if check:
                await message.answer(
                    f'Количество людей в этой команде превысило 10\nПожалуйста, попробуйте другой пароль')
            else:
                db.set_variant(message.from_user.id, variant)
                await message.answer(f'Вы в команде под номером {team_selection[answer]} 🙌')
                await asyncio.sleep(1)

                await message.answer(f'Узнай у организатора, в той ли ты команде сидишь сейчас\n\n'
                                     f'Если в той, оставайся на местах. Если ты в другой команде, пересядь')
                await asyncio.sleep(1)

                await message.answer('Нашел свою команду?', parse_mode=inline_password_three)
                await asyncio.sleep(1)

                # await message.answer(f'Супер, ты получаешь исследование по теме <b>{team_name[variant]}</b>',
                #                      parse_mode='HTML')
                # await asyncio.sleep(1)
                #
                # await state.finish()  # очищаем позицию
                # await message.answer('Назови тему исследования организатору. Он выдаст тебе набор для исследования')
                # await asyncio.sleep(3)
                # await message.answer('Как тебе набор?', reply_markup=likeTheSet)
    else:
        await message.answer('Вы ввели неправильный пароль. Введите пароль снова')

    # await Test.next()


async def inlinePasswordThree(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()  # тут хранится весь словарь состояний
    variant = data.get('variant')
    await call.message.answer('Отлично!')
    await asyncio.sleep(1)

    await call.message.answer(f'Сегодня ты будешь проводить исследование по теме <b>{team_name[variant]}</b>',
                              parse_mode='HTML')
    await asyncio.sleep(1)

    await call.message.answer(
        'Назови тему исследования организатору. Он выдаст тебе персональный чемоданчик для исследования')
    await asyncio.sleep(1)

    await call.message.answer('Получил чемоданчик?', reply_markup=inline_interaction_one)
    await asyncio.sleep(1)

    await state.finish()  # очищаем позицию

async def inlineIntecactiveThree(call: CallbackQuery):

    await call.message.answer('Как тебе набор?', reply_markup=inline_interaction_two)


def register_data_collection(dp: Dispatcher):
    dp.register_callback_query_handler(start_bot, text_contains='start', state=None)
    dp.register_message_handler(answer_name, state=Data.Name)
    dp.register_message_handler(answer_education, state=Data.EducationalInstitution)
    dp.register_callback_query_handler(inlinePasswordOne, text_contains='inlinePassOne',
                                       state=Data.EducationalInstitution)
    dp.register_callback_query_handler(inlinePasswordTwo, text_contains='inlinePassTwo',
                                       state=Data.EducationalInstitution)

    dp.register_message_handler(answer_case_password, state=Data.PasswordCase)

    dp.register_callback_query_handler(inlinePasswordThree, text_contains='inlinePassThree',
                                       state=Data.PasswordCase)
    dp.register_callback_query_handler(inlineIntecactiveThree, text_contains='inlineInteractOne',
                                       state=None)

import asyncio
import random
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from datetime import datetime

from tgbot.handlers.message import team_selection, team_name
from tgbot.keyboards.inline import inline_interaction_one
from tgbot.keyboards.inline_password import inline_case_pass_one, inline_case_pass_two, inline_case_pass_three
from tgbot.services.db import Database
from tgbot.states.test import DataPass


async def password_write_one(call: CallbackQuery):
    await call.answer(cache_time=5)
    await call.message.answer(
        'Чтобы получить тему жизненной ситуации введи пароль')
    await asyncio.sleep(4)

    await call.message.answer(
        'Попроси его у организатора')
    await asyncio.sleep(6)

    await call.message.answer(
        'Получил?', reply_markup=inline_case_pass_one)


async def password_write_two(call: CallbackQuery):
    await call.answer(cache_time=5)
    await asyncio.sleep(2)
    await call.message.answer('Ты получил название химического вещества⚛️')
    await asyncio.sleep(5)

    await call.message.answer('Теперь найди формулу данного вещества, '
                                  'покажи модератору данную формулу и сверься')
    await asyncio.sleep(6)

    await call.message.answer('Нашел формулу данного вещества?', reply_markup=inline_case_pass_two)


async def password_write_three(call: CallbackQuery):
    await call.answer(cache_time=5)
    await asyncio.sleep(2)
    await call.message.answer('Данная формула вещества будет являться паролем')
    await asyncio.sleep(5)
    await call.message.answer('Введи пароль (Заглавными буквами и английским шрифтом)')
    await DataPass.CasePassword.set()


async def password_write_four(message: types.Message, state: FSMContext):
    data = await state.get_data()  # тут хранится весь словарь состояний
    if not bool(data.get('password_case')):
        answer = message.text
        if answer in team_selection:
            db = Database('database.db')
            nowdate = datetime.now()
            newdate = nowdate.strftime("%d/%m/%Y")
            variant = random.randint(0, 9)
            db.set_case_number(message.from_user.id, team_selection[answer])
            if db.counting_variant_case(team_selection[answer], newdate)[0][0] > 10:
                await message.answer(f'Количество людей в этой команде превысило 10\n'
                                     f'Пожалуйста, попробуйте другой пароль')
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
                    await state.update_data(password_case=answer)
                    db.set_variant(message.from_user.id, variant)
                    await message.answer(f'Ты ввел правильную формулу вещества!')
                    await asyncio.sleep(5)
                    await message.answer(f'Сейчас ты получишь случайным образом '
                                         f'одну из десяти жизненных ситуаций, на примере '
                                         f'которой будешь рассчитывать способы снижения '
                                         f'углеродного следа', reply_markup=inline_case_pass_three)
                    await state.finish()
        else:
            await message.answer('Вы ввели неправильный пароль. Введите его снова')


async def password_write_five(call: CallbackQuery):
    await call.answer(cache_time=5)
    db = Database('database.db')
    await asyncio.sleep(2)
    await call.message.answer('Несколько мгновений и ты получишь заветную тему')
    await asyncio.sleep(3)

    # await call.message.answer_sticker(sticker='CAACAgIAAxkBAAIJ-mMd94_BTkMZCs6Gf61vffaK-ly0AAJNAAOtZbwU9rZs9GUx5hopBA')
    # await asyncio.sleep(1)

    await call.message.answer('Еще секундочку!')
    await asyncio.sleep(2)

    variant = db.get_variant(call.message.chat.id)[0][0]
    await call.message.answer(f'И наконец! Ты получаешь исследование по теме <b>{team_name[variant]}</b>',
                              parse_mode='HTML')
    await asyncio.sleep(5)

    await call.message.answer('Покажи тему жизненной ситуации организатору '
                              'и он выдаст тебе персональный чемоданчик для исследования')
    await asyncio.sleep(5)

    await call.message.answer('Получил чемоданчик?', reply_markup=inline_interaction_one)
    await asyncio.sleep(5)


def register_password_write_worker(dp: Dispatcher):
    dp.register_callback_query_handler(password_write_one, text_contains='liveSitSeven', state=None)
    dp.register_callback_query_handler(password_write_two, text_contains='CasePasswordOne', state=None)
    dp.register_callback_query_handler(password_write_three, text_contains='CasePasswordTwo', state=None)
    dp.register_message_handler(password_write_four, state=DataPass.CasePassword)
    dp.register_callback_query_handler(password_write_five, text_contains='CasePasswordThree', state=None)

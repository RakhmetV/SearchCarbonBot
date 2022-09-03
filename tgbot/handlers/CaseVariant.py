import asyncio
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from tgbot.handlers.formulas import calculation_one
from tgbot.handlers.message import case_text_one, case_text_two, case_text_three, case_text_four, case_text_five, \
    case_text_seven
from tgbot.keyboards.inline import carbonInlineOne
from tgbot.services.db import Database
from tgbot.states.test import DataCase
db = Database('database.db')

async def carbon_footprint_answer(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=5)
    await DataCase.Variant.set()

    list_var = db.get_variant(call.message.chat.id)
    print(bool(len(list_var)))
    if bool(len(list_var)):
        variant = list_var[0][0]
        await state.update_data(variant=variant)
    # Фото Гули
    await call.message.answer('Давай рассмотрим жизненные ситуации, на примере которых ты сможешь узнать, '
                              'как можно будет снизить свой углеродный след. \n\nПогнали!')
    await asyncio.sleep(2)
    data = await state.get_data()  # тут хранится весь словарь состояний
    variant_case = data.get('variant')
    await call.message.answer(case_text_one[variant_case])
    await asyncio.sleep(1)

    await call.message.answer(case_text_two[variant_case])
    await asyncio.sleep(1)

    await call.message.answer(case_text_three[variant_case])
    await asyncio.sleep(1)

    await call.message.answer(case_text_four[variant_case])
    await asyncio.sleep(1)

    await DataCase.next()

async def carbon_question_one(message: types.Message, state: FSMContext):
    await state.update_data(one=message.text)
    data = await state.get_data()  # тут хранится весь словарь состояний
    variant_case = data.get('variant')
    await message.answer(case_text_five[variant_case])
    await asyncio.sleep(1)

    await DataCase.next()

async def carbon_question_two(message: types.Message, state: FSMContext):
    await state.update_data(two=message.text)
    data = await state.get_data()  # тут хранится весь словарь состояний
    variant_case = data.get('variant')

    # await message.answer(case_text_six[variant_case])
    # await asyncio.sleep(1)

    answer_a = data.get('one')
    answer_b = data.get('two')
    await message.answer(f'<b>На {calculation_one(variant_case ,answer_a, answer_b)} кг СО2 (углеродного следа) в год</b>\nты сможешь снизить, заменив маленькие флаконы с шампунями на большие', parse_mode='HTML')
    await asyncio.sleep(1)

    await message.answer(case_text_seven[variant_case], reply_markup=carbonInlineOne[0])
    await asyncio.sleep(1)
    print(answer_a, answer_b)
    await DataCase.next()


def register_case_variant(dp: Dispatcher):
    dp.register_callback_query_handler(carbon_footprint_answer, text_contains='carbonAnswer', state=None)
    dp.register_message_handler(carbon_question_one, state=DataCase.QuestionOne)
    dp.register_message_handler(carbon_question_two, state=DataCase.QuestionTwo)

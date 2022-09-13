import asyncio

from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from math import fabs

from tgbot.handlers.formulas import calculation_one, calculation_two
from tgbot.handlers.message_variant import variant_text_one, variant_text_two, variant_text_three, variant_text_four, \
    variant_text_five, variant_text_six, variant_text_seven, variant_text_eight, variant_text_nine, variant_text_ten, \
    variant_text_eleven, variant_text_twelve, variant_text_thirteen, variant_text_fourteen, variant_text_fifteen, \
    variant_text_sixteen, variant_text_seventeen, variant_text_nineteen, variant_text_twenty_one, variant_text_twenty, \
    variant_text_twenty_two, variant_text_twenty_three
from tgbot.keyboards.inline_variant_case import inline_variant_case_one, inline_variant_case_two, \
    inline_variant_case_three, inline_variant_case_four, inline_variant_case_five, inline_variant_case_six
from tgbot.services.db import Database
from tgbot.states.test import DataCase

db = Database('database.db')


async def variant_case_one(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=5)
    await DataCase.Variant.set()

    list_var = db.get_variant(call.message.chat.id)
    if bool(len(list_var)):
        variant = list_var[0][0]
        await state.update_data(variant=variant)
    data = await state.get_data()  # тут хранится весь словарь состояний
    variant_case = data.get('variant')
    await asyncio.sleep(3)
    await call.message.answer(variant_text_one[variant_case])
    await asyncio.sleep(6)

    await call.message.answer(variant_text_two[variant_case])
    await asyncio.sleep(6)

    await call.message.answer(variant_text_three[variant_case], reply_markup=inline_variant_case_one)
    await asyncio.sleep(5)


async def variant_case_two(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=5)
    data = await state.get_data()  # тут хранится весь словарь состояний
    variant_case = data.get('variant')

    await call.message.answer(variant_text_four[variant_case], reply_markup=inline_variant_case_two)


async def variant_case_three(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=5)
    data = await state.get_data()  # тут хранится весь словарь состояний
    variant_case = data.get('variant')
    await asyncio.sleep(2)
    await call.message.answer(variant_text_five[variant_case])
    await asyncio.sleep(5)

    await call.message.answer(variant_text_six[variant_case])
    await asyncio.sleep(5)

    await call.message.answer(variant_text_seven[variant_case])
    await asyncio.sleep(5)

    await call.message.answer(variant_text_eight[variant_case])
    await asyncio.sleep(8)

    await call.message.answer(variant_text_nine[variant_case])
    await asyncio.sleep(5)
    await DataCase.next()


async def variant_question_one(message: types.Message, state: FSMContext):
    data = await state.get_data()  # тут хранится весь словарь состояний
    if not bool(data.get('one')):
        if message.text.isdigit():
            if int(message.text) >= 0:
                await state.update_data(one=int(message.text))

                data = await state.get_data()  # тут хранится весь словарь состояний
                variant_case = data.get('variant')

                formula_first_answer = {  # варианты, которые выводят формулу после первого ответа
                    2: calculation_one(variant_case, int(message.text), 1),
                    4: calculation_one(variant_case, int(message.text), 1),
                    5: calculation_one(variant_case, int(message.text), 1),
                    6: calculation_one(variant_case, int(message.text), 1),
                    8: calculation_one(variant_case, int(message.text), 1)
                }
                await asyncio.sleep(2)
                # 2 4 5 6 8
                if variant_case in formula_first_answer:
                    await DataCase.next()
                    await DataCase.next()

                    result = formula_first_answer[variant_case]
                    if variant_case == 4:
                        await message.answer(
                            f'<b>{result:.2f} гектаров триплоидной осины</b>'
                            f'\n{variant_text_ten[variant_case]}',
                            parse_mode='HTML')
                    else:
                        await message.answer(
                            f'{variant_text_ten[variant_case]}'
                            f'<b>На {result:.2f} кг СО2 (углеродного следа) в год</b>',
                            parse_mode='HTML')

                    db.set_answer_one(message.from_user.id, result)  # в бд первый ответ
                    await asyncio.sleep(5)
                    await message.answer(variant_text_twelve[variant_case])
                    await asyncio.sleep(5)
                    await message.answer(variant_text_thirteen[variant_case],
                                         reply_markup=inline_variant_case_three)



                # 0 1 3 7 9
                else:
                    await message.answer(variant_text_ten[variant_case])
                    if variant_case == 7:
                        await DataCase.next()
                    else:
                        await DataCase.next()
                        await DataCase.next()
            else:
                await message.answer('Введите положительное число.')
        else:
            await message.answer('Введите целое число.')


async def carbon_question_c(message: types.Message, state: FSMContext):
    data = await state.get_data()  # тут хранится весь словарь состояний
    if not bool(data.get('c')):
        if message.text.isdigit():
            if int(message.text) >= 0:
                # 7
                await state.update_data(c=int(message.text))
                await asyncio.sleep(2)
                await message.answer('Какое расстояние от твоего дома до торгового центра?')
                await DataCase.next()
            else:
                await message.answer('Введите положительное число')
        else:
            await message.answer('Введите целое число.')


async def carbon_question_two(message: types.Message, state: FSMContext):
    await asyncio.sleep(1)
    data = await state.get_data()  # тут хранится весь словарь состояний
    if not bool(data.get('two')):
        if message.text.isdigit():
            if int(message.text) >= 0:

                # 0 1 3 7 9

                await state.update_data(two=int(message.text))
                variant_case = data.get('variant')
                await asyncio.sleep(3)
                if variant_case == 0 \
                        or variant_case == 1 \
                        or variant_case == 3 \
                        or variant_case == 7 \
                        or variant_case == 9:

                    if variant_case == 7:
                        answer_a = data.get('one')
                        answer_b = data.get('c')
                        result = fabs((answer_a * answer_b * 12 * 3000 - int(message.text) * 12 * 66) / 1000)
                        db.set_answer_one(message.from_user.id, result)
                        await message.answer(
                            f'Выбирая изначально в интернете одежду, ты можешь снизить\n'
                            f'<b>На {result:.2f} кг СО2 (углеродного следа) в год</b>',
                            parse_mode='HTML')
                        await asyncio.sleep(5)

                        await message.answer(variant_text_twelve[variant_case])
                        await asyncio.sleep(5)
                        await message.answer(variant_text_thirteen[variant_case],
                                             reply_markup=inline_variant_case_three)
                    else:
                        answer_a = data.get('one')
                        answer_b = int(message.text)

                        result = calculation_one(variant_case, answer_a, answer_b)
                        db.set_answer_one(message.from_user.id, result)
                        if variant_case == 3:
                            await message.answer(
                                f'<b>{result:.2f} гектаров соснового леса в год</b>\n{variant_text_eleven[variant_case]}',
                                parse_mode='HTML')
                        else:
                            await message.answer(
                                f'Ты можешь снизить\n'
                                f'<b>На {result:.2f} кг СО2 (углеродного следа) в год</b>\n{variant_text_eleven[variant_case]}',
                                parse_mode='HTML')
                        await asyncio.sleep(5)
                        await message.answer(variant_text_twelve[variant_case])

                        await asyncio.sleep(5)
                        await message.answer(variant_text_thirteen[variant_case],
                                             reply_markup=inline_variant_case_three)
                    # await DataCase.next()
            else:
                await message.answer('Введите положительное число.')
        else:
            await message.answer('Введите целое число.')


async def variant_case_four(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=5)
    data = await state.get_data()  # тут хранится весь словарь состояний
    variant_case = data.get('variant')
    await asyncio.sleep(2)
    await call.message.answer(variant_text_fourteen[variant_case])
    await asyncio.sleep(6)

    await call.message.answer(variant_text_fifteen[variant_case])
    await asyncio.sleep(7)

    await call.message.answer(variant_text_sixteen[variant_case])
    await asyncio.sleep(5)

    await call.message.answer(variant_text_seventeen[variant_case])
    await asyncio.sleep(7)

    await call.message.answer(variant_text_nineteen[variant_case])
    await DataCase.next()


async def carbon_question_three(message: types.Message, state: FSMContext):
    await asyncio.sleep(2)
    # 0 1 2 3 4 5 6 7 8 9

    data = await state.get_data()  # тут хранится весь словарь состояний
    if not bool(data.get('three')):

        if message.text.isdigit():
            if int(message.text) >= 0:
                await state.update_data(three=int(message.text))

                variant_case = data.get('variant')

                formula_first_answer = {  # варианты, которые выводят формулу после первого ответа
                    1: calculation_two(variant_case, int(message.text), 1),
                    2: calculation_two(variant_case, int(message.text), 1),
                    3: calculation_two(variant_case, int(message.text), 1)
                }

                # 1 2 3
                if variant_case in formula_first_answer:
                    result = formula_first_answer[variant_case]
                    if variant_case == 3:
                        await message.answer(
                            f'<b>на {result:.2f} кг СО2 (углеродного следа) в год</b>\n{variant_text_twenty_one[variant_case]}',
                            parse_mode='HTML')
                    else:
                        await message.answer(
                            f'{variant_text_twenty_one[variant_case]}\n<b>На {result:.2f} кг СО2 (углеродного следа) в год</b>',
                            parse_mode='HTML')
                    db.set_answer_two(message.from_user.id, result)

                    await asyncio.sleep(5)
                    await message.answer(variant_text_twenty_two[variant_case], reply_markup=inline_variant_case_four)

                else:
                    # 0 4 5 6 7 8 9
                    await asyncio.sleep(2)
                    await message.answer(variant_text_twenty[variant_case])

                await DataCase.next()
            else:
                await message.answer('Введите положительное число.')
        else:
            await message.answer('Введите целое число.')


async def carbon_question_four(message: types.Message, state: FSMContext):
    await asyncio.sleep(1)
    data = await state.get_data()  # тут хранится весь словарь состояний
    if not bool(data.get('four')):
        if message.text.isdigit():
            if int(message.text) >= 0:
                await asyncio.sleep(2)
                # 0 4 5 6 7 8 9
                variant_case = data.get('variant')
                if variant_case != 1 or variant_case != 2 or variant_case != 3:
                    await state.update_data(four=int(message.text))

                    answer_a = data.get('three')
                    answer_b = int(message.text)

                    result = calculation_two(variant_case, answer_a, answer_b)
                    db.set_answer_two(message.from_user.id, result)
                    if variant_case == 9 or variant_case == 7:
                        await message.answer(
                            f'<b>На {result:.2f} кг СО2 (углеродного следа) в год</b>\n{variant_text_twenty_one[variant_case]}',
                            parse_mode='HTML')
                    else:
                        await message.answer(
                            f'{variant_text_twenty_one[variant_case]}\n<b>на {result:.2f} кг СО2 (углеродного следа) в год</b>',
                            parse_mode='HTML')
                    await asyncio.sleep(6)

                    await message.answer(variant_text_twenty_two[variant_case], reply_markup=inline_variant_case_four)

            else:
                await message.answer('Введите положительное число.')

        else:
            await message.answer('Введите целое число.')


async def variant_case_five(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=5)
    await asyncio.sleep(2)

    await call.message.answer('Отлично, твой персональный вклад в сохранении планеты будет очень существенным!')
    await asyncio.sleep(5)

    await call.message.answer('Готов получить полезный подарок?!', reply_markup=inline_variant_case_five)


async def variant_case_six(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=5)
    data = await state.get_data()  # тут хранится весь словарь состояний
    variant_case = data.get('variant')
    await asyncio.sleep(2)

    await call.message.answer(variant_text_twenty_three[variant_case])
    await asyncio.sleep(5)
    await state.finish()

    await call.message.answer('Как тебе подарок?', reply_markup=inline_variant_case_six)


def register_variant_case(dp: Dispatcher):
    dp.register_callback_query_handler(variant_case_one, text_contains='inlineInteractNine', state=None)
    dp.register_callback_query_handler(variant_case_two, text_contains='inlineVarCaseOne', state=DataCase.Variant)
    dp.register_callback_query_handler(variant_case_three, text_contains='inlineVarCaseTwo', state=DataCase.Variant)
    dp.register_message_handler(variant_question_one, state=DataCase.QuestionOne)
    dp.register_message_handler(carbon_question_c,  state=DataCase.StateC)
    dp.register_message_handler(carbon_question_two,  state=DataCase.QuestionTwo)
    dp.register_callback_query_handler(variant_case_four, text_contains='inlineVarCaseThree', state=DataCase.QuestionTwo)
    dp.register_message_handler(carbon_question_three, state=DataCase.QuestionThree)
    dp.register_message_handler(carbon_question_four, state=DataCase.QuestionFour)
    dp.register_callback_query_handler(variant_case_five, text_contains='inlineVarCaseFour',
                                       state=DataCase.QuestionFour)
    dp.register_callback_query_handler(variant_case_six, text_contains='inlineVarCaseFive',
                                       state=DataCase.QuestionFour)


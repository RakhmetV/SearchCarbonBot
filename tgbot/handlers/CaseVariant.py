import asyncio
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, InputFile
from aiogram.utils.markdown import hlink
from math import fabs

from tgbot.handlers.formulas import calculation_one, calculation_two
from tgbot.handlers.message import case_text_one, case_text_two, case_text_three, case_text_four, case_text_five, \
    case_text_seven, case_text_eight, case_text_nine, case_text_ten, case_text_eleven, case_text_thirteen, \
    case_text_fourteen, case_text_fifteen, case_text_sixteen, case_text_seventeen, case_text_six, case_text_twelve
from tgbot.keyboards.inline import carbonInlineOne, carbonInlineTwo, carbonInlineThree, carbonInlineFour
from tgbot.services.db import Database
from tgbot.states.test import DataCase

db = Database('database.db')


async def carbon_footprint_answer(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=5)
    await DataCase.Variant.set()

    list_var = db.get_variant(call.message.chat.id)
    if bool(len(list_var)):
        variant = list_var[0][0]
        await state.update_data(variant=variant)
    # Фото Гули
    photo = InputFile("gulya.png")

    await call.message.answer_photo(photo, caption='Давай рассмотрим жизненные ситуации, на примере которых ты сможешь узнать, '
                              'как можно будет снизить свой углеродный след. \n\nПогнали!')

    # await call.message.answer('Давай рассмотрим жизненные ситуации, на примере которых ты сможешь узнать, '
    #                           'как можно будет снизить свой углеродный след. \n\nПогнали!')
    await asyncio.sleep(2)
    data = await state.get_data()  # тут хранится весь словарь состояний
    variant_case = data.get('variant')
    print(bool(data.get('variant')))
    print(bool(data.get('aaa')))
    await call.message.answer(case_text_one[variant_case])
    await asyncio.sleep(1)

    await call.message.answer(case_text_two[variant_case])
    await asyncio.sleep(1)

    await call.message.answer(case_text_three[variant_case])
    await asyncio.sleep(1)

    await call.message.answer(case_text_four[variant_case])

    await DataCase.next()


async def carbon_question_one(message: types.Message, state: FSMContext):
    await asyncio.sleep(1)
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

                # 2 4 5 6 8
                if variant_case in formula_first_answer:
                    await DataCase.next()
                    await DataCase.next()

                    result = formula_first_answer[variant_case]
                    if variant_case == 4:
                        await message.answer(
                            f'<b>{result:.2f} гектаров триплоидной осины</b>'
                            f'\n{case_text_six[variant_case]}',
                            parse_mode='HTML')
                    else:
                        await message.answer(
                            f'<b>На {result:.2f} кг СО2 (углеродного следа) в год</b>'
                            f'\n{case_text_six[variant_case]}',
                            parse_mode='HTML')

                    db.set_answer_one(message.from_user.id, result)  # в бд первый ответ
                    await asyncio.sleep(1)

                    if variant_case == 2 or variant_case == 6:  # сперва сообщение потом inline кнопки
                        await message.answer(case_text_five[variant_case])
                        await asyncio.sleep(1)

                        await message.answer(case_text_seven[variant_case], reply_markup=carbonInlineOne[variant_case])

                    else:  # сразу inline кнопки
                        await message.answer(case_text_seven[variant_case], reply_markup=carbonInlineOne[variant_case])

                # 0 1 3 7 9
                else:
                    await message.answer(case_text_five[variant_case])
                    if variant_case == 7:
                        await DataCase.next()
                    else:
                        await DataCase.next()
                        await DataCase.next()
            else:
                await message.answer('Введите положительное число.')
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
                            f'<b>На {result:.2f} кг СО2 (углеродного следа) в год</b>\n{case_text_six[variant_case]}',
                            parse_mode='HTML')

                        await message.answer(case_text_seven[variant_case], reply_markup=carbonInlineOne[variant_case])

                    else:
                        answer_a = data.get('one')
                        answer_b = int(message.text)

                        result = calculation_one(variant_case, answer_a, answer_b)
                        db.set_answer_one(message.from_user.id, result)
                        await message.answer(
                            f'<b>На {result:.2f} кг СО2 (углеродного следа) в год</b>\n{case_text_six[variant_case]}',
                            parse_mode='HTML')
                        await asyncio.sleep(1)

                        if variant_case == 3:
                            await asyncio.sleep(1)
                        else:
                            await message.answer(case_text_seven[variant_case], reply_markup=carbonInlineOne[0])
                    # await DataCase.next()
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

                await message.answer('Какое расстояние от твоего дома до торгового центра?')
                await DataCase.next()
            else:
                await message.answer('Введите положительное число')
        else:
            await message.answer('Введите целое число.')


async def carbon_inline_keyboard_one(call: CallbackQuery, state: FSMContext):
    # 0 1 2 4 5 6 7 8 9
    # все кроме 3
    await call.answer(cache_time=5)
    await asyncio.sleep(1)
    data = await state.get_data()  # тут хранится весь словарь состояний
    variant_case = data.get('variant')

    await call.message.answer(case_text_eight[variant_case])
    await asyncio.sleep(1)

    await call.message.answer(case_text_nine[variant_case])
    await asyncio.sleep(1)

    await call.message.answer(case_text_ten[variant_case])
    await DataCase.next()


async def carbon_question_three(message: types.Message, state: FSMContext):
    await asyncio.sleep(1)
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
                    await message.answer(
                        f'<b>на {result:.2f} кг СО2 (углеродного следа) в год</b>\n{case_text_twelve[variant_case]}',
                        parse_mode='HTML')
                    db.set_answer_two(message.from_user.id, result)

                    if variant_case == 1:
                        await message.answer(f'{case_text_thirteen[variant_case]}')
                        await asyncio.sleep(1)

                        await message.answer(f'{case_text_fourteen[variant_case]}', reply_markup=carbonInlineTwo[0])
                        await asyncio.sleep(1)

                    elif variant_case == 2:
                        await message.answer(f'{case_text_fourteen[variant_case]}', reply_markup=carbonInlineTwo[0])
                        await asyncio.sleep(1)
                    else:
                        # 3
                        await message.answer(f'{case_text_thirteen[variant_case]}')
                        await asyncio.sleep(1)

                        await message.answer(f'{case_text_fifteen[variant_case]}')
                        await asyncio.sleep(1)

                        await message.answer(f'{case_text_sixteen[variant_case]}',
                                             reply_markup=carbonInlineThree[variant_case])
                        await asyncio.sleep(1)

                else:
                    # 0 4 5 6 7 8 9
                    await asyncio.sleep(1)
                    await message.answer(case_text_eleven[variant_case])

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

                # 0 4 5 6 7 8 9
                variant_case = data.get('variant')
                if variant_case != 1 or variant_case != 2 or variant_case != 3:
                    await state.update_data(four=int(message.text))

                    answer_a = data.get('three')
                    answer_b = int(message.text)

                    result = calculation_two(variant_case, answer_a, answer_b)
                    db.set_answer_two(message.from_user.id, result)
                    await message.answer(
                        f'<b>на {result:.2f} кг СО2 (углеродного следа) в год</b>\n{case_text_twelve[variant_case]}',
                        parse_mode='HTML')
                    await asyncio.sleep(2)

                    if variant_case == 4 or variant_case == 6:
                        await message.answer(case_text_fourteen[variant_case],
                                             reply_markup=carbonInlineTwo[variant_case])
                    elif variant_case == 7:
                        await message.answer(case_text_thirteen[variant_case])
                        await asyncio.sleep(1)
                        await message.answer(
                            'Внутри твоего персонального набора тебя ждет подарок - два набора термонаклеек!\n\n'
                            'С помощью них ты можешь подарить вторую жизнь своим вещам!')
                        await asyncio.sleep(1)
                        await message.answer(case_text_fourteen[variant_case],
                                             reply_markup=carbonInlineTwo[variant_case])
                    elif variant_case == 8:
                        await message.answer(case_text_thirteen[variant_case])
                        await asyncio.sleep(1)
                        await message.answer(
                            'Внутри твоего персонального набора тебя ждет подарок - набор фосфорных наклеек для потолка!\n\n'
                            'Используй его вместо ночника. Твоя комната будет краше и не настолько темной с фосфорными наклейками!')
                        await asyncio.sleep(1)
                        await message.answer(case_text_fourteen[variant_case],
                                             reply_markup=carbonInlineTwo[variant_case])

                    else:
                        await message.answer(case_text_thirteen[variant_case])
                        await asyncio.sleep(1)

                        await message.answer(case_text_fourteen[variant_case],
                                             reply_markup=carbonInlineTwo[variant_case])
            else:
                await message.answer('Введите положительное число.')

        else:
            await message.answer('Введите целое число.')


async def carbon_inline_keyboard_two(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=5)
    await asyncio.sleep(1)
    data = await state.get_data()  # тут хранится весь словарь состояний
    variant_case = data.get('variant')
    # 0 1 4 7 8 9
    if variant_case == 7 or variant_case == 8:
        await call.message.answer(case_text_sixteen[variant_case], reply_markup=carbonInlineFour[0])
        await asyncio.sleep(1)
    else:
        if variant_case == 4:
            await call.message.answer('И наш заключительный совет\n\n!Летом мы советуем тебе гулять на природе. '
                                      'А если ты любишь заниматься спортом, то бегать и заниматься йогой можно в парках. '
                                      'Занятия на природе лучше еще тем, что они вместо тренажеров,требующих электроэнергию. ')
            await asyncio.sleep(1)

        await call.message.answer(case_text_fifteen[variant_case])
        await asyncio.sleep(1)

        await call.message.answer(case_text_sixteen[variant_case], reply_markup=carbonInlineThree[variant_case])
        await asyncio.sleep(1)


async def carbon_inline_keyboard_three(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=5)
    data = await state.get_data()  # тут хранится весь словарь состояний
    variant_case = data.get('variant')

    await call.message.answer(case_text_seventeen[variant_case], reply_markup=carbonInlineFour[0])
    await asyncio.sleep(1)


async def carbon_inline_keyboard_four(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=5)
    await call.message.answer(
        'Нам было очень приятно проводить обучающее исследование с тобой!'
        '\nНадеемся, что ты открыл для себя что-то новое и полезное')
    await asyncio.sleep(2)
    await call.message.answer('Мы будем очень рады, если ты оставишь отзыв о сегодняшнем обучающем исследовании')
    await DataCase.next()


async def carbon_feedback(message: types.Message, state: FSMContext):
    txt = message.text
    if len(txt) > 250:
        await message.answer(f'Количество допустимых символов: 250\nКоличество ваших смволов: {len(txt)}')
    else:
        await state.finish()
        db.set_feedback(message.from_user.id, txt)
        db.set_status(message.from_user.id, 1)
        await asyncio.sleep(1)
        await message.answer('Спасибо большое за отзыв!')
        await asyncio.sleep(2)
        link_one = hlink('Обучающее-исследование', 'https://xn----7sbbbhlfabd2ae8a6adj1ca5a4fzb5g.xn--p1ai/')
        link_two = hlink('официальном сайте Благотворительного фонда “Татнефть', 'http://bf-tatneft.ru/fond/?1main')
        link_three = hlink('сайте Всероссийского образовательного проекта “Образ. будущего“', 'https://obrazbudu.ru/')
        link_four = hlink('сайте Интерактивного центра “Альметрика”', 'https://almetrika.ru/')
        await message.answer(f'Мы собрали для тебя полезные ссылки, лови!\n\n'
                             f'{link_one} - Сайт обучающего исследования “В поисках углеродного следа”.'
                             f'На этом сайте будут выкладываться все результаты исследования школьников из 7 районов '
                             f'Республики Татарстан, фото и видеоматериалы\n\n'
                             f'На {link_two}'
                             f'ты можешь ознакомиться со всеми программами и проектами БФ '
                             f'“Татнефть” и в последующем принять участие в них\n\n'
                             f'На {link_three} ты можешь следить за деятельностью проекта\n\n'
                             f'На {link_four} ты можешь смотреть расписание мастер-классов и научно-познавательных экскурсий',
                             disable_web_page_preview=True)
        await asyncio.sleep(3)

        await message.answer('Спасибо, что ты был сегодня с нами и прошел обучающее исследование '
                             '“В поисках углеродного следа”\n\n'
                             'До новых встреч!')


def register_case_variant(dp: Dispatcher):
    # dp.register_callback_query_handler(carbon_footprint_answer, text_contains='carbonAnswer', state=None)
    dp.register_message_handler(carbon_question_one, state=DataCase.QuestionOne)
    dp.register_message_handler(carbon_question_two, state=DataCase.QuestionTwo)
    dp.register_callback_query_handler(carbon_inline_keyboard_one, text_contains='carbonInOne',
                                       state=DataCase.QuestionTwo)

    dp.register_message_handler(carbon_question_three, state=DataCase.QuestionThree)
    dp.register_message_handler(carbon_question_four, state=DataCase.QuestionFour)
    dp.register_callback_query_handler(carbon_inline_keyboard_two, text_contains='carbonInTwo',
                                       state=DataCase.QuestionFour)
    dp.register_callback_query_handler(carbon_inline_keyboard_three, text_contains='carbonInThree',
                                       state=DataCase.QuestionFour)
    dp.register_callback_query_handler(carbon_inline_keyboard_four, text_contains='carbonInFour',
                                       state=DataCase.QuestionFour)
    dp.register_message_handler(carbon_feedback, state=DataCase.FeedBack)
    dp.register_message_handler(carbon_question_c, state=DataCase.StateC)

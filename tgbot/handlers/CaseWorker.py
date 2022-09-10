import asyncio
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from tgbot.keyboards.inline import researchesStart, carbon_footprint, carbonFootprintTest, carbonFootprintAnswer, \
    inline_interaction_three
from tgbot.states.test import Data


async def researches_start(call: CallbackQuery):
    await call.answer(cache_time=5)

    # Фото Никиты

    await call.message.answer('Я очень рад, что тебе понравился набор. '
                                                   'Давай его распаковывать :)',
                                    reply_markup=inline_interaction_three)

    await asyncio.sleep(1)
    await call.message.answer(
        'Внутри набора лежат все необходимое, которое поможет тебе провести исследование: '
        'письмо-приветствие, секретный конверт, бандана и полезный подарок')
    await asyncio.sleep(1)

    await call.message.answer('Для начала прочитай письмо-приветствие')
    await asyncio.sleep(1)


    await call.message.answer('Ну что, перейдем к исследованию?', reply_markup=researchesStart)
    await asyncio.sleep(1)


async def studying_the_topic(call: CallbackQuery):
    await call.answer(cache_time=5)

    # Фото Яны

    await call.message.answer('Слышал ли ты когда нибудь об углеродном следе?',
                                    reply_markup=carbon_footprint)
    # await call.message.answer('Слышал ли ты когда нибудь об углеродном следе?', reply_markup=carbon_footprint)
    await asyncio.sleep(1)


async def carbon_footprint_info(call: CallbackQuery):
    await call.answer(cache_time=5)
    await call.message.answer("""Углеродный след - это совокупность всех парниковых газов, которые попадают в окружающую среду от деятельности людей, организаций, компаний, городов и стран. 

В состав парниковых газов входит углекислый газ СО2, метан СН4, закись азота N2O, водяной пар Н2О и фторированные газы. Так как большая часть, на 80%, парникового газа состоит из СО2, то след называют углеродным.""")
    await asyncio.sleep(1)

    await call.message.answer(
        'Сами по себе парниковые газы не несут вреда, но они усиливают естественное явление - парниковый эффект. '
        'Этот эффект позволяет поддерживать комфортную температуру для жизни на Земле. '
        'Но увеличение концентрации парниковых газов сопутствуют изменению климата на Земле')
    await asyncio.sleep(1)
    await call.message.answer('Давай повторим изученное:\n'
                              'Какой газ не входит в состав парниковых газов?', reply_markup=carbonFootprintTest)


async def carbon_footprint_test(call: CallbackQuery):
    await call.answer(cache_time=5)

    await call.message.answer('Ошибочка, на самом деле, сернистый газ H2S  не входит в состав парниковых газов')
    await asyncio.sleep(1)

    # Фото Тимура

    await call.message.answer('А еще углеродный след бывает прямым и косвенным. '
                                                   'Например, поездка на машине, использование газа для готовки еды - это прямые выбросы. '
                                                   'А покупка игрушечной машины, которая производилась на предприятии, где использовалось '
                                                   'тепло и электроэнергию на изготовление игрушечной машины, а еще и ее доставка до места '
                                                   'продажи - это косвенные выбросы.')
    await asyncio.sleep(1)
    # await call.message.answer('А еще углеродный след бывает прямым и косвенным. '
    #                           'Например, поездка на машине, использование газа для готовки еды - это прямые выбросы. '
    #                           'А покупка игрушечной машины, которая производилась на предприятии, где использовалось '
    #                           'тепло и электроэнергию на изготовление игрушечной машины, а еще и ее доставка до места '
    #                           'продажи - это косвенные выбросы.')

    await call.message.answer('Если мы оставляем углеродный след, то значит, '
                              'мы сами же можем сделать так, чтобы его было меньше. '
                              '\nДа, ведь?', reply_markup=carbonFootprintAnswer)


async def carbon_footprint_test_answer(call: CallbackQuery):
    await call.answer(cache_time=5)
    await call.message.answer('Все верно, сернистый газ H2S  не входит в состав парниковых газов')

    await asyncio.sleep(1)

    # Фото Тимура

    await call.message.answero('А еще углеродный след бывает прямым и косвенным. '
                                                   'Например, поездка на машине, использование газа для готовки еды - это прямые выбросы. '
                                                   'А покупка игрушечной машины, которая производилась на предприятии, где использовалось '
                                                   'тепло и электроэнергию на изготовление игрушечной машины, а еще и ее доставка до места '
                                                   'продажи - это косвенные выбросы.')
    await asyncio.sleep(1)

    # await call.message.answer('А еще углеродный след бывает прямым и косвенным. '
    #                           'Например, поездка на машине, использование газа для готовки еды - это прямые выбросы. '
    #                           'А покупка игрушечной машины, которая производилась на предприятии, где использовалось '
    #                           'тепло и электроэнергию на изготовление игрушечной машины, а еще и ее доставка до места '
    #                           'продажи - это косвенные выбросы.')

    await call.message.answer('Если мы оставляем углеродный след, то значит, '
                              'мы сами же можем сделать так, чтобы его было меньше. '
                              '\nДа, ведь?', reply_markup=carbonFootprintAnswer)


def register_case_worker(dp: Dispatcher):
    dp.register_callback_query_handler(researches_start, text_contains='likeSet', state=None)
    dp.register_callback_query_handler(studying_the_topic, text_contains='resStart', state=None)
    dp.register_callback_query_handler(carbon_footprint_info, text_contains='carbonfootprint', state=None)
    dp.register_callback_query_handler(carbon_footprint_test, text_contains='carbonTest', state=None)
    dp.register_callback_query_handler(carbon_footprint_test_answer, text_contains='carbonTesAnswer', state=None)

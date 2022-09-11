import asyncio
from aiogram import Dispatcher
from aiogram.types import CallbackQuery

from tgbot.keyboards.inline_live_situation import inline_live_sit_one, inline_live_sit_two, inline_live_sit_three, \
    inline_live_sit_four, inline_live_sit_five, inline_live_sit_six, inline_live_sit_seven


async def live_situation_one(call: CallbackQuery):
    await call.answer(cache_time=5)
    await call.message.answer(
        'Давай рассмотрим жизненные ситуации, на примере которых ты сможешь узнать, '
        'как можно будет снизить свой углеродный след\n\n'
        'Погнали!')
    await asyncio.sleep(1)

    await call.message.answer(
        'На примере жизни каждого школьникам можем рассмотреть '
        'несколько ситуаций и придумать то, как в них можно '
        'снизить углеродный след')
    await asyncio.sleep(1)

    await call.message.answer(
        'Вот какие жизненные ситуации сегодня мы разберем', reply_markup=inline_live_sit_one)
    await asyncio.sleep(1)


async def live_situation_two(call: CallbackQuery):
    await call.answer(cache_time=5)
    await call.message.answer(
        'Ванные процедуры - мы умываемся, расходуем воду, '
        'используем флаконы для косметических средств.'
        ' Практически на каждом шагу '
        'можно снизить углеродный след', reply_markup=inline_live_sit_two)
    await asyncio.sleep(1)


async def live_situation_three(call: CallbackQuery):
    await call.answer(cache_time=5)
    await call.message.answer(
        'Поездка в школу - мы пользуемся средствами передвижения ежедневно: автомобили, автобусы, поезда,')
    await asyncio.sleep(1)
    await call.message.answer(
        'Школьные уроки -', reply_markup=inline_live_sit_three)
    await asyncio.sleep(1)


async def live_situation_four(call: CallbackQuery):
    await call.answer(cache_time=5)
    await call.message.answer(
        'Экскурсия на предприятие -')
    await asyncio.sleep(1)

    await call.message.answer(
        'Увлечения, хобби -', reply_markup=inline_live_sit_four)
    await asyncio.sleep(1)


async def live_situation_five(call: CallbackQuery):
    await call.answer(cache_time=5)
    await call.message.answer(
        'Уборка по дому -', reply_markup=inline_live_sit_five)
    await asyncio.sleep(1)


async def live_situation_six(call: CallbackQuery):
    await call.answer(cache_time=5)
    await call.message.answer(
        'Покупка вещей -')
    await asyncio.sleep(1)

    await call.message.answer(
        'Здоровый сон -', reply_markup=inline_live_sit_six)
    await asyncio.sleep(1)


async def live_situation_seven(call: CallbackQuery):
    await call.answer(cache_time=5)
    await call.message.answer(
        'Поход, путешествие -')
    await asyncio.sleep(1)

    await call.message.answer(
        'И сегодня ты будешь разбирать одну из данных тем для исследования', reply_markup=inline_live_sit_seven)
    await asyncio.sleep(1)


def register_live_situation_worker(dp: Dispatcher):
    dp.register_callback_query_handler(live_situation_one, text_contains='carbonAnswer', state=None)
    dp.register_callback_query_handler(live_situation_two, text_contains='liveSitOne', state=None)
    dp.register_callback_query_handler(live_situation_three, text_contains='liveSitTwo', state=None)
    dp.register_callback_query_handler(live_situation_four, text_contains='liveSitThree', state=None)
    dp.register_callback_query_handler(live_situation_five, text_contains='liveSitFour', state=None)
    dp.register_callback_query_handler(live_situation_six, text_contains='liveSitFive', state=None)
    dp.register_callback_query_handler(live_situation_seven, text_contains='liveSitSix', state=None)
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
        'Погнали☺')
    await asyncio.sleep(6)

    await call.message.answer(
        'На примере жизни каждого школьникам можем рассмотреть '
        'несколько ситуаций и придумать то, как в них можно '
        'снизить углеродный след')
    await asyncio.sleep(6)

    await call.message.answer(
        'Вот какие жизненные ситуации сегодня мы разберем', reply_markup=inline_live_sit_one)
    await asyncio.sleep(5)


async def live_situation_two(call: CallbackQuery):
    await call.answer(cache_time=5)
    await call.message.answer(
        'Ванные процедуры🚰\n\n'
        'Мы умываемся, расходуем воду, '
        'используем флаконы для косметических средств.'
        '\n\nПрактически на каждом шагу '
        'можно снизить углеродный след', reply_markup=inline_live_sit_two)
    await asyncio.sleep(7)


async def live_situation_three(call: CallbackQuery):
    await call.answer(cache_time=5)
    await call.message.answer(
        'Поездка в школу🚌\n\n'
        'Утро обычного школьника не обходится без '
        'выбора способа передвижения до школы.\n\n'
        'Важно знать, что '
        'каждый вид транспорта оставляет углеродный след, будь то: '
        'автомобиль, троллейбус, автобус и т п.')
    await asyncio.sleep(8)
    await call.message.answer(
        'Школьные уроки\n\n'
        'Мы ходим в школу, меняем одежду и обувь, пьем воду и используем много бумаги. И каждое наше действие в школе оставляет углеродный след.'
        '\n\nС помощью простых эко-привычек можно снизить углеродный след в школе!', reply_markup=inline_live_sit_three)
    await asyncio.sleep(5)


async def live_situation_four(call: CallbackQuery):
    await call.message.answer(
        'Экскурсия на предприятие🏭\n\n'
        'Думаем, каждый из вас немного знаком с промышленностью и вы знаете, что она также влияет на окружающую среду.\n\n'
        'Каждое предприятие с ответственностью подходит к этому вопросу и старается снижать углеродный след')
    await asyncio.sleep(8)

    await call.message.answer(
        'Увлечения, хобби🎨🏀\n\n'
        'У каждого из нас есть'
        ' различные увлечения, способы проведения досуга. '
        'И представляете, каждый из них оставляет за собой '
        'углеродный след!\n\n'
        'Есть много способов проведения '
        'свободного времени не только с пользой для себя, но '
        'и природе!', reply_markup=inline_live_sit_four)
    await asyncio.sleep(10)


async def live_situation_five(call: CallbackQuery):
    await call.answer(cache_time=5)
    await call.message.answer(
        'Питание, продукты🍎🥦🥖\n\n'
        'Все мы любим ходить в магазины за '
        'различными вкусняшками, но это можно делать и с пользой '
        'для природы.\n\n'
        'Дело в том, что покупая продукты мы можем '
        'значительно снизить углеродный след !')
    await asyncio.sleep(8)

    await call.message.answer(
        'Уборка по дому🧽🗑\n\n'
        'При уборке помещения мы используем различную бытовую химию, расходуем воду и прочее.\n\n'
        'Практически на каждом шагу можно снизить углеродный след', reply_markup=inline_live_sit_five)
    await asyncio.sleep(5)


async def live_situation_six(call: CallbackQuery):
    await call.answer(cache_time=5)
    await call.message.answer(
        'Покупка вещей🛍\n\n'
        'Порой наши любимые вещи приходят в негодность '
        '(где-то порвались, запачкались), но не стоит забывать о том, '
        'что можно дать вторую жизнь своей любимой вещи\n\n'
        'Так мы будем модными и экологичными! Снизим углеродный след!')
    await asyncio.sleep(5)

    await call.message.answer(
        'Здоровый сон🛏🌕\n\n'
        'Во время отдыха и сна есть много способов снизить углеродный след: отключение электроприборов от сетей, диджитал-детокс, использование энергосберегающих ночников', reply_markup=inline_live_sit_six)
    await asyncio.sleep(5)


async def live_situation_seven(call: CallbackQuery):
    await call.answer(cache_time=5)
    await call.message.answer(
        'Поход, путешествие🏕\n\n'
        'Мы часто отдыхаем на природе, любим исследовать новые места и на каждом действии оставляем углеродный след.\n\n'
        'Есть много способов его снизить во время путешествия')
    await asyncio.sleep(5)

    await call.message.answer(
        'И в сегодняшнем исследовании ты будешь разбирать свою тему💥', reply_markup=inline_live_sit_seven)
    await asyncio.sleep(5)


def register_live_situation_worker(dp: Dispatcher):
    dp.register_callback_query_handler(live_situation_one, text_contains='carbonAnswer', state=None)
    dp.register_callback_query_handler(live_situation_two, text_contains='liveSitOne', state=None)
    dp.register_callback_query_handler(live_situation_three, text_contains='liveSitTwo', state=None)
    dp.register_callback_query_handler(live_situation_four, text_contains='liveSitThree', state=None)
    dp.register_callback_query_handler(live_situation_five, text_contains='liveSitFour', state=None)
    dp.register_callback_query_handler(live_situation_six, text_contains='liveSitFive', state=None)
    dp.register_callback_query_handler(live_situation_seven, text_contains='liveSitSix', state=None)

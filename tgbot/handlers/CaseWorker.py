import asyncio
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from tgbot.keyboards.inline import researchesStart
from tgbot.states.test import Data


async def researches_start(call: CallbackQuery):
    await call.answer(cache_time=5)

    # Фото Никиты
    await call.message.answer('Я очень рад, что тебе понравился набор. Давай его распаковывать :)')

    await asyncio.sleep(1)
    await call.message.answer(
        'Внутри набора лежат все необходимое, которое поможет тебе провести исследование: письмо-приветствие, конверт, бандана и полезный подарок')
    await asyncio.sleep(1)
    await call.message.answer('Ну что, перейдем к исследованию?', reply_markup=researchesStart)
    await Data.Name.set()


async def studying_the_topic(call: CallbackQuery):
    await call.answer(cache_time=5)

def register_data_collection(dp: Dispatcher):
    dp.register_callback_query_handler(researches_start, text_contains='likeSet', state=None)
    dp.register_callback_query_handler(studying_the_topic, text_contains='researchesStart', state=None)

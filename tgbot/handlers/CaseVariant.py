from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

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
        await DataCase.next()
    # Фото Гули
    await call.message.answer('Давай рассмотрим жизненные ситуации, на примере которых ты сможешь узнать, '
                              'как можно будет снизить свой углеродный след. \n\nПогнали!')


def register_case_variant(dp: Dispatcher):
    dp.register_callback_query_handler(carbon_footprint_answer, text_contains='carbonAnswer', state=None)

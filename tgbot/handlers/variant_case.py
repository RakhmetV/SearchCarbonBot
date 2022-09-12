from aiogram import Dispatcher
from aiogram.types import CallbackQuery


async def variant_case_one(call: CallbackQuery):
    await call.answer(cache_time=5)


def register_variant_case(dp: Dispatcher):
    dp.register_callback_query_handler(variant_case_one, text_contains='inlineInteractNine', state=None)
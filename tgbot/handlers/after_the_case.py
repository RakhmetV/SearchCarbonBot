import asyncio
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from tgbot.keyboards.inline_after_case import inline_after_case_one, inline_after_case_two
from tgbot.states.test import AfterCasePass


async def after_case_one(call: CallbackQuery):
    await call.answer(cache_time=5)
    await call.message.answer('Теперь поделись полученными знаниями с другими из команды ребятами\n\n'
                              'В этом поможет тебе организатор')
    await asyncio.sleep(1)

    await call.message.answer('После того, как задание будет выполнено, организатор вам скажет код')
    await asyncio.sleep(1)

    await call.message.answer('Введи код')
    await AfterCasePass.Password.set()


async def after_case_two(message: types.Message, state: FSMContext):
    if message.text == 'конференция' or message.text == 'Конференция':
        await state.finish()
        await message.answer('Поздравляю!\n\n'
                             'Ты успешно прошел обучающее исследование '
                             '“В поисках углеродного следа” ')
        await asyncio.sleep(1)

        await message.answer('Теперь ты получаешь удостоверение '
                             '“будущего исследователя” и можешь '
                             'гордо нести данное звание', reply_markup=inline_after_case_one)
        await asyncio.sleep(1)
    else:
        await message.answer('Вы ввели неправильный пароль.\nПовторите снова')


async def after_case_three(call: CallbackQuery):
    await call.answer(cache_time=5)
    await call.message.answer('Нам было очень приятно проводить обучающее исследование с тобой!\n\n'
                              'Ты отличный член команды')
    await asyncio.sleep(1)

    await call.message.answer('Мы с тобой')
    await asyncio.sleep(1)

    await call.message.answer('Гуля')
    await asyncio.sleep(1)

    await call.message.answer('Яна')
    await asyncio.sleep(1)

    await call.message.answer('Никита')
    await asyncio.sleep(1)

    await call.message.answer('Мы будем очень рады, если ты оставишь '
                              'отзыв о сегодняшнем обучающем исследовании')
    await asyncio.sleep(1)


async def after_case_four(message: types.Message, state: FSMContext):
    if len(message.text) <= 250:
        await message.answer('Спасибо, что ты был сегодня с нами и прошел '
                             'обучающее исследование '
                             '“В поисках углеродного следа”', reply_markup=inline_after_case_two)
    else:
        await message.answer(f'Количество допустимых символов: 250\n'
                             f'Количество введенных символов: {len(message.text)}')


def register_after_the_case(dp: Dispatcher):
    dp.register_callback_query_handler(after_case_one, text_contains='afterCaseOne', state=None)

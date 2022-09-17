import asyncio

from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from tgbot.keyboards.inline import inline_interaction_two, inline_interaction_three, inline_interaction_four, \
    inline_interaction_six, inline_interaction_seven, inline_interaction_eight, inline_interaction_nine, \
    inline_interaction_five
from tgbot.states.test import InterPass


# async def interact_case_one(call: CallbackQuery):
#     await call.answer(cache_time=5)
#
#     await call.message.answer('Как тебе набор?', reply_markup=inline_interaction_two)



async def interact_case_two(call: CallbackQuery):
    await call.answer(cache_time=5)
    await call.message.answer('Для начала откроем чемоданчик',
                              reply_markup=inline_interaction_three)


async def interact_case_three(call: CallbackQuery):
    await call.answer(cache_time=5)
    await call.message.answer('Внутри чемоданчика лежат все необходимое, которое поможет тебе провести исследование🔍:\n\n'
                              '•письмо-приветствие\n'
                              '•конверт\n'
                              '•бандана\n'
                              '•полезный подарок')
    await asyncio.sleep(7)

    await call.message.answer('Для начала прочитай письмо-приветствие, которое находится в конверте✉')
    await asyncio.sleep(5)

    await call.message.answer('Прочитал?', reply_markup=inline_interaction_four)


async def interact_case_four(call: CallbackQuery):
    await call.answer(cache_time=5)
    await call.message.answer('Теперь прочитай еще раз и найди все цифры в тексте🔢',
                              reply_markup=inline_interaction_five)


async def interact_case_five(call: CallbackQuery):
    await call.answer(cache_time=5)
    await call.message.answer('Расположи их в виде возрастаниями\n\n'
                              'Это будет являться паролем')
    await asyncio.sleep(5)

    await call.message.answer('Введи пароль')
    await InterPass.InterPassword.set()


async def interact_case_six(message: types.Message, state: FSMContext):
    data = await state.get_data()  # тут хранится весь словарь состояний
    if not bool(data.get('password_interact')):
        if message.text == '012567':
            await state.update_data(password_interact=message.text)
            await asyncio.sleep(1)

            await message.answer('Супер, теперь переходим к следующему реквизиту для исследования, к бандане!')
            await asyncio.sleep(5)

            await message.answer('Получилось её найти?', reply_markup=inline_interaction_six)

        else:
            await message.answer('Вы ввели неправильный пароль. Введите его снова')


async def interact_case_seven(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=5)
    await call.message.answer('В этой бандане нарисованы символы всех жизненных ситуаций, которых будем исследовать🙌')
    await asyncio.sleep(5)

    await call.message.answer('Ты можешь повязать бандану на руку или придумать '
                              'любое применение, которое тебе нравится', reply_markup=inline_interaction_seven)


async def interact_case_eight(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=5)
    await call.message.answer('Открой конверт😉', reply_markup=inline_interaction_eight)


async def interact_case_nine(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=5)
    await state.finish()
    await call.message.answer('Как ты видишь, внутри него лежит комикс и плакат🧩\n\n'
                              'Ты можешь повесить плакат на стену, а комикс '
                              'нам понадобится при проведении исследования')
    await asyncio.sleep(5)

    await call.message.answer('Кроме всего этого есть полезные подарки, но о них мы расскажем чуть позже')
    await asyncio.sleep(5)

    await call.message.answer('Ну что, перейдем к исследованию?', reply_markup=inline_interaction_nine)


def register_interaction_case(dp: Dispatcher):
    dp.register_callback_query_handler(interact_case_two, text_contains='liveSitSeven', state=None)
    dp.register_callback_query_handler(interact_case_three, text_contains='inlineInteractThree', state=None)
    dp.register_callback_query_handler(interact_case_four, text_contains='inlineInteractFour', state=None)
    dp.register_callback_query_handler(interact_case_five, text_contains='inlineInteractFive', state=None)
    dp.register_message_handler(interact_case_six, state=InterPass.InterPassword)
    dp.register_callback_query_handler(interact_case_seven, text_contains='inlineInteractSix', state=InterPass.InterPassword)
    dp.register_callback_query_handler(interact_case_eight, text_contains='inlineInteractSeven', state=InterPass.InterPassword)
    dp.register_callback_query_handler(interact_case_nine, text_contains='inliIterEight', state=InterPass.InterPassword)

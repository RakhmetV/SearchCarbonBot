from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext

from tgbot.services.db import Database
from tgbot.states.test import Test


async def enter_test(message: types.Message):
    await message.answer(f'Здравствуйте, {message.from_user.first_name}\n'
                         f'Вы начали новое тестирование!\n'
                         f'Сколько вам лет?')
    # указываем состояние одним из двух вариантов
    await Test.Q1.set()
    # await Test.first()


async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text

    # записываем ответ в state
    await state.update_data(answer1=answer)

    # записываем ответ в state Вариант 2
    # await state.update_data(
    #     {'answear1':answer}
    # )

    # записываем ответ в state Вариант 3
    # async with state.proxy() as data:
    #     data['answer1'] = answer
    # Удобно, если нужно сделать data['answer1']+=1
    # или data['list'].append(1), т.к не нужно сначала доставать из стейта. а потом задавать

    await message.answer(f'Вопрос 2\n'
                         f'Сколько часов вы сидите за компьютером?')
    await Test.next()


async def answer_q2(message: types.message, state: FSMContext, db: Database):
    # Достаем переменные
    data = await state.get_data()  # тут хранится весь словарь состояний
    answer1 = data.get('answer1')
    answer2 = message.text

    await message.answer('Спасибо за ответы на вопросы)')
    if (int(answer1) >= 20 and int(answer2) >= 12):
        await message.answer('Капец! как можно так долго сидеть за компом?\n'
                             'Ты уже не молодой')
    elif (int(answer1) >= 20 and int(answer2) >= 6):
        await message.answer('Ну в теории нормально')
    elif (int(answer1) < 20 and int(answer2) >= 12):
        await message.answer('Ты еще молодой, иди отдыхай!')
    elif (int(answer1) < 20 and int(answer2) >= 6):
        await message.answer('Ну так-то нрормально сидишь')
    else:
        await message.answer('Нифига ты кацфушник)))')
    # После завершени я теста нужно стереть у пользователя его СОСТОЯНИЕ
    # Вариант 1
    y = [int(answer1), int(answer2)]

    await state.finish()

    # Вариант 2
    # await state.reset_state()

    # если хочу стереть только состояние, без стриания данных внутри(словари, списки. ответы), то делаем
    # await state.reset_state(with_data=False)


async def save_info(message: types.Message, state: FSMContext):
    await state.update_data(some_info='some info')
    data = await state.get_data()
    some_info = data.get('some_info')


def register_testing(dp: Dispatcher):
    dp.register_message_handler(enter_test, commands=['test'], state=None)
    dp.register_message_handler(answer_q1, state=Test.Q1)
    dp.register_message_handler(answer_q2, state=Test.Q2)

# если захочу попасть в любое состояние, то пишу state='*'

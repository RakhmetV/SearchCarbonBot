import asyncio
import random
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from datetime import datetime

from tgbot.handlers.message import district_name
from tgbot.keyboards.inline import acquaintance_bot, description_Nikita, description_Gulya, description_Yana, \
    description_Timyr, description_add_hero, description_eco, carbon_footprint
from tgbot.keyboards.inline_college import district_rt, college_inline_keyboard
from tgbot.services.db import Database
from tgbot.states.test import Data

db = Database('database.db')


async def start_bot(call: CallbackQuery):
    await call.answer(cache_time=5)
    await call.message.answer('Для начала познакомимся с командой☺', reply_markup=acquaintance_bot)


async def acquaintance_fun(call: CallbackQuery):
    await call.answer(cache_time=5)
    await call.message.answer_sticker(
        sticker='CAACAgIAAxkBAAIKTWMf886YA250jvZ3xIDnpWTEg6cOAAIqIAACOUcBSbK3nTPwlyI5KQQ')
    await call.message.answer('Меня зовут Никита\n\n'
                              'Меня увлекают изобретения и разные отрасли промышленности🏭\n'
                              'Когда-нибудь я создам что-то полезное для всей планеты!\n\n'
                              'Только вот что именно создать? И кого позвать в команду?\n\n'
                              'Ладно, разберёмся вместе🖐!',
                              reply_markup=description_Nikita)


async def helloNikita(call: CallbackQuery):
    await call.answer(cache_time=5)
    await call.message.answer_sticker(
        sticker='CAACAgIAAxkBAAIKS2Mf88xGkMUD0B0tJ25Mo7k5z-aJAAIJGwACgmMAAUkeOIwi7tLzgykE')

    await call.message.answer('Привет, Никита! Привет всем! Я Гуля 😊\n\n'
                              'Я люблю придумывать всякие полезные проекты. '
                              'Никите нужна была помощь с тем, чтобы создать что-то новое, '
                              'и я решила ему помочь. Никита любит изобретать, '
                              'а я — организовать.\n\n'
                              'Но мы не могли придумать тему для нашего нового проекта🤔',
                              reply_markup=description_Gulya)


async def helloGulya(call: CallbackQuery):
    await call.answer(cache_time=5)
    await call.message.answer_sticker(
        sticker='CAACAgIAAxkBAAIKT2Mf89BmctGgxDyZ-4kr4n9KxmfkAAIpKQACJ8IAAUlkK54XjzwGvikE')

    await call.message.answer('Привет, я Яна✌🏻\n\n'
                              'Я увлекаюсь экологией, знаю много эко-привычек.🌿\n\n'
                              'Вот недавно мы встретились с Гулей и Никитой в парке. '
                              'Им нужна была тема для нового проекта.\n\n'
                              'Я им предложила создать проект '
                              'по экологии, ведь это то, в чем я отлично '
                              'разбираюсь!',
                              reply_markup=description_Yana)


async def helloYana(call: CallbackQuery):
    await call.answer(cache_time=5)
    await call.message.answer('У нас есть классная тема, команда из организатора, изобретателя '
                              'и эколога. Но нам кого-то еще не хватает🤔')
    await asyncio.sleep(3)
    await call.message.answer_sticker(sticker='CAACAgIAAxkBAAIKSWMf88q62Tq38G5ROUkDRDQipQXBAALZHwACPicBSXADhHQ3AuSOKQQ')
    await call.message.answer('Привет, я Тимур👋🏻\n\n'
                              'Я увлекаюсь наукой, в будущем я точно стану ученым.'
                              ' Кстати, лучший способ узнать что-то новое или создать '
                              'свой проект — это исследование🔍\n\n'
                              'Яна пригласила меня в '
                              'команду, и я им предложил сделать формат проекта '
                              'исследовательским. То есть, мы сами будем получать '
                              'новые знания!⚡️',
                              reply_markup=description_Timyr)


async def helloTimyr(call: CallbackQuery):
    await call.answer(cache_time=5)
    await call.message.answer('Нас четверо, но в команде должно быть пятеро\n\n'
                              'Присоединишься к нашей команде?', reply_markup=description_add_hero)


async def addNewHero(call: CallbackQuery):
    await call.answer(cache_time=5)
    await call.message.answer('У нашего исследования есть свой секретный код.🔐\n\n'
                              'Спроси его у организатора')
    await Data.Password.set()


async def checkPassword(message: types.Message, state: FSMContext):
    data = await state.get_data()  # тут хранится весь словарь состояний
    if not bool(data.get('password')):
        if message.text == 'фотосинтез' or message.text == 'Фотосинтез':
            await message.answer('Верно: ты прошел проверку!')
            await asyncio.sleep(3)

            await message.answer('Давай заполним анкету члена нашей команды✌🏻')
            await asyncio.sleep(3)
            await message.answer('Как тебя зовут? (напиши свое Имя)')
            await Data.next()
        else:
            await message.answer('Ты ввел неправильный код')


async def answer_name(message: types.Message, state: FSMContext):
    data = await state.get_data()  # тут хранится весь словарь состояний
    if not bool(data.get('name')):
        nowdate = datetime.now()
        newdate = nowdate.strftime("%d/%m/%Y")

        answer = message.text
        await state.update_data(name=message.text)
        db.add_user(message.from_user.id, answer, newdate)

        await message.answer(f'Приятно познакомиться, {answer}🥰')
        await asyncio.sleep(4)
        await message.answer(
            'Из какого ты района Республики Татарстан?', reply_markup=district_rt)
        await Data.next()


async def answer_district(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=5)
    db.set_district(call.message.chat.id, district_name[call.data.split(':')[1]])
    await call.message.answer('Выбери свое учебное заведение🏫',
                              reply_markup=college_inline_keyboard[call.data.split(':')[1]])
    await Data.next()


async def answer_college(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=5)
    db.set_college(call.message.chat.id, call.data.split(':')[1])
    await call.message.answer('Напиши несколько своих увлечений в одном предложении🎨🏀')
    await Data.next()


async def answer_hobbies(message: types.Message, state: FSMContext):
    # добавить увлечения в базу данных
    if len(message.text) <= 150:
        db.set_hobby(message.from_user.id, message.text)
        await message.answer('Какой предмет в школе ты больше всего любишь?📚')
        await Data.next()
    else:
        await message.answer(f'Количество символов не должно превышать 150\n'
                             f'Количество ваших символов: {len(message.text)}')


async def answer_favorite_sub(message: types.Message, state: FSMContext):
    if len(message.text) <= 50:
        db.set_favorite_subject(message.from_user.id, message.text)
        await Data.next()
        await message.answer('Интересуешься ли ты экологией🌳?', reply_markup=description_eco)
    else:
        await message.answer(f'Количество символов не должно превышать 150\n'
                             f'Количество ваших символов: {len(message.text)}')


async def data_coll_one(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=5)
    db.set_interest_ecology(call.message.chat.id, call.data.split(':')[1])
    await state.finish()

    await call.message.answer('Слышал ли ты когда нибудь об углеродном следе?👣',
                              reply_markup=carbon_footprint)


def register_data_collection(dp: Dispatcher):
    dp.register_callback_query_handler(start_bot, text_contains='start', state=None)

    dp.register_callback_query_handler(acquaintance_fun, text_contains='acquaintance', state=None)
    dp.register_callback_query_handler(helloNikita, text_contains='helloNikita', state=None)
    dp.register_callback_query_handler(helloGulya, text_contains='helloGulya', state=None)
    dp.register_callback_query_handler(helloYana, text_contains='helloYana', state=None)
    dp.register_callback_query_handler(helloTimyr, text_contains='helloTimyr', state=None)
    dp.register_callback_query_handler(addNewHero, text_contains='AddUserInComand', state=None)
    dp.register_message_handler(checkPassword, state=Data.Password)
    dp.register_message_handler(answer_name, state=Data.Name)
    dp.register_callback_query_handler(answer_district, text_contains='district', state=Data.District)
    dp.register_callback_query_handler(answer_college, text_contains='college', state=Data.College)
    dp.register_message_handler(answer_hobbies, state=Data.Hobbies)
    dp.register_message_handler(answer_favorite_sub, state=Data.Favorite_subject)
    dp.register_callback_query_handler(data_coll_one, text_contains='ecoSearch', state=Data.Eco)

    # dp.register_message_handler(answer_education, state=Data.EducationalInstitution)
    # dp.register_callback_query_handler(inlinePasswordOne, text_contains='inlinePassOne',
    #                                    state=Data.EducationalInstitution)
    # dp.register_callback_query_handler(inlinePasswordTwo, text_contains='inlinePassTwo',
    #                                    state=Data.EducationalInstitution)
    #
    # dp.register_message_handler(answer_case_password, state=Data.PasswordCase)
    #
    # dp.register_callback_query_handler(inlinePasswordThree, text_contains='inlinePassThree',
    #                                    state=Data.PasswordCase)
    # dp.register_callback_query_handler(inlineIntecactiveThree, text_contains='inlineInteractOne',
    #                                    state=None)

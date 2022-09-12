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
    await call.message.answer('Для начала познакомимся с командой', reply_markup=acquaintance_bot)


async def acquaintance_fun(call: CallbackQuery):
    await call.answer(cache_time=5)
    with open('nikita.png', 'rb') as photo:
        await call.message.answer_photo(photo,
                                        caption='Меня зовут Никита\n\nМеня увлекают изобретения и разные отрасли промышленности. '
                                                'Когда-нибудь я создам что-то полезное для всей планеты! Только вот что именно создать? И кого позвать в команду? Ладно, разберёмся вместе!',
                                        reply_markup=description_Nikita)


async def helloNikita(call: CallbackQuery):
    await call.answer(cache_time=5)
    with open('gulya.png', 'rb') as photo:
        await call.message.answer_photo(photo, caption='Привет, Никита! Привет всем! Я Гуля\n\n'
                                                       'Я люблю придумывать всякие полезные проекты. '
                                                       'Никите нужна была помощь с тем, чтобы создать что-то новое,'
                                                       ' и я решила ему помочь. Никита любит изобретать, а я —'
                                                       ' организовать. Но мы не могли придумать тему для нашего '
                                                       'нового проекта.',
                                        reply_markup=description_Gulya)


async def helloGulya(call: CallbackQuery):
    await call.answer(cache_time=5)
    with open('yana.png', 'rb') as photo:
        await call.message.answer_photo(photo, caption='Привет, я Яна\n\n'
                                                       'Я увлекаюсь экологией, знаю много эко-привычек. '
                                                       'Вот недавно мы встретились с Гулей и Никитой в парке. '
                                                       'Им нужна была тема для нового проекта. Я им предложила '
                                                       'создать проект по экологии, ведь это то, в чем я отлично '
                                                       'разбираюсь!',
                                        reply_markup=description_Yana)


async def helloYana(call: CallbackQuery):
    await call.answer(cache_time=5)
    await call.message.answer('У нас есть классная тема, команда из организатора, изобретателя '
                              'и эколога. Но нам кого-то еще не хватает')
    await asyncio.sleep(1)

    with open('timur.png', 'rb') as photo:
        await call.message.answer_photo(photo, caption='Привет, я Тимур\n\n'
                                                       'Я увлекаюсь наукой, в будущем я точно стану ученым.'
                                                       ' Кстати, лучший способ узнать что-то новое или создать '
                                                       'свой проект — это исследование. Яна пригласила меня в '
                                                       'команду, и я им предложил сделать формат проекта '
                                                       'исследовательским. То есть, мы сами будем получать '
                                                       'новые знания!',
                                        reply_markup=description_Timyr)


async def helloTimyr(call: CallbackQuery):
    await call.answer(cache_time=5)
    await call.message.answer('Нас четверо, но в команде должно быть пятеро\n\n'
                              'Присоединишься к нашей команде?', reply_markup=description_add_hero)
    await asyncio.sleep(1)


async def addNewHero(call: CallbackQuery):
    await call.answer(cache_time=5)
    await call.message.answer('У нашего исследования есть свой секретный код. Спроси его у организатора')
    await Data.Password.set()


async def checkPassword(message: types.Message, state: FSMContext):
    data = await state.get_data()  # тут хранится весь словарь состояний
    if not bool(data.get('password')):
        if message.text == 'фотосинтез':
            await message.answer('Верно: ты прошел проверку!')
            await asyncio.sleep(1)

            await message.answer('Давай заполним анкету члена нашей команды✌🏻')
            await asyncio.sleep(1)
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
        await asyncio.sleep(1)
        await message.answer(
            'Из какого ты района Республики Татарстан?', reply_markup=district_rt)
        await Data.next()


async def answer_district(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=5)
    db.set_district(call.message.chat.id, district_name[call.data.split(':')[1]])
    await call.message.answer('Выбери свое учебное заведение',
                              reply_markup=college_inline_keyboard[call.data.split(':')[1]])
    await Data.next()


async def answer_college(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=5)
    db.set_college(call.message.chat.id, call.data.split(':')[1])
    await call.message.answer('Напиши несколько своих увлечений в одном предложении')
    await Data.next()


async def answer_hobbies(message: types.Message, state: FSMContext):
    # добавить увлечения в базу данных
    if len(message.text) <= 150:
        db.set_hobby(message.from_user.id, message.text)
        await message.answer('Какой предмет в школе ты больше всего любишь?')
        await Data.next()
    else:
        await message.answer(f'Количество символов не должно превышать 150\n'
                             f'Количество ваших символов: {len(message.text)}')


async def answer_favorite_sub(message: types.Message, state: FSMContext):
    if len(message.text) <= 50:
        db.set_favorite_subject(message.from_user.id, message.text)

        await message.answer('Интересуешься ли ты экологией?', reply_markup=description_eco)
        await Data.next()
    else:
        await message.answer(f'Количество символов не должно превышать 150\n'
                             f'Количество ваших символов: {len(message.text)}')


async def answer_eco(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=5)
    db.set_interest_ecology(call.message.chat.id, call.data.split(':')[1])
    await call.message.answer('Отлично, ты в нашей команде!')
    await asyncio.sleep(1)
    await call.message.answer('Слышал ли ты когда нибудь об углеродном следе?',
                              reply_markup=carbon_footprint)
    await state.finish()


# async def answer_education(message: types.Message, state: FSMContext):
#     data = await state.get_data()  # тут хранится весь словарь состояний
#     if not bool(data.get('college')):
#         answer = message.text
#         if len(answer) > 60:
#             await message.answer(f'Количество допустимых символов: 60\nКоличество ваших символов: {len(answer)}')
#             await asyncio.sleep(1)
#             await message.answer(f'Сократите название')
#         else:
#             await state.update_data(college=answer)
#             await asyncio.sleep(1)
#
#             await message.answer('Перед тем, как начать исследование, мы разделимся на команды')
#             await asyncio.sleep(1)
#
#             await message.answer('Попроси у организатора пароль')
#             await asyncio.sleep(1)
#
#             await message.answer('Получил?', reply_markup=inline_password_one)
#             await asyncio.sleep(1)
#
#
# async def inlinePasswordOne(call: CallbackQuery, state: FSMContext):
#     await call.message.answer('Ты получил название химического вещества⚛')
#     await asyncio.sleep(1)
#
#     await call.message.answer('Теперь найди формулу данного вещества, покажи модератору данную формулу и сверься')
#     await asyncio.sleep(1)
#
#     await call.message.answer('Нашел формулу данного вещества?', reply_markup=inline_password_two)
#     await asyncio.sleep(1)
#
#
# async def inlinePasswordTwo(call: CallbackQuery, state: FSMContext):
#     await call.message.answer('Данная формула вещества будет являться паролем')
#     await asyncio.sleep(1)
#
#     await call.message.answer('Введи пароль (Заглавными буквами и английским шрифтом)')
#     await Data.next()
#
#
# async def answer_case_password(message: types.Message, state: FSMContext):
#     answer = message.text
#     await state.update_data(password_case=answer)
#     db = Database('database.db')
#     nowdate = datetime.now()
#     newdate = nowdate.strftime("%d/%m/%Y")
#     if answer in team_selection:
#         data = await state.get_data()  # тут хранится весь словарь состояний
#         name = data.get('name')
#         college = data.get('college')
#         db.add_user(message.from_user.id,
#                     name,
#                     college,
#                     newdate,
#                     team_selection[answer]
#                     )  # добавляем нового пользователя
#
#         variant = random.randint(0, 9)
#         if db.counting_variant_case(team_selection[answer], newdate)[0][0] > 10:
#             await message.answer(f'Количество людей в этой команде превысило 10\n'
#                                  f'Пожалуйста, попробуйте другой пароль')
#         else:
#             check = False
#             while db.check_variant(newdate, team_selection[answer], variant):
#                 if db.counting_variant_case(team_selection[answer], newdate)[0][0] > 10:
#                     check = True
#                     break
#                 else:
#                     variant = random.randint(0, 9)
#
#             if check:
#                 await message.answer(
#                     f'Количество людей в этой команде превысило 10\nПожалуйста, попробуйте другой пароль')
#             else:
#                 db.set_variant(message.from_user.id, variant)
#                 await message.answer(f'Вы в команде под номером {team_selection[answer]} 🙌')
#                 await asyncio.sleep(1)
#
#                 await message.answer(f'Узнай у организатора, в той ли ты команде сидишь сейчас\n\n'
#                                      f'Если в той, оставайся на местах. Если ты в другой команде, пересядь')
#                 await asyncio.sleep(1)
#
#                 await message.answer('Нашел свою команду?', reply_markup=inline_password_three)
#                 await asyncio.sleep(1)
#
#                 # await message.answer(f'Супер, ты получаешь исследование по теме <b>{team_name[variant]}</b>',
#                 #                      parse_mode='HTML')
#                 # await asyncio.sleep(1)
#                 #
#                 # await state.finish()  # очищаем позицию
#                 # await message.answer('Назови тему исследования организатору. Он выдаст тебе набор для исследования')
#                 # await asyncio.sleep(3)
#                 # await message.answer('Как тебе набор?', reply_markup=likeTheSet)
#     else:
#         await message.answer('Вы ввели неправильный пароль. Введите пароль снова')
#
#
# async def inlinePasswordThree(call: CallbackQuery, state: FSMContext):
#     db = Database('database.db')
#     variant = db.get_variant(call.message.chat.id)
#
#     await call.message.answer('Отлично!')
#     await asyncio.sleep(1)
#
#     await call.message.answer(f'Сегодня ты будешь проводить исследование по теме <b>{team_name[variant[0][0]]}</b>',
#                               parse_mode='HTML')
#     await asyncio.sleep(1)
#
#     await call.message.answer(
#         'Назови тему исследования организатору. '
#         'Он выдаст тебе персональный чемоданчик для исследования')
#     await asyncio.sleep(1)
#
#     await call.message.answer('Получил чемоданчик?', reply_markup=inline_interaction_one)
#     await asyncio.sleep(1)
#
#     await state.finish()  # очищаем позицию
#
#
# async def inlineIntecactiveThree(call: CallbackQuery):
#     await call.message.answer('Как тебе набор?', reply_markup=inline_interaction_two)


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
    dp.register_callback_query_handler(answer_eco, text_contains='ecoSearch', state=Data.Eco)

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

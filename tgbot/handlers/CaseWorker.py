import asyncio
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from tgbot.keyboards.inline import researchesStart, carbon_footprint, carbonFootprintTest, carbonFootprintAnswer, \
    carbon_heard, carbon_greenhouse_effect, carbon_understand, carbon_bulochka
from tgbot.services.db import Database
from tgbot.states.test import Data

db = Database('database.db')
async def carbon_footprint_info(call: CallbackQuery):
    await call.answer(cache_time=5)
    await call.message.answer('Я очень рад, что тебе понравился чемоданчик\n\n'
                              'Но сперва мы изучим тему нашего исследования👨‍🏫👩‍🏫')
    await asyncio.sleep(3)

    await call.message.answer('Углеродный след👣 - это совокупность всех парниковых газов💨, '
                              'которые попадают в окружающую среду от деятельности людей, '
                              'организаций, компаний, городов и стран')
    await asyncio.sleep(7)

    await call.message.answer('В состав парниковых газов входит:\n\n'
                              '•углекислый газ СО2\n'
                              '•метан СН4\n'
                              '•закись азота N2O\n'
                              '•водяной пар Н2О\n'
                              '•фторированные газы\n')
    await asyncio.sleep(6)

    await call.message.answer('Слышал про данные газы?', reply_markup=carbon_heard)




async def carbon_Heard(call: CallbackQuery):
    await call.answer(cache_time=5)
    await call.message.answer(
        'Так как большая часть парникового газа состоит из СО2 (80 %), то след называют углеродным👣')
    await asyncio.sleep(5)

    await call.message.answer(
        'Сами по себе парниковые газы не несут вреда, но они усиливают'
        ' естественное явление - парниковый эффект')
    await asyncio.sleep(6)

    await call.message.answer(
        'Как ты думаешь, в чем суть парникового эффекта?🤔', reply_markup=carbon_greenhouse_effect)


async def carbon_Heard_answer(call: CallbackQuery):
    await call.answer(cache_time=5)
    await asyncio.sleep(2)
    if call.data.split(':')[1] == 'true':
        await call.message.answer(
            'Да, парниковый эффект позволяет поддерживать комфортную температуру для жизни на Земле')
        await asyncio.sleep(5)
    else:
        await call.message.answer(
            'Нет, на самом деле парниковый эффект позволяет '
            'поддерживать комфортную температуру для жизни🌍')
        await asyncio.sleep(6)

    await call.message.answer(
        'Но увеличение концентрации парниковых газов сопутствуют изменению климата на Земле')
    await asyncio.sleep(5)

    await call.message.answer(
        'Поэтому вопросы сохранения климата во всем мире являются важными для многих организаций и компаний☝')
    await asyncio.sleep(5)

    await call.message.answer('Давай повторим изученное:\n'
                              'Какой газ не входит в состав парниковых газов?', reply_markup=carbonFootprintTest)


async def carbon_footprint_test_answer(call: CallbackQuery):
    await call.answer(cache_time=5)
    if call.data.split(':')[1] == 'true':
        db.set_studying_topic_two(call.message.chat.id, 'H2S')
        await call.message.answer('Все верно, сернистый газ H2S  не входит в состав парниковых газов')
    else:
        db.set_studying_topic_two(call.message.chat.id, call.data.split(':')[1])
        await call.message.answer('Ошибочка, на самом деле, сернистый газ H2S  не входит в состав парниковых газов')
    await asyncio.sleep(5)

    await call.message.answer('А еще углеродный след бывает прямым и косвенным. '
                              'Например, поездка на машине🚘, использование газа '
                              'для готовки еды - это прямые выбросы')
    await asyncio.sleep(6)

    await call.message.answer('А покупка игрушечной машины, которая производилась '
                              'на предприятии🏭, где использовалось тепло и электроэнергия '
                              'на изготовление игрушечной машины, а еще и ее доставка🚚 до '
                              'места продажи - это косвенные выбросы.')
    await asyncio.sleep(7)

    await call.message.answer('Давай проверим, какой из этих примеров '
                              'относится к прямому углеродному следу',
                              reply_markup=carbon_bulochka)



async def carbonBulka(call: CallbackQuery):
    await call.answer(cache_time=5)
    if call.data.split(':')[1] == 'true':
        db.set_studying_topic_three(call.message.chat.id, 'производство булочек с корицей')
        await call.message.answer('Ты хорошо освоил тему!')
    else:
        db.set_studying_topic_three(call.message.chat.id, 'покупка булочек с корицей местного производства')
        await call.message.answer('Правильный ответ - производство булочек с корицей')
    await asyncio.sleep(3)

    await call.message.answer('Мы с тобой изучили, что такое углеродный след и его виды, '
                              'а также разобрались в чем суть парникового эффекта😎')
    await asyncio.sleep(5)

    await call.message.answer('Теперь ты понял, что такое углеродный след?', reply_markup=carbon_understand)

async def carbonUnderstand(call: CallbackQuery):
    await call.answer(cache_time=5)
    db.set_studying_topic_four(call.message.chat.id, call.data.split(':')[1])
    await call.message.answer(
        'Если у тебя еще остались вопросы, обратись к организатору. Он ответит на все твои вопросы')
    await asyncio.sleep(5)

    await call.message.answer('Если мы оставляем углеродный след, то значит, '
                              'мы сами же можем сделать так, чтобы его было меньше.📉\n'
                              'Да, ведь?', reply_markup=carbonFootprintAnswer)


def register_case_worker(dp: Dispatcher):
    dp.register_callback_query_handler(carbon_footprint_info, text_contains='inlineInteractTwo', state=None)
    dp.register_callback_query_handler(carbon_Heard, text_contains='carbonheard', state=None)
    dp.register_callback_query_handler(carbon_Heard_answer, text_contains='greenhouse', state=None)
    dp.register_callback_query_handler(carbon_footprint_test_answer, text_contains='carbonTest', state=None)
    dp.register_callback_query_handler(carbonBulka, text_contains='bulochka', state=None)
    dp.register_callback_query_handler(carbonUnderstand, text_contains='carbonundestand', state=None)

import asyncio
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from aiogram.utils.markdown import hlink

from tgbot.handlers.message_variant import variant_text_twenty_four, variant_text_twenty_six, variant_text_twenty_five, \
    variant_text_twenty_seven
from tgbot.keyboards.inline_after_case import inline_after_case_one, inline_after_case_two, inline_after_case_three, \
    inline_after_case_four, inline_after_case_video
from tgbot.services.db import Database
from tgbot.states.test import AfterCasePass

db = Database('database.db')


async def after_case_one(call: CallbackQuery):
    await call.answer(cache_time=5)
    variant = db.get_variant(call.message.chat.id)[0][0]
    await call.message.answer(variant_text_twenty_four[variant])
    await asyncio.sleep(5)

    await call.message.answer(variant_text_twenty_five[variant])
    await asyncio.sleep(5)

    await call.message.answer(variant_text_twenty_six[variant])
    await asyncio.sleep(8)

    await call.message.answer(variant_text_twenty_seven[variant])
    await asyncio.sleep(5)


    await call.message.answer('Теперь поделись полученными знаниями с другими из команды ребятами\n\n'
                              'В этом поможет тебе организатор')
    await asyncio.sleep(5)

    await call.message.answer('После того, как задание будет выполнено, организатор вам скажет код🔐')
    await asyncio.sleep(5)

    await call.message.answer('Введи код')
    await AfterCasePass.Password.set()


async def after_case_two(message: types.Message, state: FSMContext):
    if message.text == 'конференция' or message.text == 'Конференция':
        await state.finish()
        await message.answer('Поздравляю🤩\n\n'
                             'Ты успешно прошел обучающее исследование '
                             '“В поисках углеродного следа” ')
        await asyncio.sleep(3)

        await message.answer('Теперь ты получаешь удостоверение '
                             '“Будущего исследователя”🕵️‍♀️🕵️‍♂️ и можешь '
                             'гордо нести данное звание', reply_markup=inline_after_case_one)
        await asyncio.sleep(5)
    else:
        await message.answer('Вы ввели неправильный пароль.\nПовторите снова')


async def after_case_three(call: CallbackQuery):
    await call.answer(cache_time=5)
    # стикер Тимура
    await call.message.answer_sticker(sticker='CAACAgIAAxkBAAIKSWMf88q62Tq38G5ROUkDRDQipQXBAALZHwACPicBSXADhHQ3AuSOKQQ')
    await call.message.answer('Нам было очень приятно проводить проект с тобой🙌\n\n'
                              'Ты отличный член команды, мы на время стали учеными '
                              'и изучили очень интересную тему путем исследования!')
    await asyncio.sleep(6)

    # стикер Яна
    await call.message.answer_sticker(
        sticker='CAACAgIAAxkBAAIKT2Mf89BmctGgxDyZ-4kr4n9KxmfkAAIpKQACJ8IAAUlkK54XjzwGvikE')
    await call.message.answer('Я очень рада, что сегодня мы освоили тему углеродного '
                              'следа и изучили эко-привычки, которую '
                              'можно внести в собственную жизнь☺️', reply_markup=inline_after_case_three)


async def after_case_four(call: CallbackQuery):
    await call.answer(cache_time=5)
    await call.message.answer_sticker(
        sticker='CAACAgIAAxkBAAIKS2Mf88xGkMUD0B0tJ25Mo7k5z-aJAAIJGwACgmMAAUkeOIwi7tLzgykE')
    await call.message.answer('Очень здорово, что мы собрались такой '
                              'командой и организовали экологический проект🌿\n\n '
                              'Каждый смог унести для себя что-то полезное!')

    await asyncio.sleep(5)

    await call.message.answer_sticker(
        sticker='CAACAgIAAxkBAAIKTWMf886YA250jvZ3xIDnpWTEg6cOAAIqIAACOUcBSbK3nTPwlyI5KQQ')

    await call.message.answer('Я всегда мечтал создать, что-то полезное '
                              'для нашей планеты. И сегодня это у нас получилось😊\n\n '
                              'Применив данные советы в жизнь, мы можем принести '
                              'пользу для Земли! Как же это здорово!')
    await asyncio.sleep(6)

    await call.message.answer(f'А что думаешь ты? какие остались у тебя '
                              f'впечатления от обучающего исследования?\n\n'
                              f'<i>(Напиши пару слов о мероприятии)</i>',
                              parse_mode='HTML')
    await AfterCasePass.FeedBack.set()


async def after_case_five(message: types.Message, state: FSMContext):
    if len(message.text) <= 250:
        await state.finish()
        db.set_feedback(message.from_user.id, message.text)
        await message.answer('Спасибо, что ты был сегодня с нами и прошел '
                             'обучающее исследование '
                             '“В поисках углеродного следа”💚', reply_markup=inline_after_case_two)
    else:
        await message.answer(f'Количество допустимых символов: 250\n'
                             f'Количество введенных символов: {len(message.text)}')


async def after_case_six(call: CallbackQuery):
    await call.answer(cache_time=5)
    db.set_status(call.message.chat.id, 1)
    await call.message.answer('Направляем тебе дальнейшую инструкцию!')
    await asyncio.sleep(2)

    await call.message.answer('Персональный чемоданчик остаётся у тебя😻\n\n '
                              'Плакат, бандана, комикс и полезный подарок '
                              'будут напоминать тебе об участии в обучающем '
                              'исследовании “В поисках углеродного следа”', reply_markup=inline_after_case_four)


async def after_case_seven(call: CallbackQuery):
    await call.answer(cache_time=5)
    await call.message.answer('Сейчас мы направим тебе перечень '
                              'полезных ссылок, с помощью которых '
                              'ты можешь узнать о многих интересных проектов💫')
    await asyncio.sleep(5)
    link_one = hlink('Обучающее-исследование', 'https://xn----7sbbbhlfabd2ae8a6adj1ca5a4fzb5g.xn--p1ai/')
    link_two = hlink('официальном сайте Благотворительного фонда “Татнефть', 'http://bf-tatneft.ru/fond/?1main')
    link_three = hlink('сайте Всероссийского образовательного проекта “Образ. будущего“', 'https://obrazbudu.ru/')
    link_four = hlink('сайте Интерактивного центра “Альметрика”', 'https://almetrika.ru/')
    await call.message.answer(f'Мы собрали для тебя полезные ссылки, лови!\n\n'
                              f'{link_one} - Сайт обучающего исследования “В поисках углеродного следа”.'
                              f'На этом сайте будут выкладываться все результаты исследования школьников из 7 районов '
                              f'Республики Татарстан, фото и видеоматериалы\n\n'
                              f'На {link_two}'
                              f'ты можешь ознакомиться со всеми программами и проектами БФ '
                              f'“Татнефть” и в последующем принять участие в них\n\n'
                              f'На {link_three} ты можешь следить за деятельностью проекта\n\n'
                              f'На {link_four} ты можешь смотреть расписание мастер-классов и научно-познавательных экскурсий',
                              disable_web_page_preview=True)
    await asyncio.sleep(5)
    await call.message.answer('Через несколько часов тебе придут видеоролики с лабораторными работами🔬')

    await asyncio.sleep(7200)  # тут 2 часа - 7200 с

    await call.message.answer('Еще раз привет😊\n\n'
                              ' Мы высылаем тебе 10 '
                              'лабораторных работ, при прохождении которых '
                              'ты приобретешь полезные эко-привычки и узнаешь, '
                              'как сократить углеродный след')
    await asyncio.sleep(5)

    await call.message.answer_video(video='BAACAgIAAxkBAAJS9GMh1Uzs_b45tPyyZC8Zq-KEv2TPAAKfHAACEHURSchjJ3fKot6MKQQ')
    await asyncio.sleep(5)

    await call.message.answer('Выбери из списка тему своего '
                              'исследования и посмотри по ней '
                              'лабораторную работу', reply_markup=inline_after_case_video)


async def after_case_video(call: CallbackQuery):
    await call.answer(cache_time=5)
    lab_number = call.data.split(':')[1]
    if lab_number == '1':
        await call.message.answer_video(
            video='BAACAgIAAxkBAAJS6WMh04kh9V3lp9Z0aybyHltSktcQAAKMHAACEHURSZpsQoOTeHRpKQQ',
            caption='Лабораторная работа №1\n\n'
                    'Ты узнаешь о том, как использовать многоразовый '
                    'складной стакан и снизить при помощи этого '
                    'углеродный след! 👣\n\n'
                    'В студии проекта Линаз и Никита')
    elif lab_number == '2':
        await call.message.answer_video(
            video='BAACAgIAAxkBAAJTIWMiEff7NI5JtPTdu_oW7uBi6ti9AALGHgACEHURSV-x3hz70S1CKQQ',
            caption='Лабораторная работа №2.1\n\n'
                    'В этой работе ты узнаешь, как с помощью энергии '
                    'солнца можно сократить углеродный след 👣\n\n'
                    'В студии проекта Линаз и Алия')
        await asyncio.sleep(3)
        await call.message.answer_video(
            video='BAACAgIAAxkBAAJTFmMiELozL535b7JEBi_wMLpMFn_rAALDHgACEHURSYxGIJM9QteJKQQ',
            caption='Лабораторная работа №2.2\n\n'
                    'Как обезопасить себя на дороге в тёмное время суток '
                    'и каким образом это уменьшить углеродный след 👣\n\n'
                    'В студии Алия и Никита')

    elif lab_number == '3':
        await call.message.answer_video(
            video='BAACAgIAAxkBAAJTDmMh5GF6yo8bcb3J8W4bOiRoIeNeAAIGHQACEHURSbu6hxo5V1eXKQQ',
            caption='Лабораторная работа №3\n\n'
                    'Ты узнаешь о том, как можно дать вещам вторую '
                    'жизнь и таким образом снизить углеродный след 👣\n\n'
                    'В студии проекта Алия и Никита')

    elif lab_number == '4':
        await call.message.answer_video(
            video='BAACAgIAAxkBAAJS_mMh14G03DJHb7Q0u1eSHfEOD-jYAAKoHAACEHURSZfh2HuHge3JKQQ',
            caption='Лабораторная работа №4\n\n'
                    'В этом видео мы расскажем о том, что такое аэратор '
                    'и как с его помощью снизить углеродный след👣\n\n'
                    'В студии проекта Никита и Алия')

    elif lab_number == '5':
        await call.message.answer_video(
            video='BAACAgIAAxkBAAJTFGMh6iKKVl5192Kv_yoBdDGGpdGfAAIrHQACEHURSY47EBmYJKPlKQQ',
            caption='Лабораторная работа №5\n\n'
                    'Ты узнаешь, почему важно использовать многоразовый '
                    'мешок для обуви и как это повлияет на углеродный след 👣\n\n'
                    'В студии проекта Алия и Никита')

    elif lab_number == '6':
        await call.message.answer_video(
            video='BAACAgIAAxkBAAJTEGMh51PHOTGxXP_l9_-7O1mTNbI8AAIiHQACEHURSecI6XrcGgmVKQQ',
            caption='Лабораторная работа №6\n\n'
                    'В чем преимущество силиконовых губок '
                    'от поролоновых? Именно это мы и расскажем!\n\n'
                    'В студии проекта Алия и Никита')

    elif lab_number == '7':
        await call.message.answer_video(
            video='BAACAgIAAxkBAAJTCmMh2y0zmm59fzF9edi_tiStA3PpAALBHAACEHURSS5LEHj0rF6LKQQ',
            caption='Лабораторная работа №7\n\n'
                    'Чем же отличаются эко-мешочки от полиэтиленовых и как их '
                    'применять при походе в магазин и как это поможет сократить '
                    'углеродный след  мы сейчас и расскажем!\n\n'
                    'В студии проекта Алия и Никита')

    elif lab_number == '8':
        await call.message.answer_video(
            video='BAACAgIAAxkBAAJTDGMh3HTRXoyhbcxqQU4YjbkheU4qAALNHAACEHURSRKSHAY517pUKQQ',
            caption='Лабораторная работа №8\n\n'
                    'Ты узнаешь о том, какая есть альтернатива '
                    'общественному и личному транспорту, которые '
                    'оставляют ощутимый углеродный след!\n\n'
                    'В студии проекта Линаз и Никита')

    elif lab_number == '9':
        await call.message.answer_video(
            video='BAACAgIAAxkBAAJTCGMh2VX5yCxZd4nWzdcW11iWYv5cAAKyHAACEHURSScqjjHgY5cyKQQ',
            caption='Лабораторная работа №9\n\n'
                    'Как заменить светильник (ночник) на что '
                    'то менее энергозатратное? Об этом мы Вам расскажем!\n\n'
                    'В студии проекта Алия и Никита')

    elif lab_number == '10':
        await call.message.answer_video(
            video='BAACAgIAAxkBAAJTEmMh59ZBAWDj0qex3Sd3v4B0NmIsAAIlHQACEHURSWj26GaDPdbgKQQ',
            caption='Лабораторная работа №10\n\n'
                    'ы узнаешь как заменить поход на фитнес занятиями '
                    'на природе и как это повлияет на углеродный след!👣\n\n'
                    'В студии Алия и Линаз')


def register_after_the_case(dp: Dispatcher):
    dp.register_callback_query_handler(after_case_one, text_contains='inlineVarCaseSix', state=None)
    dp.register_message_handler(after_case_two, state=AfterCasePass.Password)
    dp.register_callback_query_handler(after_case_three, text_contains='AfterCaseOne', state=None)
    dp.register_callback_query_handler(after_case_four, text_contains='AfterCaseThree', state=None)
    dp.register_message_handler(after_case_five, state=AfterCasePass.FeedBack)
    dp.register_callback_query_handler(after_case_six, text_contains='AfterCaseTwo', state=None)
    dp.register_callback_query_handler(after_case_seven, text_contains='AfterCaseFour', state=None)
    dp.register_callback_query_handler(after_case_video, text_contains='AfterCaseVideo', state=None)

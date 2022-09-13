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
    await asyncio.sleep(2)
    variant = db.get_variant(call.message.chat.id)[0][0]
    await call.message.answer(variant_text_twenty_four[variant])
    await asyncio.sleep(5)

    await call.message.answer(variant_text_twenty_five[variant])
    await asyncio.sleep(5)

    await call.message.answer(variant_text_twenty_six[variant])
    await asyncio.sleep(5)

    await call.message.answer(variant_text_twenty_seven[variant])
    await asyncio.sleep(5)


    await call.message.answer('Теперь поделись полученными знаниями с другими из команды ребятами\n\n'
                              'В этом поможет тебе организатор')
    await asyncio.sleep(5)

    await call.message.answer('После того, как задание будет выполнено, организатор вам скажет код')
    await asyncio.sleep(5)

    await call.message.answer('Введи код')
    await AfterCasePass.Password.set()


async def after_case_two(message: types.Message, state: FSMContext):
    if message.text == 'конференция' or message.text == 'Конференция':
        await state.finish()
        await message.answer('Поздравляю!\n\n'
                             'Ты успешно прошел обучающее исследование '
                             '“В поисках углеродного следа” ')
        await asyncio.sleep(5)

        await message.answer('Теперь ты получаешь удостоверение '
                             '“будущего исследователя” и можешь '
                             'гордо нести данное звание', reply_markup=inline_after_case_one)
        await asyncio.sleep(5)
    else:
        await message.answer('Вы ввели неправильный пароль.\nПовторите снова')


async def after_case_three(call: CallbackQuery):
    await call.answer(cache_time=5)
    await call.message.answer('Нам было очень приятно проводить проект с тобой!\n\n'
                              'Ты отличный член команды, мы на время стали учеными '
                              'и изучили очень интересную тему путем исследования!')
    # стикер Тимура
    await call.message.answer_sticker(sticker='CAACAgIAAxkBAAIKSWMf88q62Tq38G5ROUkDRDQipQXBAALZHwACPicBSXADhHQ3AuSOKQQ')
    await asyncio.sleep(6)


    await call.message.answer('Я очень рада, что сегодня мы освоили тему углеродного '
                              'следа и изучили эко-привычки, которую '
                              'можно внести в собственную жизнь', reply_markup=inline_after_case_three)
    # стикер Яна
    await call.message.answer_sticker(sticker='CAACAgIAAxkBAAIKT2Mf89BmctGgxDyZ-4kr4n9KxmfkAAIpKQACJ8IAAUlkK54XjzwGvikE')
    await asyncio.sleep(6)


async def after_case_four(call: CallbackQuery):
    await call.answer(cache_time=5)
    await call.message.answer('Очень здорово, что мы собрались такой '
                              'командой и организовали экологический проект. '
                              'Каждый смог унести для себя что-то полезное!')

    await call.message.answer_sticker(
        sticker='CAACAgIAAxkBAAIKS2Mf88xGkMUD0B0tJ25Mo7k5z-aJAAIJGwACgmMAAUkeOIwi7tLzgykE')
    await asyncio.sleep(6)
    await call.message.answer('Я всегда мечтал создать, что-то полезное '
                              'для нашей планеты. И сегодня это у нас получилось! '
                              'Применив данные советы в жизнь, мы можем принести '
                              'пользу для Земли! Как же это здорово!')
    await call.message.answer_sticker(
        sticker='CAACAgIAAxkBAAIKTWMf886YA250jvZ3xIDnpWTEg6cOAAIqIAACOUcBSbK3nTPwlyI5KQQ')
    await asyncio.sleep(6)
    await call.message.answer('А что думаешь ты? какие остались у тебя '
                              'впечатления от обучающего исследования? '
                              '(напиши пару слов о мероприятии)')
    await AfterCasePass.FeedBack.set()


async def after_case_five(message: types.Message, state: FSMContext):
    if len(message.text) <= 250:
        await state.finish()
        db.set_feedback(message.from_user.id, message.text)
        await asyncio.sleep(2)
        await message.answer('Спасибо, что ты был сегодня с нами и прошел '
                             'обучающее исследование '
                             '“В поисках углеродного следа”', reply_markup=inline_after_case_two)
    else:
        await message.answer(f'Количество допустимых символов: 250\n'
                             f'Количество введенных символов: {len(message.text)}')


async def after_case_six(call: CallbackQuery):
    await call.answer(cache_time=5)
    db.set_status(call.message.chat.id, 1)
    await call.message.answer('Направляем тебе дальнейшую инструкцию!')
    await asyncio.sleep(5)

    await call.message.answer('Персональный чемоданчик остаётся у тебя. '
                              'Плакат, бандана, комикс и полезный подарок '
                              'будут напоминать тебе об участии в обучающем '
                              'исследовании “В поисках углеродного следа”', reply_markup=inline_after_case_four)


async def after_case_seven(call: CallbackQuery):
    await call.answer(cache_time=5)
    await asyncio.sleep(3)
    await call.message.answer('Сейчас мы направим тебе перечень '
                              'полезных ссылок, с помощью которых '
                              'ты можешь узнать о многих интересных проектов')
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

    await asyncio.sleep(7200)  # тут 2 часа - 7200 с

    await call.message.answer('Еще раз привет! Мы высылаем тебе 10 '
                              'лабораторных работ, при прохождении которых '
                              'ты приобретешь полезные эко-привычки и узнаешь, '
                              'как сократить углеродный след')
    await asyncio.sleep(10)

    await call.message.answer_video(video='BAACAgIAAxkBAAIO0mMfpJeKPKWoJ4B49nDgm4mRbVEVAAI4HQACkDkBSYSu39vwehxdKQQ')
    await asyncio.sleep(5)

    await call.message.answer('Выбери из списка тему своего '
                              'исследования и посмотри по ней '
                              'лабораторную работу', reply_markup=inline_after_case_video)


async def after_case_video(call: CallbackQuery):
    await call.answer(cache_time=5)
    lab_number = call.data.split(':')[1]
    if lab_number == '1':
        await call.message.answer_video(
            video='BAACAgIAAxkBAAIO32MfqhHapqEDlvyCowHDmO_lhG7LAAI7HQACkDkBSRhmwgABabRq8CkE',
            caption='Лабораторная работа №1\n\n'
                    'Ты узнаешь о том, как использовать многоразовый '
                    'складной стакан и снизить при помощи этого '
                    'углеродный след! 👣\n\n'
                    'В студии проекта Линаз и Никита')
    elif lab_number == '2':
        await call.message.answer_video(
            video='BAACAgIAAxkBAAIO8WMft06xE3WtV1h8fYyDbgRiQZyJAAJdHQACkDkBSQzmmYkXjL4mKQQ',
            caption='Лабораторная работа №2.1\n\n'
                    'В этой работе ты узнаешь, как с помощью энергии '
                    'солнца можно сократить углеродный след 👣\n\n'
                    'В студии проекта Линаз и Алия')
        await asyncio.sleep(3)
        await call.message.answer_video(
            video='BAACAgIAAxkBAAIO72Mfs36p5hxYE2zvWFi0I6tfYl6BAAJYHQACkDkBSWZ8m4qHOQuTKQQ',
            caption='Лабораторная работа №2.2\n\n'
                    'Как обезопасить себя на дороге в тёмное время суток '
                    'и каким образом это уменьшить углеродный след 👣\n\n'
                    'В студии Алия и Никита')

    elif lab_number == '3':
        await call.message.answer_video(
            video='BAACAgIAAxkBAAIO9WMfxJp8lQMRu_Du6D1Ll2bMceNEAAJoHQACkDkBSQl1X0Dr3e9gKQQ',
            caption='Лабораторная работа №3\n\n'
                    'Ты узнаешь о том, как можно дать вещам вторую '
                    'жизнь и таким образом снизить углеродный след 👣\n\n'
                    'В студии проекта Алия и Никита')

    elif lab_number == '4':
        await call.message.answer_video(
            video='BAACAgIAAxkBAAIO82MfvGQulSdjbiTFDDC3DbQWivB4AAJiHQACkDkBSawEd5CT3UuaKQQ',
            caption='Лабораторная работа №4\n\n'
                    'В этом видео мы расскажем о том, что такое аэратор '
                    'и как с его помощью снизить углеродный след👣\n\n'
                    'В студии проекта Никита и Алия')

    elif lab_number == '5':
        await call.message.answer_video(
            video='BAACAgIAAxkBAAIO7WMfsrVrmBpKVsfxFOeuujk3Pf2UAAJXHQACkDkBSQcUomSpJ99IKQQ',
            caption='Лабораторная работа №5\n\n'
                    'Ты узнаешь, почему важно использовать многоразовый '
                    'мешок для обуви и как это повлияет на углеродный след 👣\n\n'
                    'В студии проекта Алия и Никита')

    elif lab_number == '6':
        await call.message.answer_video(
            video='BAACAgIAAxkBAAIO6WMfsGc4JiZxQvWRs_76L1orVBtyAAJUHQACkDkBSbIFe4VxnrB4KQQ',
            caption='Лабораторная работа №6\n\n'
                    'В чем преимущество силиконовых губок '
                    'от поролоновых? Именно это мы и расскажем!\n\n'
                    'В студии проекта Алия и Никита')

    elif lab_number == '7':
        await call.message.answer_video(
            video='BAACAgIAAxkBAAIO42MfrJ8u9puCnzHxdFmdQRfNnHJgAAJKHQACkDkBST0WkJqE086RKQQ',
            caption='Лабораторная работа №7\n\n'
                    'Чем же отличаются эко-мешочки от полиэтиленовых и как их '
                    'применять при походе в магазин и как это поможет сократить '
                    'углеродный след  мы сейчас и расскажем!\n\n'
                    'В студии проекта Алия и Никита')

    elif lab_number == '8':
        await call.message.answer_video(
            video='BAACAgIAAxkBAAIO5WMfraG9RN61ThRF-G34chHBtCP6AAJNHQACkDkBSTxMmgpLcUSGKQQ',
            caption='Лабораторная работа №8\n\n'
                    'Ты узнаешь о том, какая есть альтернатива '
                    'общественному и личному транспорту, которые '
                    'оставляют ощутимый углеродный след!\n\n'
                    'В студии проекта Линаз и Никита')

    elif lab_number == '9':
        await call.message.answer_video(
            video='BAACAgIAAxkBAAIO4WMfqqMcUxhDvkYupL6Jax4XrjuFAAI8HQACkDkBSf6tRk8YYmNnKQQ',
            caption='Лабораторная работа №9\n\n'
                    'Как заменить светильник (ночник) на что '
                    'то менее энергозатратное? Об этом мы Вам расскажем!\n\n'
                    'В студии проекта Алия и Никита')

    elif lab_number == '10':
        await call.message.answer_video(
            video='BAACAgIAAxkBAAIO62MfsMlNQ931KVL_rqG6P63-YexfAAJWHQACkDkBSQHGdgcNoeytKQQ',
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

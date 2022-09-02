from aiogram import types, Dispatcher
from aiogram import Dispatcher as dp
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardRemove, CallbackQuery, InputFile

from tgbot.handlers.message import text_in_faculty_rus, text_in_faculty_eng
from tgbot.keyboards.inline import personal_account_keyboard_rus, personal_account_keyboard_eng
from tgbot.keyboards.keyboards_menu import keyboards_menu_faculty_rus, keyboards_menu_faculty_eng, \
    keyboards_menu_department_rus, keyboards_menu_department_eng, keyboards_main_menu_rus, keyboards_main_menu_eng, \
    keyboards_applicant_menu_rus, keyboards_applicant_menu_eng

language = ['rus']


async def show_menu_rus(call: CallbackQuery):
    await call.answer(cache_time=5)
    language.pop(0)
    language.append('rus')
    await call.message.answer(f'Привет!', reply_markup=keyboards_main_menu_rus)


async def show_menu_eng(call: CallbackQuery):
    await call.answer(cache_time=5)
    language.pop(0)
    language.append('eng')
    await call.message.answer(f'Hi!', reply_markup=keyboards_main_menu_eng)


# @dp.message_handler(text='ГНФ')
async def get_faculry(message: types.Message):
    if language[0] == 'rus':
        if message.text == 'Личный кабинет':
            await  message.answer(f'Для входа в личный кабинет студента <b>нажмите по ссылке</b>', parse_mode='HTML',
                                  reply_markup=personal_account_keyboard_rus)
        elif message.text == 'Абитуриенту':
            await  message.answer(f'Меню для абитуриента', parse_mode='HTML',
                                  reply_markup=keyboards_applicant_menu_rus)
        elif message.text == 'Язык':
            await  message.answer(f'Выберите язык/Select a language:', parse_mode='HTML',
                                  reply_markup=language_keyboard)
        elif message.text == 'Факультеты':
            await  message.answer('Факультеты', parse_mode='HTML', reply_markup=keyboards_menu_faculty_rus)
        elif message.text == 'Калькулятор ЕГЭ':
            await  message.answer('Для ознакомления своих возможностей для поступления перейдите по ссылке',
                                  parse_mode='HTML',
                                  reply_markup=use_keyboard_rus)
        elif message.text == 'Фото':
            photo = InputFile("first.png")
            await message.answer_photo(photo=photo)


        elif message.text == 'Меню':
            await  message.answer('Факультеты', parse_mode='HTML', reply_markup=keyboards_main_menu_rus)
        elif message.text in text_in_faculty_rus:
            mult = text_in_faculty_rus[message.text]
            await  message.answer(f'Вы выбрали кафедру:<b> {message.text}</b>\n{mult}', parse_mode='HTML',
                                  reply_markup=keyboards_menu_department_rus[message.text])
        # else:
        #     await  message.answer(f'Вы выбрали: {message.text}', parse_mode='HTML')
    else:

        if message.text == 'Personal account':
            await  message.answer(f'To log in to the student`s personal account <b>click on the link</b>',
                                  parse_mode='HTML',
                                  reply_markup=personal_account_keyboard_eng)
        elif message.text == 'To the applicant':
            await  message.answer(f'Menu for the applicant', parse_mode='HTML',
                                  reply_markup=keyboards_applicant_menu_eng)
        elif message.text == 'Language':
            await  message.answer(f'Выберите язык/Select a language:', parse_mode='HTML',
                                  reply_markup=language_keyboard)
        elif message.text == 'Faculty':
            await  message.answer('Faculty', parse_mode='HTML', reply_markup=keyboards_menu_faculty_eng)
        elif message.text == 'USE Calculator':
            await  message.answer('To familiarize yourself with your admission opportunities, follow the link',
                                  parse_mode='HTML',
                                  reply_markup=use_keyboard_eng)
        elif message.text == 'Menu':
            await  message.answer('Menu', parse_mode='HTML', reply_markup=keyboards_main_menu_eng)
        elif message.text in text_in_faculty_eng:
            mult = text_in_faculty_eng[message.text]
            await  message.answer(f'You have chosen the department:<b> {message.text}</b>\n{mult}', parse_mode='HTML',
                                  reply_markup=keyboards_menu_department_eng[message.text])
        # else:
        #     await  message.answer(f'You have chosen: {message.text}', parse_mode='HTML')


# await  message.answer(f'Вы выбрали факультет:<b> {message.text}</b>\nAAAAAAAAAAA', parse_mode='HTML',reply_markup=ReplyKeyboardRemove())

def register_menu(dp: Dispatcher):
    # dp.register_message_handler(show_menu, commands=['menu'])
    dp.register_callback_query_handler(show_menu_rus, text_contains='rus')
    dp.register_callback_query_handler(show_menu_eng, text_contains='eng')
    dp.register_message_handler(get_faculry)

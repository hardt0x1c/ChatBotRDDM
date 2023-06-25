import csv
import text.messages as msg
import keyboards.admin_keyboard as kb_admin
from config import *
from States.Admin import *
from aiogram import types
from aiogram.filters import Text
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove, FSInputFile
from loader import dp, bot, db


# Админ панель
@dp.message(Command('admin'))
async def admin(message: types.Message):
    if message.from_user.id == admin_id:
        await message.answer(msg.greet_admin, reply_markup=kb_admin.admin_panel)
    else:
        await message.answer(msg.no_permission, reply_markup=kb_admin.back_menu_inline)


# Обработка команды "Рассылка"
@dp.message(Text('🎙 Рассылка'))
async def send_spam(message: types.Message, state: FSMContext):
    if message.from_user.id == admin_id:
        await state.set_state(Admin.spam)
        await message.answer('Текст будет отправлен всем пользователям бота.', reply_markup=ReplyKeyboardRemove())
        await message.answer('Напиши текст рассылки и прикрепи фото, видео или гиф.\n'
                             'Но только одно!', reply_markup=kb_admin.back_menu_inline)
    else:
        await message.answer(msg.no_permission, reply_markup=kb_admin.back_menu_inline)


@dp.message(Admin.spam)
async def start_spam(message: types.Message, state: FSMContext):
    message_for_spam = message.html_text
    users = db.get_users()
    counter = 0
    errors = 0

    if types.ContentType.TEXT == message.content_type:  # Если админ отправил текст
        for i in range(len(users)):
            try:
                await bot.send_message(users[i][0], message_for_spam, parse_mode='html')
                counter += 1
            except Exception:
                errors += 1
                continue

        await message.answer(f'Рассылка завершена. Количество адресатов: {counter}',
                             reply_markup=kb_admin.back_menu_inline)
        await state.clear()

    elif types.ContentType.PHOTO == message.content_type:  # Если админ отправил фото
        for i in range(len(users)):
            try:
                await bot.send_photo(users[i][0],
                                     message.photo[-1].file_id,
                                     caption=message.html_text if message.caption else None,
                                     parse_mode='html'
                                     )
                counter += 1
            except Exception:
                errors += 1
                continue

        await message.answer(f'Рассылка завершена. Количество адресатов: {counter}',
                             reply_markup=kb_admin.back_menu_inline)
        await state.clear()

    elif types.ContentType.VIDEO == message.content_type:  # Если админ отправил видео
        for i in range(len(users)):
            try:
                await bot.send_video(users[i][0],
                                     message.video.file_id,
                                     caption=message.html_text if message.caption else None,
                                     parse_mode='html'
                                     )
                counter += 1
            except Exception:
                errors += 1
                continue

        await message.answer(f'Рассылка завершена. Количество адресатов: {counter}',
                             reply_markup=kb_admin.back_menu_inline)
        await state.clear()

    elif types.ContentType.ANIMATION == message.content_type:  # Если админ отправил gif
        for i in range(len(users)):
            try:
                await bot.send_animation(users[i][0],
                                         message.animation.file_id,
                                         caption=message.html_text if message.caption else None,
                                         parse_mode='html'
                                         )
                counter += 1
            except Exception:
                errors += 1
                continue

        await message.answer(f'Рассылка завершена. Количество адресатов: {counter}',
                             reply_markup=kb_admin.back_menu_inline)
        await state.clear()

    else:
        await message.answer('<b>❗️ Данный формат контента не поддерживается для рассылки!</b>')


# Обработка команды "Статистика"
@dp.message(Text('📊 Статистика'))
async def send_stats(message: types.Message):
    if message.from_user.id == admin_id:
        users = db.get_users()
        count = len(users)
        await message.answer(f'Количество подписчиков: {count}', reply_markup=kb_admin.back_menu_inline)
    else:
        await message.answer(msg.no_permission, reply_markup=kb_admin.back_menu_inline)


# Обработка команды "📜 Получить ответы пользователей на викторину"
@dp.message(Text('📜 Получить ответы пользователей на викторину'))
async def send_db(message: types.Message):
    if message.from_user.id == admin_id:
        await message.answer('Идет выгрузка ответов из БД')
        users_data = db.get_users_data()
        if users_data:
            # Путь до CSV файла
            csv_file = 'data/users_answers/users_data.csv'

            try:
                # Открываем файл на запись
                with open(csv_file, 'w', newline='') as file:
                    writer = csv.writer(file)

                    # Создаем заголовки
                    writer.writerow(
                        ['id', 'user_id', 'username', 'name', 'surname', 'first_question', 'second_question',
                         'third_question'])

                    # Заполняем столбцы
                    for row in users_data:
                        writer.writerow(row)
                file = FSInputFile(csv_file)
                await message.answer_document(file, caption='Файл успешно записан!')
            except Exception as ex:
                print(f"Ошибка записи в CSV: {ex}")
        else:
            await message.answer('Произошла ошибка: Не удалось взять данные из БД')
    else:
        await message.answer(msg.no_permission, reply_markup=kb_admin.back_menu_inline)


# Обработчик коллбека "в главное меню"
@dp.callback_query(Text('back_menu_inline'))
async def back_menu_inline(callback: types.CallbackQuery, state: FSMContext):
    if callback.from_user.id == admin_id:
        await state.clear()
        await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
        await callback.message.answer('Главное меню:', reply_markup=kb_admin.admin_panel)
    else:
        await state.clear()
        await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
        await callback.message.answer('Главное меню:', reply_markup=ReplyKeyboardRemove())

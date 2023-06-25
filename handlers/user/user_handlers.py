import text.messages as msg
import keyboards.user_keyboard as kb_user
from States.User import *
from aiogram import types
from aiogram.filters import Text
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile, ReplyKeyboardRemove
from loader import dp, db


# Обработка команды '/help'
@dp.message(Command('help'))
async def send_help(message: types.Message):
    await message.answer(msg.help)


# Обработчик команды '/start'
@dp.message(Command('start'))
async def start(message: types.Message):
    video = FSInputFile('data/videos/video.mp4')
    await message.answer_video(video=video, caption=msg.send_video)
    await message.answer(msg.greet, reply_markup=kb_user.start_button)


# Обработчик кнопки 'старт'
@dp.message(Text('Старт'))
async def send_first_location(message: types.Message, state: FSMContext):
    user = db.get_user(message.from_user.id)
    username = message.from_user.username
    if user is None:
        await message.answer(msg.registration)
        await message.answer(msg.registration_name)
        await state.set_state(User.get_name)
    else:
        await message.answer(f'Привет {username}!')
        await message.answer(msg.first_location, reply_markup=kb_user.here)


# Записываем имя пользователя
@dp.message(User.get_name)
async def get_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer(msg.registration_surname)
    await state.set_state(User.get_surname)


# Записываем фамилию пользователя и добавляем в БД
@dp.message(User.get_surname)
async def get_surname(message: types.Message, state: FSMContext):
    data = await state.get_data()
    name = data['name']
    surname = message.text
    # Если успешно то выводим сообщения об успешной регистрации и кнопку "Старт"
    if db.add_user(message.from_user.id, message.from_user.username, name, surname):
        await message.answer(msg.registration_success, reply_markup=kb_user.start_button)
        await state.clear()
    # Если неуспешно, то выводим сообщения об ошибке
    else:
        await message.answer(msg.registration_error)
        await state.clear()


# Обработка кнопки "Я на месте"
@dp.message(Text('Я на месте'))
async def first_location(message: types.Message):
    await message.answer(msg.first_location_success, parse_mode='html', reply_markup=kb_user.ready_button)


# Обработка кнопки "Готово"
@dp.message(Text('Готово'))
async def second_location(message: types.Message):
    await message.answer(msg.second_location, reply_markup=kb_user.ready_to_create)


# Обработка кнопки "Я готов творить"
@dp.message(Text('Я готов творить'))
async def third_location(message: types.Message):
    await message.answer(msg.third_location, parse_mode='html', reply_markup=kb_user.move_to_next_station)


# Обработка кнопки "Готов двигаться на следующую станцию"
@dp.message(Text('Готов двигаться на следующую станцию'))
async def four_location(message: types.Message):
    await message.answer(msg.four_location, reply_markup=kb_user.on_location)


# Обработка кнопки "Я пришел на локацию!"
@dp.message(Text('Я пришел на локацию!'))
async def five_location(message: types.Message):
    await message.answer(msg.five_location, reply_markup=kb_user.played_button)


# Обработка кнопки "Я сыграл!"
@dp.message(Text('Я сыграл!'))
async def six_location(message: types.Message):
    await message.answer(msg.six_location, reply_markup=kb_user.six_loc_ready_button)


# Обработка кнопки "Я готов!"
@dp.message(Text('Я готов!'))
async def seven_location(message: types.Message):
    await message.answer(msg.seven_location, reply_markup=kb_user.made_selfie)


# Обработка кнопки "Я сделал селфи!"
@dp.message(Text('Я сделал селфи!'))
async def eight_location(message: types.Message):
    await message.answer(msg.eight_location, reply_markup=kb_user.here_button)


# Обработка кнопки "Я на месте!"
@dp.message(Text('Я на месте!'))
async def nine_location(message: types.Message):
    await message.answer(msg.nine_location, reply_markup=kb_user.mission_complete)


# Обработка кнопки "Задание выполнено!"
@dp.message(Text('Задание выполнено!'))
async def ten_location(message: types.Message):
    await message.answer(msg.ten_location, parse_mode='html', reply_markup=kb_user.next_location)


# Обработка кнопки "Следующая локация"
@dp.message(Text('Следующая локация'))
async def eleven_location(message: types.Message):
    await message.answer(msg.eleven_location, parse_mode='html', reply_markup=kb_user.selfie_done)


# Обработки кнопки "Селфи готово"
@dp.message(Text('Селфи готово'))
async def twelve_location(message: types.Message):
    await message.answer(msg.twelve_location, reply_markup=kb_user.watch_video)


# Обработка кнопки "Смотреть видео"
@dp.message(Text('Смотреть видео'))
async def thirteen_location(message: types.Message):
    video = FSInputFile('data/videos/video2.mp4')
    await message.answer_video(video)
    await message.answer(msg.thirteen_location, reply_markup=kb_user.start_quiz)


# Обработка кнопки "Начать прохождение викторины"
@dp.message(Text('Начать прохождение викторины'))
async def fourteen_location_first_question(message: types.Message, state: FSMContext):
    await message.answer(msg.fourteen_location_first_question)
    await state.set_state(User.first_question)


# Записываем ответ на первый вопрос и идешь дальше
@dp.message(User.first_question)
async def fourteen_location_second_question(message: types.Message, state: FSMContext):
    await state.update_data(first_question=message.text)
    await message.answer(msg.fourteen_location_second_question)
    await state.set_state(User.second_question)


# Записываем ответ на второй вопрос и идем дальше
@dp.message(User.second_question)
async def fourteen_location_third_question(message: types.Message, state: FSMContext):
    await state.update_data(second_question=message.text)
    await message.answer(msg.fourteen_location_third_question)
    await state.set_state(User.third_question)


# Записываем ответ на третий вопрос и идем дальше
@dp.message(User.third_question)
async def fourteen_location_success(message: types.Message, state: FSMContext):
    data = await state.get_data()
    first_question = data['first_question']
    second_question = data['second_question']
    third_question = message.text
    user_id = message.from_user.id
    # Если запись в БД прошла успешно
    if db.add_questions(first_question, second_question, third_question, user_id):
        await message.answer(msg.fourteen_location_success, reply_markup=kb_user.meet)
        await state.clear()
    # Если запись в БД прошла неуспешно, то просто переходим к следующему шагу
    else:
        print(msg.fourteen_location_error)
        await message.answer(msg.fourteen_location_success, reply_markup=kb_user.meet)
        await state.clear()


# Обработка кнопки "Познакомиться"
@dp.message(Text('Познакомиться'))
async def fifteen_location(message: types.Message):
    await message.answer(msg.fifteen_location, reply_markup=ReplyKeyboardRemove())

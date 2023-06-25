from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup

start_button = [
    [KeyboardButton(text='Старт')]
]
start_button = ReplyKeyboardMarkup(keyboard=start_button, resize_keyboard=True)

here = [
    [KeyboardButton(text='Я на месте')]
]
here = ReplyKeyboardMarkup(keyboard=here, resize_keyboard=True)

ready_button = [
    [KeyboardButton(text='Готово')]
]
ready_button = ReplyKeyboardMarkup(keyboard=ready_button, resize_keyboard=True)

ready_to_create = [
    [KeyboardButton(text='Я готов творить')]
]
ready_to_create = ReplyKeyboardMarkup(keyboard=ready_to_create, resize_keyboard=True)

move_to_next_station = [
    [KeyboardButton(text='Готов двигаться на следующую станцию')]
]
move_to_next_station = ReplyKeyboardMarkup(keyboard=move_to_next_station, resize_keyboard=True)

on_location = [
    [KeyboardButton(text='Я пришел на локацию!')]
]
on_location = ReplyKeyboardMarkup(keyboard=on_location, resize_keyboard=True)

played_button = [
    [KeyboardButton(text='Я сыграл!')]
]
played_button = ReplyKeyboardMarkup(keyboard=played_button, resize_keyboard=True)

six_loc_ready_button = [
    [KeyboardButton(text='Я готов!')]
]
six_loc_ready_button = ReplyKeyboardMarkup(keyboard=six_loc_ready_button, resize_keyboard=True)

made_selfie = [
    [KeyboardButton(text='Я сделал селфи!')]
]
made_selfie = ReplyKeyboardMarkup(keyboard=made_selfie, resize_keyboard=True)

here_button = [
    [KeyboardButton(text='Я на месте!')]
]
here_button = ReplyKeyboardMarkup(keyboard=here_button, resize_keyboard=True)

mission_complete = [
    [KeyboardButton(text='Задание выполнено!')]
]
mission_complete = ReplyKeyboardMarkup(keyboard=mission_complete, resize_keyboard=True)

next_location = [
    [KeyboardButton(text='Следующая локация')]
]
next_location = ReplyKeyboardMarkup(keyboard=next_location, resize_keyboard=True)

selfie_done = [
    [KeyboardButton(text='Селфи готово')]
]
selfie_done = ReplyKeyboardMarkup(keyboard=selfie_done, resize_keyboard=True)

watch_video = [
    [KeyboardButton(text='Смотреть видео')]
]
watch_video = ReplyKeyboardMarkup(keyboard=watch_video, resize_keyboard=True)

start_quiz = [
    [KeyboardButton(text='Начать прохождение викторины')]
]
start_quiz = ReplyKeyboardMarkup(keyboard=start_quiz, resize_keyboard=True)

meet = [
    [KeyboardButton(text='Познакомиться')]
]
meet = ReplyKeyboardMarkup(keyboard=meet, resize_keyboard=True)

from aiogram.fsm.state import StatesGroup, State


class User(StatesGroup):
    get_name = State()
    get_surname = State()
    first_question = State()
    second_question = State()
    third_question = State()

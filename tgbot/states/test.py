from aiogram.dispatcher.filters.state import StatesGroup, State


class Test(StatesGroup):
    Q1 = State()
    Q2 = State()
    Q3 = State()
    Q4 = State()
    Q5 = State()
    Q6 = State()
    Q7 = State()

class Data(StatesGroup):
    Name = State()
    EducationalInstitution = State()
    PasswordCase = State()
    Q4 = State()
    Q5 = State()
    Q6 = State()
    Q7 = State()
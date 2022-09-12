from aiogram.dispatcher.filters.state import StatesGroup, State


class Test(StatesGroup):
    Q1 = State()
    Q2 = State()
    Q3 = State()
    Q4 = State()
    Q5 = State()


class Data(StatesGroup):
    Password = State()
    Name = State()
    District = State()
    College = State()
    Hobbies = State()
    Favorite_subject = State()
    Eco = State()


class DataPass(StatesGroup):
    CasePassword = State()


class InterPass(StatesGroup):
    InterPassword = State()


class DataCase(StatesGroup):
    Variant = State()
    QuestionOne = State()
    StateC = State()
    QuestionTwo = State()
    QuestionThree = State()
    QuestionFour = State()
    FeedBack = State()

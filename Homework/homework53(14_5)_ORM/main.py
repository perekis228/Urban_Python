from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from Keyboards import *
from crud_functions import *
import sqlite3
from aiogram.dispatcher import FSMContext
import asyncio

'''---------------------------Инфо+БД---------------------------'''
api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())
connection = sqlite3.connect('ForBot.db')
cursor = connection.cursor()
initiate_db(connection, cursor)

'''----------------------------Старт----------------------------'''
@dp.message_handler(commands=["start"])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb)

@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=in_kb)

@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5')
    await call.answer()

'''-----------------------Рассчёт калорий-----------------------'''
class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.callback_query_handler(text = 'calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()

@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=int(message.text))
    await message.answer('Введите свой рост:')
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=int(message.text))
    await message.answer('Введите свой вес:')
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=int(message.text))
    data = await state.get_data()
    await message.answer(f'Ваша норма калорий: {10 * data["weight"] + 6.25 * data["growth"] - 5 * data["age"] + 5}', reply_markup = kb)
    await state.finish()

'''---------------------------Покупка---------------------------'''
@dp.message_handler(text='Купить')
async def get_buying_list(message):
    products = get_all_products(cursor)
    for i in range(4):
        with open(f'Product{i+1}.png', 'rb') as img:
            await message.answer_photo(img, f'Название: {products[i][0]} | Описание: {products[i][1]} | Цена: {products[i][2]}')
    await message.answer('Выберите продукт для покупки:', reply_markup=buy_in_kb)

@dp.callback_query_handler(text='product_buying')
async def end_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()


'''-------------------------Регистрация-------------------------'''
class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = State()

@dp.message_handler(text = 'Регистрация')
async def sing_up(message):
    await message.answer('Введите имя пользователя (только латинский алфавит):')
    await RegistrationState.username.set()

@dp.message_handler(state=RegistrationState.username)
async def set_username(message, state):
    if is_included(cursor, message.text):
        await message.answer('Пользователь существует, введите другое имя.')
        await RegistrationState.username.set()
    else:
        await state.update_data(username=message.text)
        await message.answer('Введите свой email:')
        await RegistrationState.email.set()

@dp.message_handler(state=RegistrationState.email)
async def set_email(message, state):
    await state.update_data(email=message.text)
    await message.answer('Введите свой возраст:')
    await RegistrationState.age.set()

@dp.message_handler(state=RegistrationState.age)
async def set_age(message, state):
    await state.update_data(age=int(message.text))
    data = await state.get_data()
    add_user(cursor, connection, data['username'], data['email'], data['age'])
    await message.answer('Регистрация прошла успешно.', reply_markup = kb)
    await state.finish()

'''----------------------------Дефолт----------------------------'''
@dp.message_handler()
async def all_massages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

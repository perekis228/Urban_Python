from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Регистрация'),
         KeyboardButton(text='Рассчитать'),
         KeyboardButton(text='Информация'),
         KeyboardButton(text='Купить')]
    ],
    resize_keyboard=True
)

in_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')],
        [InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')]
    ],
    resize_keyboard=True
)

buy_in_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Product1', callback_data='product_buying')],
        [InlineKeyboardButton(text='Product2', callback_data='product_buying')],
        [InlineKeyboardButton(text='Product3', callback_data='product_buying')],
        [InlineKeyboardButton(text='Product4', callback_data='product_buying')]
    ],
    resize_keyboard=True
)
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="о боте"),
        KeyboardButton(text="помощь")],
        [KeyboardButton(text="информация о разработчике"),]
    ],
    resize_keyboard=True
)

yes_no_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="да"),
        KeyboardButton(text="нет")],
    ],
    resize_keyboard=True
)



yes_no_keyboard
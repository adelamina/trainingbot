from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_kb = InlineKeyboardMarkup(
    inline_keyboard=[
            [InlineKeyboardButton(text="Документация", url="docs.aiogram.dev")]
    ]
)


avtor_kb = InlineKeyboardMarkup(
    inline_keyboard=[
            [InlineKeyboardButton(text="Ссылка на twitch разраба", url="https://www.twitch.tv/adelamina123/about"),
            InlineKeyboardButton(text="Ссылка на github", url="https://github.com/adelamina/trainingbot")]
    ]
)



test_kb = InlineKeyboardMarkup(
    inline_keyboard=[
            [InlineKeyboardButton(text="test button", callback_data="test")]
    ]
)


#меню
menu11_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="о боте", callback_data="about11"),
        InlineKeyboardButton(text="помощь", callback_data="commands11")],
        [InlineKeyboardButton(text="еда", callback_data="food11"),
        InlineKeyboardButton(text="время сна", callback_data="sleep11")],
        [InlineKeyboardButton(text="информация о разработчике", callback_data="adelamina11")]
    ]
)


#о боте
aboutbot = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="назад", callback_data="back11")]
    ]
)

#помощь
helpbot = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="назад", callback_data="back22")]
    ]
)

#автор
avtorbot = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Ссылка на twitch разраба", url="https://www.twitch.tv/adelamina123/about"),
        InlineKeyboardButton(text="Ссылка на github", url="https://github.com/adelamina/trainingbot")],
        [InlineKeyboardButton(text="назад", callback_data="back33")]
    ]
)

#сон
sleepbot = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="назад", callback_data="back44")]
    ]
)

#еда
foodbot = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="назад", callback_data="back55")]
    ]
)

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
        InlineKeyboardButton(text="время сна", callback_data="sleep11"),
        InlineKeyboardButton(text="напоминание", callback_data="taimer")],
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
        [InlineKeyboardButton(text="оценка сна", callback_data="sleeptime")],
        [InlineKeyboardButton(text="назад", callback_data="back44")]
    ]
)

#еда
foodbot = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="3000ккал", callback_data="3000k"),
        InlineKeyboardButton(text="1500ккал", callback_data="1500k")],
        [InlineKeyboardButton(text="назад", callback_data="back55")]
    ]
)


#еда назад
forfood = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="назад", callback_data="back66")]
    ]
)




#оценка сна
sleeprate = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="6 - 12", callback_data="sleeprate11"),
        InlineKeyboardButton(text="13 - 18", callback_data="sleeprate22")],
        [InlineKeyboardButton(text="18 - 60", callback_data="sleeprate33"),
        InlineKeyboardButton(text="61+", callback_data="sleeprate44")],
        [InlineKeyboardButton(text="назад", callback_data="back77")]
    ]
)

sleeprate6 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="9 - 12", callback_data="sleeprate111")],
        [InlineKeyboardButton(text="больше", callback_data="sleeprate222"),
        InlineKeyboardButton(text="меньше", callback_data="sleeprate333")],
        [InlineKeyboardButton(text="назад", callback_data="back88")]
    ]
)


sleepmenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="меню", callback_data="menu99")]
    ]
)


sleeprate13 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="8 - 10", callback_data="sleeprate1111")],
        [InlineKeyboardButton(text="больше", callback_data="sleeprate2222"),
        InlineKeyboardButton(text="меньше", callback_data="sleeprate3333")],
        [InlineKeyboardButton(text="назад", callback_data="back111")]
    ]
)

sleeprate18 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="7 - 9", callback_data="sleeprate444")],
        [InlineKeyboardButton(text="больше", callback_data="sleeprate555"),
        InlineKeyboardButton(text="меньше", callback_data="sleeprate666")],
        [InlineKeyboardButton(text="назад", callback_data="back222")]
    ]
)


sleeprate61 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="7 - 8", callback_data="sleeprate777")],
        [InlineKeyboardButton(text="больше", callback_data="sleeprate888"),
        InlineKeyboardButton(text="меньше", callback_data="sleeprate999")],
        [InlineKeyboardButton(text="назад", callback_data="back999")]
    ]
)




taimer11 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="напоминалка на пол часа", callback_data="taimer111")],
        [InlineKeyboardButton(text="напоминалка на час", callback_data="taimer222"),
        InlineKeyboardButton(text="напоминалка на 2 часа", callback_data="taimer333")],
        [InlineKeyboardButton(text="назад", callback_data="back116")]
    ]
)


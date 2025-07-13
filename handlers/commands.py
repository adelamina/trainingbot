from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram import F
from keyboards.inline import start_kb, test_kb, avtor_kb, menu11_kb
from keyboards.reply import  keyboard


command_router = Router()


@command_router.message(Command("style"))
async def send_styles(message: Message):
    text = (
        "<b>bold</b> -- <strong>bold</strong>\n"
        "<i>italic</i> -- <em>italic</em>\n"
        "<u>underline</u> -- <ins>underline</ins>\n"
        "<s>strikethrough</s> -- <strike>strikethrough</strike> --  <del>strikethrough</del>\n"
        "<span class=\"tg-spoiler\">spoiler</span> -- <tg-spoiler>spoiler</tg-spoiler>\n"
        "<b>bold   <i>italic bold   <s>italic bold strikethrough "
        "<span class=\"tg-spoiler\">italic bold strikethrough spoiler</span>"
        "</s> <u>underline italic bold</u></i> bold</b>\n"
        "<a href=\"http://www.example.com/\">inline URL</a>\n"
        "<code>inline fixed-width code</code>\n"
        "<pre>pre-formatted fixed-width code block</pre>\n"
        "<pre><code class=\"language-python\">pre-formatted fixed-width code block written in the Python programming "
        "language</code></pre>"
    )
    await message.answer(text=text, parse_Mode="html")


@command_router.message(Command("menu"))
async def command_start_handler(message: Message) -> None:
    start_message = (f'Главное меню.')
    await message.answer(text=start_message, reply_markup=menu11_kb)    


@command_router.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    start_message = (f'Здравствуй друг')
    await message.answer(text=start_message, reply_markup=start_kb)


@command_router.message(Command("help"))
async def command_start_handler(message: Message) -> None:
    text = (f"Пропишите /menu чтобы начать")
    await message.answer(text)

@command_router.message(F.text.lower().contains('помощь'))
async def reply_heart(message: Message):
    await message.answer(text="всего 3 команды: ./help, ./about, ./start")

@command_router.message(F.text.lower().contains('информация о разработчике'))
async def reply_heart(message: Message):
    await message.answer(text="здесь ссылки автора:", reply_markup=avtor_kb)

    


    

@command_router.message(F.text.lower().contains('о боте'))
async def reply_heart(message: Message):
    await message.answer(text="Бот для тренировок, который сможет рассчитывать суточную норму калорий, будет напоминать о тренировках, который будет хранить данные о сне и оценивать их.")

@command_router.message(F.sticker)
async def handle_sticker(message: Message):
    await message.answer(text="Классный стикер!")

@command_router.message(F.photo)
async def handle_sticker(message: Message):
    await message.answer(text="Отличное фото!")




@command_router.message(F.text.lower().contains('пока'))
async def reply_goodbye(message: Message):
    await message.answer(text="До свидания!")


@command_router.message(F.text.lower().contains('привет'))
async def reply_hi(message: Message):
    await message.answer(text="Привет, как дела?")


@command_router.message(F.text.lower().contains('❤️'))
async def reply_heart(message: Message):
    await message.answer(text="Спасибо за сердечко!")


@command_router.message(F.text.lower().contains('плохо'))
async def reply_heart(message: Message):
    await message.answer(text="👎")


@command_router.message(F.text.lower().contains('хорошо'))
async def reply_heart(message: Message):
    await message.answer(text="👍")



@command_router.message()
async def echo_message(message: Message) -> None:
    try:
        await message.reply(text=message.text)
    except TypeError:
        await message.answer("Nice try!")











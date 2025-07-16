from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from keyboards.reply import  yes_no_keyboard
from aiogram.fsm.state import State, StatesGroup
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram import F
from keyboards.reply import  keyboard
from database import add_user


fsm_router = Router()

class Form(StatesGroup):
    name = State()
    age = State()
    weight = State()
    height = State()
    like_bots = State()



@fsm_router.message(Command("form"))
async def cmd_start(message: Message, state: FSMContext):
    await message.answer("Привет, как тебя зовут?")
    await state.set_state(Form.name)


@fsm_router.message(Form.name)
async def cmd_start(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Form.weight)
    await message.answer("Сколько ты весишь?")



@fsm_router.message(Form.weight)
async def cmd_start(message: Message, state: FSMContext):
    await state.update_data(weight=message.text)
    await state.set_state(Form.height)
    await message.answer("Какой у тебя рост?")

@fsm_router.message(Form.height)
async def cmd_start(message: Message, state: FSMContext):
    await state.update_data(height=message.text)
    await state.set_state(Form.age)
    await message.answer("Сколько тебе лет?")

    

@fsm_router.message(Form.age, F.text.isdigit())
async def process_age(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await state.set_state(Form.like_bots)
    data = await state.get_data()
    await message.answer(text = f"Приятно познакомиться, {data['name']}!\n Тебе нравятся телеграмм боты?", reply_markup=yes_no_keyboard)
    


@fsm_router.message(Form.like_bots, F.text.casefold() == "да")
async def process_dont_like_write_bots(message: Message, state: FSMContext) -> None:
    await state.update_data(like_bots="да")
    data = await state.update_data()
    add_user(
        user_id=message.from_user.id,
        name=data['name'],
        age=int(data['age']),
        weight=int(data['weight']),
        height=int(data['height']),
        like_bots=data['like_bots']
    )
    await state.clear()
    await message.reply(
        text="Классно мне тоже!",
        reply_markup=keyboard
    )
    
@fsm_router.message(Form.like_bots, F.text.casefold() == "нет")
async def process_dont_like_write_bots(message: Message, state: FSMContext) -> None:
    await state.update_data(like_bots="нет")
    data = await state.update_data()
    add_user(
        user_id=message.from_user.id,
        name=data['name'],
        age=int(data['age']),
        weight=int(data['weight']),
        height=int(data['height']),
        like_bots=data['like_bots']
    )
    await state.clear()
    await message.reply(
        text="я запомню..",
        reply_markup=keyboard
    )




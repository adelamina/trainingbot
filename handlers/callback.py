import aiogram
from aiogram import Router, F
from aiogram.types import CallbackQuery
from keyboards.inline import start_kb, test_kb, avtor_kb, menu11_kb, aboutbot, helpbot, avtorbot, sleepbot, foodbot
from keyboards.reply import  keyboard

callbacks_router = Router()


@callbacks_router.callback_query(F.data == "query")
async def get_query(callback: CallbackQuery):
    await callback.answer("zxc")
    q_message = "we got query"
    await callback.message.answer(text=q_message)


@callbacks_router.callback_query(F.data == "test")
async def handle_test(t: CallbackQuery):
    await t.answer("asd")
    await t.message.answer(text="test")


@callbacks_router.callback_query(F.data == "help")
async def handle_test(t: CallbackQuery):
    await t.message.answer(text="всего 3 команды: ./help, ./about, ./start")


@callbacks_router.callback_query(F.data == "details")
async def handle_button(callback: CallbackQuery):
    await t.message.answer(text="текст обновился", reply_markup=avtor_kb)

#главное меню о боте
@callbacks_router.callback_query(F.data == "about11")
async def handle_button(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text="Бот для тренировок, который сможет рассчитывать суточную норму калорий, будет напоминать о тренировках, который будет хранить данные о сне и оценивать их.", reply_markup=aboutbot)

#главное меню информация о разработчике
@callbacks_router.callback_query(F.data == "adelamina11")
async def handle_button(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text="здесь будут ссылки автора", reply_markup=avtorbot)

#главное меню оценка сна
@callbacks_router.callback_query(F.data == "sleep11")
async def handle_button(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text="оценка времени сна", reply_markup=sleepbot)

#главное меню помощь
@callbacks_router.callback_query(F.data == "commands11")
async def handle_button(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text="все команды:",reply_markup=helpbot)

#главное меню еда
@callbacks_router.callback_query(F.data == "food11")
async def handle_button(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text="помощь с рационом еды", reply_markup=foodbot)

# о боте назад
@callbacks_router.callback_query(F.data == "back11")
async def handle_button(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text="Главное меню.", reply_markup=menu11_kb)


#помощь назад
@callbacks_router.callback_query(F.data == "back22")
async def handle_button(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text="Главное меню.", reply_markup=menu11_kb)


#автор назад
@callbacks_router.callback_query(F.data == "back33")
async def handle_button(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text="Главное меню.", reply_markup=menu11_kb)



#информация о сне назад
@callbacks_router.callback_query(F.data == "back44")
async def handle_button(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text="Главное меню.", reply_markup=menu11_kb)

#еда назад
@callbacks_router.callback_query(F.data == "back55")
async def handle_button(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text="Главное меню.", reply_markup=menu11_kb)




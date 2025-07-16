import aiogram
import asyncio
from aiogram import Router, F
from aiogram.types import CallbackQuery
from keyboards.inline import start_kb, test_kb, avtor_kb, menu11_kb, aboutbot, helpbot, avtorbot, sleepbot, foodbot, sleeprate, sleeprate6, sleepmenu, sleeprate13, sleeprate18, sleeprate61, taimer11, taimerback
from keyboards.reply import  keyboard
from aiogram.types import FSInputFile
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
    await t.message.answer(text="если вы нашли ошибку пишите @adelamina")


@callbacks_router.callback_query(F.data == "details")
async def handle_button(callback: CallbackQuery):
    await t.message.answer(text="текст обновился", reply_markup=avtor_kb)

#главное меню о боте
@callbacks_router.callback_query(F.data == "about11")
async def handle_button(callback: CallbackQuery):
    photo = FSInputFile("marcicat123.jpg")
    await callback.message.answer_photo(photo=photo, caption="Бот для тренировок, который сможет рассчитывать суточную норму калорий, будет напоминать о тренировках, который будет хранить данные о сне и оценивать их.", reply_markup=aboutbot)
    await callback.answer()


#главное меню информация о разработчике
@callbacks_router.callback_query(F.data == "adelamina11")
async def handle_button(callback: CallbackQuery):
    photo = FSInputFile("aboutme.jpg")
    await callback.message.answer_photo(photo=photo, caption="здесь будут ссылки автора", reply_markup=avtorbot)
    await callback.answer()


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



@callbacks_router.callback_query(F.data == "3000k")
async def handle_button(callback: CallbackQuery):
    a = random.randint(1, 10)
    if a == 1:
        b = '-Завтрак: Омлет из 3 яиц + 100 г овсянки на молоке + 20 г орехов + чай с мёдом -Перекус: 200 г творога (5%) + 1 банан + 1 ст. л. мёда -Обед: 150 г куриной грудки + 100 г гречки + 200 г овощей + 1 ст. л. оливкового масла -Перекус: 50 г протеина + 2 кусочка цельнозернового хлеба + 30 г арахисовой пасты -Ужин: 150 г лосося + 100 г бурого риса + салат из овощей -Перед сном: 200 мл кефира + 30 г орехов'

    elif a == 2:
        b = '-Завтрак: 150 г овсянки на молоке + 30 г изюма + 20 г орехов + кофе -Перекус: 2 банана + 100 г рисовых хлебцев + 30 г мёда -Обед: 150 г индейки + 150 г макарон из твёрдых сортов + 200 г овощей -Перекус: 100 г творога + 50 г фиников + 1 ст. л. льняного масла -Ужин: 150 г говядины + 150 г картофеля + салат с оливковым маслом -На ночь: 200 г натурального йогурта + 1 фрукт  '

    elif a == 3:
        b = '-Завтрак: 200 г творога + 50 г овсянки + 1 банан -Перекус: 150 г куриной грудки + 100 г риса + овощи  -Обед: 200 г говядины + 150 г гречки + салат -Перекус: 6 яичных белков + 2 тоста + авокадо -Ужин: 200 г рыбы + 100 г киноа + зелень -Перед сном: казеиновый протеин + 30 г миндаля'

    elif a == 4:
        b = '- Завтрак: 3 яйца + авокадо + 2 кусочка цельнозернового хлеба -Перекус: 30 г орехов + 100 г творога + 1 ст. л. мёда -Обед: 150 г сёмги + 100 г киноа + овощи -Перекус: смузи (банан, орехи, молоко, протеин) -Ужин: 150 г курицы + 100 г нута + салат с оливковым маслом -На ночь: 200 мл кефира + льняные семена'

    elif a == 5:
        b = '-Завтрак: 200 г гречки + 2 яйца + 20 г сливочного масла  Перекус: 100 г макарон + 100 г куриной печени -Обед: 150 г минтая + 150 г риса + тушёные овощи -Перекус: 200 г творога + 1 банан -Ужин: 150 г говяжьего фарша + 100 г картофеля -На ночь: 200 мл молока + 2 кусочка хлеба'

    elif a == 6:
        b = '-Завтрак: 150 г тофу + 100 г овсянки + орехи -Перекус: протеиновый коктейль на миндальном молоке + банан - Обед: 150 г чечевицы + 100 г киноа + овощи -Перекус: 200 г греческого йогурта + мёд + семена чиа -Ужин: 200 г фасоли + 100 г картофеля + авокадо -На ночь: 30 г орехов + стакан кефира'

    elif a == 7:
        b = '-Завтрак: 3 яйца + 100 г овсянки + 30 г арахисовой пасты -Перекус: гейнер (углеводно-белковый коктейль) + банан -Обед: 200 г курицы + 150 г макарон + овощи -Перекус: 100 г творога + 50 г мёда + орехи -Ужин: 200 г говядины + 150 г риса + салат -Перед сном: казеин + 1 фрукт '

    elif a == 8:
        b = '-Завтрак: 4 яйца + авокадо + 30 г сыра -Перекус: 200 г творога + орехи -Обед: 200 г курицы + 150 г брокколи + оливковое масло -Перекус: протеиновый коктейль + 1 ст. л. льняного масла -Ужин: 200 г рыбы + салат с орехами -На ночь: казеин + 20 г кокосового масла '

    elif a == 9:
        b = '-Завтрак: 100 г овсянки + 30 г изюма + протеин -Перекус: 2 банана + 50 г орехов -Обед: 150 г индейки + 150 г риса + овощи -Перекус: смузи (молоко, банан, протеин, овсянка) -Ужин: 150 г рыбы + 100 г гречки + салат -На ночь: творог + мёд'

    else:
        b = '-Завтрак: 200 г творога + 50 г овсянки + мёд -Перекус: протеиновый коктейль + банан -Обед: 200 г говядины + 150 г картофеля + овощи  -Перекус: 6 яичных белков + авокадо  -Ужин: 200 г курицы + 100 г гречки -На ночь: казеин + орехи'
    await callback.answer()
    await callback.message.edit_text(text=b, reply_markup=forfood)




@callbacks_router.callback_query(F.data == "1500k")
async def handle_button(callback: CallbackQuery):
    a = random.randint(1, 10)
    if a == 1:
        b = '-Завтрак: Овсянка на воде + 1 яйцо + 10 г орехов (300 ккал) -Перекус: 100 г творога + огурец (150 ккал) -Обед: 100 г куриной грудки + 50 г гречки + салат из капусты (400 ккал) -Перекус: Яблоко + 10 г арахисовой пасты (200 ккал) -Ужин: 150 г запеченной рыбы + 100 г брокколи (350 ккал) -На ночь: Стакан кефира 1% (100 ккал)  '

    elif a == 2:
        b = '-Завтрак: Омлет из 2 яиц + 30 г сыра + авокадо (400 ккал) -Перекус: Горсть миндаля (20 г) (120 ккал) -Обед: 150 г говядины + салат (огурец, оливковое масло) (450 ккал) -Перекус: Творог 5% (100 г) (120 ккал) -Ужин: Лосось на гриле + стручковая фасоль (350 ккал) -На ночь: Зеленый чай без сахара (0 ккал)  '

    elif a == 3:
        b = '-Завтрак: 200 г творога + 50 г овсянки + 1 банан -Перекус: 150 г куриной грудки + 100 г риса + овощи  -Обед: 200 г говядины + 150 г гречки + салат -Перекус: 6 яичных белков + 2 тоста + авокадо -Ужин: 200 г рыбы + 100 г киноа + зелень -Перед сном: казеиновый протеин + 30 г миндаля'

    elif a == 4:
        b = '-Завтрак: Творог 5% (150 г) + 1 яйцо (300 ккал) -Перекус: Протеиновый батончик (200 ккал) -Обед: 150 г индейки + 50 г риса + огурец (450 ккал) -Перекус: Вареные креветки (100 г) (100 ккал) -Ужин: Творожная запеканка без сахара (300 ккал) -На ночь: Казеиновый протеин (150 ккал)'

    elif a == 5:
        b = '-Завтрак: Протеиновый коктейль на молоке (300 ккал) -Перекус: Банан + 20 г орехов (250 ккал) -Обед: Консервированный тунец + ржаной хлеб (400 ккал) -Перекус: Йогурт без сахара (150 г) (100 ккал) -Ужин: Омлет из 2 яиц с помидорами (350 ккал)  '

    elif a == 6:
        b = '-Завтрак: Овсянка + мед + изюм (350 ккал) -Перекус: 2 хлебца с творожным сыром (200 ккал) -Обед: Макароны из твердых сортов + куриная грудка (450 ккал) -Перекус: Фруктовый салат (яблоко, груша) (150 ккал) -Ужин: Тыквенная каша (300 ккал)'

    elif a == 7:
        b = '-Завтрак: Яичница с беконом (2 яйца + 30 г бекона) (400 ккал) -Перекус: Сырные чипсы (30 г) (200 ккал) -Обед: Жареная курица (голень) + цветная капуста (450 ккал) -Перекус: Авокадо с солью (150 ккал) -Ужин: Стейк из свинины + зелень (300 ккал)  '

    elif a == 8:
        b = '-Завтрак: Пшенная каша на воде + яйцо (300 ккал) -Перекус: Яблоко (80 ккал) -Обед: Гречка + куриные сердечки + морковь (450 ккал) -Перекус: Кефир 1% (200 мл) (100 ккал) -Ужин: Тушеная капуста с яйцом (350 ккал) -На ночь: Чай с молоком (50 ккал)  '

    elif a == 9:
        b = '-Завтрак: Блинчики из овсяной муки + мед (350 ккал) -Перекус: Зефир (1 шт.) (120 ккал) -Обед: Курица + рис + овощи (400 ккал) -Перекус: Творог с какао и стевией (200 ккал)  -Ужин: Рыба + салат (350 ккал) -Десерт: Кусочек черного шоколада (15 г) (80 ккал)'

    else:
        b = ' -Обед: 150 г говядины + гречка + овощи (700 ккал) -Ужин: Лосось + авокадо + орехи (800 ккал)'
    await callback.answer()
    await callback.message.edit_text(text=b, reply_markup=forfood)


#вам от 61+
@callbacks_router.callback_query(F.data == "sleeprate44")
async def handle_button(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text="Сколько вы спали?", reply_markup=sleeprate61)

#вам от 6-12
@callbacks_router.callback_query(F.data == "sleeprate11")
async def handle_button(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text="Сколько вы спали?", reply_markup=sleeprate6)

#вам  6 - 12 вы поспали норму
@callbacks_router.callback_query(F.data == "sleeprate111")
async def handle_button(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text="Ваш сон идеален! Продолжайте в том же духе", reply_markup=sleepmenu)
#вам  6 - 12 вы недоспаспали норму
@callbacks_router.callback_query(F.data == "sleeprate333")
async def handle_button(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text="Вы недоспали норму! Иеальный сон для вашего возвраста 9 - 12 часов", reply_markup=sleepmenu)

#вам  6 - 12 вы переспаспали норму
@callbacks_router.callback_query(F.data == "sleeprate222")
async def handle_button(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text="Спите чуть меньше, идеальный сон для вашего возвраста 9 - 12 часов ", reply_markup=sleepmenu)

#назд после всех снов
@callbacks_router.callback_query(F.data == "menu99")
async def handle_button(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text="Главное меню.", reply_markup=menu11_kb)

#вам от 13 - 17
@callbacks_router.callback_query(F.data == "sleeprate22")
async def handle_button(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text="Сколько вы спали?", reply_markup=sleeprate13)

#вам от 18 - 60
@callbacks_router.callback_query(F.data == "sleeprate33")
async def handle_button(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text="Сколько вы спали?", reply_markup=sleeprate18)

#кнопка назад оценка сна
@callbacks_router.callback_query(F.data == "back77")
async def handle_button(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text="оценка времени сна", reply_markup=sleepbot)

#виджет анализ сна
@callbacks_router.callback_query(F.data == "sleeptime")
async def handle_button(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text="сколько вам лет", reply_markup=sleeprate)
#13 - 18
@callbacks_router.callback_query(F.data == "sleeprate1111")
async def handle_button(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text="Ваш сон идеален! Продолжайте в том же духе", reply_markup=sleepmenu)
#13 - 18
@callbacks_router.callback_query(F.data == "sleeprate3333")
async def handle_button(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text="Вы недоспали норму! Иеальный сон для вашего возвраста 8 - 10 часов", reply_markup=sleepmenu)
#13 - 18
@callbacks_router.callback_query(F.data == "sleeprate2222")
async def handle_button(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text="Спите чуть меньше, идеальный сон для вашего возвраста 8 - 10 часов ", reply_markup=sleepmenu)


#18 - 60
@callbacks_router.callback_query(F.data == "sleeprate444")
async def handle_button(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text="Ваш сон идеален! Продолжайте в том же духе", reply_markup=sleepmenu)
#18 - 60
@callbacks_router.callback_query(F.data == "sleeprate666")
async def handle_button(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text="Вы недоспали норму! Иеальный сон для вашего возвраста 7 - 9 часов", reply_markup=sleepmenu)
#18 - 60
@callbacks_router.callback_query(F.data == "sleeprate555")
async def handle_button(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text="Спите чуть меньше, идеальный сон для вашего возвраста 7 - 9 часов ", reply_markup=sleepmenu)


#61
@callbacks_router.callback_query(F.data == "sleeprate777")
async def handle_button(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text="Ваш сон идеален! Продолжайте в том же духе", reply_markup=sleepmenu)
#61
@callbacks_router.callback_query(F.data == "sleeprate999")
async def handle_button(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text="Вы недоспали норму! Иеальный сон для вашего возвраста 7 - 8 часов", reply_markup=sleepmenu)
#61
@callbacks_router.callback_query(F.data == "sleeprate888")
async def handle_button(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text="Спите чуть меньше, идеальный сон для вашего возвраста 7 - 8 часов ", reply_markup=sleepmenu)





@callbacks_router.callback_query(F.data == "back88")
async def handle_button(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text="сколько вам лет", reply_markup=sleeprate)




@callbacks_router.callback_query(F.data == "taimer")
async def handle_button(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text="здесь вы можете увидеть таймеры на разное время и использовать их", reply_markup=taimer11)



@callbacks_router.callback_query(F.data == "taimer111")
async def handle_button(callback: CallbackQuery):
    await callback.answer("Напоминалка запущена")
    await asyncio.sleep(1800)
    await callback.message.edit_text(text="пол часа прошло")

@callbacks_router.callback_query(F.data == "taimer222")
async def handle_button(callback: CallbackQuery):
    await callback.answer("Напоминалка запущена")
    await asyncio.sleep(3600)
    await callback.message.edit_text(text="час прошел")

@callbacks_router.callback_query(F.data == "taimer333")
async def handle_button(callback: CallbackQuery):
    await callback.answer("Напоминалка запущена")
    await asyncio.sleep(7200)
    await callback.message.answer(text="2 часа прошло")




@callbacks_router.callback_query(F.data == "back333")
async def handle_button(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text="здесь вы можете увидеть таймеры на разное время и использовать их", reply_markup=taimer11)

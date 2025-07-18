import aiogram
import asyncio
from aiogram import Router, F
from aiogram.types import CallbackQuery
from keyboards.inline import start_kb, test_kb, avtor_kb, menu11_kb, aboutbot, helpbot, avtorbot, sleepbot, foodbot, sleeprate, sleeprate6, sleepmenu, sleeprate13, sleeprate18, sleeprate61, taimer11, forfood
from keyboards.reply import  keyboard
from aiogram.types import FSInputFile
import random

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
    await callback.message.delete()
    photo = FSInputFile("marcicat123.jpg")
    await callback.message.answer_photo(photo=photo, caption="Бот для тренировок, который сможет рассчитывать суточную норму калорий, будет напоминать о тренировках, который будет хранить данные о сне и оценивать их.", reply_markup=aboutbot)
    await callback.answer()


#главное меню информация о разработчике
@callbacks_router.callback_query(F.data == "adelamina11")
async def handle_button(callback: CallbackQuery):
    await callback.message.delete()
    photo = FSInputFile("aboutme.jpg")
    await callback.message.answer_photo(photo=photo, caption="здесь будут ссылки автора", reply_markup=avtorbot)
    await callback.answer()
    


#главное меню оценка сна
@callbacks_router.callback_query(F.data == "sleep11")
async def handle_button(callback: CallbackQuery):
    await callback.message.delete()
    photo = FSInputFile("spit11.jpg")
    await callback.message.answer_photo(photo=photo, caption="оценка времени сна", reply_markup=sleepbot)
    await callback.answer()




#главное меню помощь
@callbacks_router.callback_query(F.data == "commands11")
async def handle_button(callback: CallbackQuery):
    await callback.message.delete()
    photo = FSInputFile("help123.jpg")
    await callback.message.answer_photo(photo=photo, caption="если вы нашли ошибку пишите @adelamina", reply_markup=helpbot)
    await callback.answer()






@callbacks_router.callback_query(F.data == "food11")
async def handle_button(callback: CallbackQuery):
    await callback.message.delete()
    photo = FSInputFile("food123.jpg")
    await callback.message.answer_photo(photo=photo, caption="здесь можно выбрать рационы еды", reply_markup=foodbot)
    await callback.answer()

@callbacks_router.callback_query(F.data == "back66")
async def handle_button(callback: CallbackQuery):
    await callback.message.delete()
    photo = FSInputFile("food123.jpg")
    await callback.message.answer_photo(photo=photo, caption="здесь можно выбрать рационы еды", reply_markup=foodbot)
    await callback.answer()



# о боте назад
@callbacks_router.callback_query(F.data == "back11")
async def handle_button(callback: CallbackQuery):
    await callback.message.delete()
    photo = FSInputFile("robot123.jpg")
    await callback.message.answer_photo(photo=photo, caption="Главное меню.", reply_markup=menu11_kb)
    await callback.answer()
    

#помощь назад
@callbacks_router.callback_query(F.data == "back22")
async def handle_button(callback: CallbackQuery):
    await callback.message.delete()
    photo = FSInputFile("robot123.jpg")
    await callback.message.answer_photo(photo=photo, caption="Главное меню.", reply_markup=menu11_kb)
    await callback.answer()
    


#автор назад
@callbacks_router.callback_query(F.data == "back33")
async def handle_button(callback: CallbackQuery): 
    await callback.message.delete()
    photo = FSInputFile("robot123.jpg")
    await callback.message.answer_photo(photo=photo, caption="Главное меню.", reply_markup=menu11_kb)
    await callback.answer()
    




#информация о сне назад
@callbacks_router.callback_query(F.data == "back44")
async def handle_button(callback: CallbackQuery):
    await callback.message.delete()
    photo = FSInputFile("robot123.jpg")
    await callback.message.answer_photo(photo=photo, caption="Главное меню.", reply_markup=menu11_kb)
    await callback.answer()
    

#еда назад
@callbacks_router.callback_query(F.data == "back55")
async def handle_button(callback: CallbackQuery):
    await callback.message.delete()
    photo = FSInputFile("robot123.jpg")
    await callback.message.answer_photo(photo=photo, caption="Главное меню.", reply_markup=menu11_kb)
    await callback.answer()
    


@callbacks_router.callback_query(F.data == "3000k")
async def handle_button(callback: CallbackQuery):
    await callback.message.delete()
    photo = FSInputFile("food123.jpg")


    a = random.randint(1, 10)
    if a == 1:
        b = '''
            <b>-Завтрак: </b>\n
            Омлет из 3 яиц + 100 г овсянки на молоке + 20 г орехов + чай с мёдом\n
            <b>-Перекус: </b>\n
            200 г творога (5%) + 1 банан + 1 ст. л. мёда\n
            <b>-Обед: </b>\n
            150 г куриной грудки + 100 г гречки + 200 г овощей + 1 ст. л. оливкового масла\n
            <b>-Перекус: </b>\n
            50 г протеина + 2 кусочка цельнозернового хлеба + 30 г арахисовой пасты\n
            <b>-Ужин </b>:\n
            50 г лосося + 100 г бурого риса + салат из овощей -Перед сном: 200 мл кефира + 30 г орехов
            '''
    elif a == 2:
        b = '''
            <b>Завтрак: </b>\n
            150 г овсянки на молоке + 30 г изюма + 20 г орехов + кофе\n
            <b>-Перекус: </b>\n
            2 банана + 100 г рисовых хлебцев + 30 г мёда\n 
            <b>-Обед: </b>\n
            150 г индейки + 150 г макарон из твёрдых сортов + 200 г овощей\n
            <b>-Перекус: </b>\n
            100 г творога + 50 г фиников + 1 ст. л. льняного масла\n
            <b>-Ужин: </b>\n 
            150 г говядины + 150 г картофеля + салат с оливковым маслом -На ночь: 200 г натурального йогурта + 1 фрукт
            '''
    elif a == 3:
        b = '''
            <b>-Завтрак: </b>\n
            200 г творога + 50 г овсянки + 1 банан\n
            <b>-Перекус: </b>
            150 г куриной грудки + 100 г риса + овощи\n
            <b>-Обед: </b>
            200 г говядины + 150 г гречки + салат\n
            <b>-Перекус: </b>
            6 яичных белков + 2 тоста + авокадо\n
            <b>-Ужин: </b>
            200 г рыбы + 100 г киноа + зелень\n
            <b>-Перед сном: </b>
            казеиновый протеин + 30 г миндаля
            '''
    elif a == 4:
        b = '''
            <b>- Завтрак: </b>\n
             яйца + авокадо + 2 кусочка цельнозернового хлеба\n 
            <b>-Перекус: </b>\n
            30 г орехов + 100 г творога + 1 ст. л. мёда\n
            <b>-Обед: </b>\n 
            150 г сёмги + 100 г киноа + овощи\n 
            <b>-Перекус: </b>\n
            смузи (банан, орехи, молоко, протеин)\n 
            <b>-Ужин: </b>\n 
            150 г курицы + 100 г нута + салат с оливковым маслом\n
            <b>-На ночь: </b>\n
            200 мл кефира + льняные семена
            '''
    elif a == 5:
        b = '''
            <b>-Завтрак </b>\n
            200 г гречки + 2 яйца + 20 г сливочного масла\n
            <b>Перекус: </b>\n
            100 г макарон + 100 г куриной печени\n 
            <b>-Обед: </b>\n 
            150 г минтая + 150 г риса + тушёные овощи\n
            <b>-Перекус: </b>\n
            200 г творога + 1 банан\n 
            <b>-Ужин: </b>\n
            150 г говяжьего фарша + 100 г картофеля\n 
            <b>-На ночь: </b>\n 
            200 мл молока + 2 кусочка хлеба
            '''
    elif a == 6:
        b = '''
            <b>-Завтрак: </b>\n
            150 г тофу + 100 г овсянки + орехи\n
            <b>-Перекус: </b>\n
            протеиновый коктейль на миндальном молоке + банан\n
            <b>-Обед: </b>\n
            150 г чечевицы + 100 г киноа + овощи\n
            <b>-Перекус </b>:\n
            200 г греческого йогурта + мёд + семена чиа\n 
            <b>-Ужин: </b>\n
            200 г фасоли + 100 г картофеля + авокадо\n
            <b>-На ночь: </b>\n
            30 г орехов + стакан кефира
            '''
    elif a == 7:
        b = '''
            <b>-Завтрак: </b>\n
            3 яйца + 100 г овсянки + 30 г арахисовой пасты\n 
            <b>-Перекус: </b>\n 
            гейнер (углеводно-белковый коктейль) + банан\n
            <b>-Обед: </b>\n
            200 г курицы + 150 г макарон + овощи\n 
            <b>-Перекус: </b>\n 
            100 г творога + 50 г мёда + орехи\n 
            <b>-Ужин: </b>\n
            200 г говядины + 150 г риса + салат\n 
            <b>-Перед сном: </b>\n 
            казеин + 1 фрукт
            '''
    elif a == 8:
        b = '''
            <b>-Завтрак: </b>\n
            4 яйца + авокадо + 30 г сыра\n
            <b>-Перекус: </b>\n 
            200 г творога + орехи\n 
            <b>-Обед: </b>\n 
            200 г курицы + 150 г брокколи + оливковое масло\n
            <b>-Перекус: </b>\n
            протеиновый коктейль + 1 ст. л. льняного масла\n 
            <b>-Ужин: </b>\n 
            200 г рыбы + салат с орехами\n 
            <b>-На ночь: </b>\n 
            казеин + 20 г кокосового масла
            '''
    elif a == 9:
        b = '''
            <b>-Завтрак: </b>\n
            100 г овсянки + 30 г изюма + протеин\n 
            <b>-Перекус: </b>\n
            2 банана + 50 г орехов\n
            <b>-Обед: </b> 
            150 г индейки + 150 г риса + овощи\n 
            <b>-Перекус: </b>\n 
            смузи (молоко, банан, протеин, овсянка)\n 
            <b>-Ужин: </b>\n 
            150 г рыбы + 100 г гречки + салат\n
            <b>-На ночь </b>:\n 
            творог + мёд
            '''
    else:
        b = '''
            <b>-Завтрак: </b>\n
            200 г творога + 50 г овсянки + мёд\n
            <b>-Перекус: </b>\n
            протеиновый коктейль + банан\n
            <b>-Обед: </b>\n
            200 г говядины + 150 г картофеля + овощи\n
            <b>-Перекус: </b>\n
            6 яичных белков + авокадо\n
            <b>-Ужин: </b>\n
            200 г курицы + 100 г гречки\n 
            <b>-На ночь: </b>\n
            казеин + орехи
            '''
    await callback.message.answer_photo(photo=photo, caption=b, reply_markup=forfood, parse_mode="HTML")
    await callback.answer()





@callbacks_router.callback_query(F.data == "1500k")
async def handle_button(callback: CallbackQuery):
    await callback.message.delete()
    photo = FSInputFile("food123.jpg")


    a = random.randint(1, 10)
    if a == 1:
        b = '''
            <b>-Завтрак: </b>\n
            Овсянка на воде + 1 яйцо + 10 г орехов (300 ккал) \n
            <b>-Перекус: </b> \n
            100 г творога + огурец (150 ккал) \n
            <b>-Обед: </b> \n
            100 г куриной грудки + 50 г гречки + салат из капусты (400 ккал)\n 
            <b>-Перекус: </b>\n 
            Яблоко + 10 г арахисовой пасты (200 ккал) \n
            <b>-Ужин: </b> \n
            150 г запеченной рыбы + 100 г брокколи (350 ккал) \n
            <b>-На ночь: </b> \n
            Стакан кефира 1% (100 ккал)
            '''
    elif a == 2:
        b = '''
            <b>-Завтрак: </b>\n
            Омлет из 2 яиц + 30 г сыра + авокадо (400 ккал)\n
            <b>-Перекус: </b>\n
            Горсть миндаля (20 г) (120 ккал)\n 
            <b>-Обед: </b>\n
            150 г говядины + салат (огурец, оливковое масло) (450 ккал)\n
            <b>-Перекус: </b>\n 
            Творог 5% (100 г) (120 ккал)\n 
            <b>-Ужин: </b>\n 
            Лосось на гриле + стручковая фасоль (350 ккал)\n 
            <b>-На ночь: </b>\n 
            Зеленый чай без сахара (0 ккал) 
            '''
    elif a == 3:
        b = '''
            <b>-Завтрак: </b>\n
            200 г творога + 50 г овсянки + 1 банан \n
            <b>-Перекус: </b> 
            150 г куриной грудки + 100 г риса + овощи\n  
            <b>-Обед: </b>\n
            200 г говядины + 150 г гречки + салат \n
            <b>-Перекус: </b>\n 
            6 яичных белков + 2 тоста + авокадо\n 
            <b>-Ужин: </b>\n
            200 г рыбы + 100 г киноа + зелень\n
            <b>-Перед сном: </b>\n
            казеиновый протеин + 30 г миндаля
            '''
    elif a == 4:
        b = '''
            <b>-Завтрак: </b> \n
            Творог 5% (150 г) + 1 яйцо (300 ккал) \n
            <b>-Перекус: </b>\n 
            Протеиновый батончик (200 ккал)\n 
            <b>-Обед: </b> \n
            150 г индейки + 50 г риса + огурец (450 ккал)\n 
            <b>-Перекус: </b>\n
            Вареные креветки (100 г) (100 ккал)\n 
            <b>-Ужин: </b>\n
            Творожная запеканка без сахара (300 ккал)\n 
            <b>-На ночь: </b>\n
            Казеиновый протеин (150 ккал)
            '''
    elif a == 5:
        b = '''
            <b>-Завтрак: </b>\n
            Протеиновый коктейль на молоке (300 ккал)\n 
            <b>-Перекус: </b>\n
            Банан + 20 г орехов (250 ккал)\n 
            <b>-Обед: </b>\n 
            Консервированный тунец + ржаной хлеб (400 ккал)\n 
            <b>-Перекус: </b>\n 
            Йогурт без сахара (150 г) (100 ккал)\n 
            <b>-Ужин: </b>\n
            Омлет из 2 яиц с помидорами (350 ккал)
            '''
    elif a == 6:
        b = '''
            <b>-Завтрак: </b>\n
            Овсянка + мед + изюм (350 ккал)\n 
            <b>-Перекус: </b>\n 
            2 хлебца с творожным сыром (200 ккал)\n 
            <b>-Обед: </b>\n
            Макароны из твердых сортов + куриная грудка (450 ккал)\n
            <b>-Перекус: </b>\n
            Фруктовый салат (яблоко, груша) (150 ккал)\n
            <b>-Ужин: </b>\n
            Тыквенная каша (300 ккал)
            '''
    elif a == 7:
        b = '''
            <b>-Завтрак: </b>\n
            Яичница с беконом (2 яйца + 30 г бекона) (400 ккал)\n 
            <b>-Перекус: </b>\n
            Сырные чипсы (30 г) (200 ккал) \n
            <b>-Обед: </b>\n
            Жареная курица (голень) + цветная капуста (450 ккал) \n
            <b>-Перекус: </b> \n
            Авокадо с солью (150 ккал)\n 
            <b>-Ужин: </b>\n 
            Стейк из свинины + зелень (300 ккал)
            '''
    elif a == 8:
        b = '''
            <b>-Завтрак: </b>\n
            Пшенная каша на воде + яйцо (300 ккал)\n 
            <b>-Перекус: </b>\n 
            Яблоко (80 ккал)\n 
            <b>-Обед: </b>\n 
            Гречка + куриные сердечки + морковь (450 ккал)\n 
            <b>-Перекус: </b>\n 
            Кефир 1% (200 мл) (100 ккал)\n
            <b>-Ужин: </b>\n
            Тушеная капуста с яйцом (350 ккал)\n 
            <b>-На ночь: </b>\n
            Чай с молоком (50 ккал)
            '''
    elif a == 9:
        b = '''
            <b>-Завтрак: </b>\n
            Блинчики из овсяной муки + мед (350 ккал)\n 
            <b>-Перекус: </b>\n
            Зефир (1 шт.) (120 ккал) \n
            <b>-Обед: </b>\n
            Курица + рис + овощи (400 ккал)\n
            <b>-Перекус: </b>\n 
            Творог с какао и стевией (200 ккал)\n
            <b>-Ужин: </b>\n
            Рыба + салат (350 ккал)\n 
            <b>-Десерт: </b>\n
            Кусочек черного шоколада (15 г) (80 ккал)
            '''
    else:
        b =  '''
            '<b>-Обед: </b>\n
            '150 г говядины + гречка + овощи (700 ккал)\n
            '<b>-Ужин: </b>\n
            'Лосось + авокадо + орехи (800 ккал)'
            '''
    await callback.message.answer_photo(photo=photo, caption=b, reply_markup=forfood, parse_mode="HTML")
    await callback.answer()



#вам от 61+
@callbacks_router.callback_query(F.data == "sleeprate44")
async def handle_button(callback: CallbackQuery):
    await callback.message.delete()
    photo = FSInputFile("sleep22.jpg")
    await callback.message.answer_photo(photo=photo, caption="Сколько вы спали?", reply_markup=sleeprate61)
    await callback.answer()

#вам от 6-12
@callbacks_router.callback_query(F.data == "sleeprate11")
async def handle_button(callback: CallbackQuery):
    await callback.message.delete()
    photo = FSInputFile("sleep33.jpg")
    await callback.message.answer_photo(photo=photo, caption="Сколько вы спали?", reply_markup=sleeprate6)
    await callback.answer()



#вам  6 - 12 вы поспали норму
@callbacks_router.callback_query(F.data == "sleeprate111")
async def handle_button(callback: CallbackQuery):
    await callback.message.delete()
    photo = FSInputFile("sleep33.jpg")
    await callback.message.answer_photo(photo=photo, caption="Ваш сон идеален! Продолжайте в том же духе", reply_markup=sleepmenu)
    await callback.answer()



#вам  6 - 12 вы недоспаспали норму
@callbacks_router.callback_query(F.data == "sleeprate333")
async def handle_button(callback: CallbackQuery):
    await callback.message.delete()
    photo = FSInputFile("sleep33.jpg")
    await callback.message.answer_photo(photo=photo, caption="Вы недоспали норму! Иеальный сон для вашего возвраста 9 - 12 часов", reply_markup=sleepmenu)
    await callback.answer()


#вам  6 - 12 вы переспаспали норму
@callbacks_router.callback_query(F.data == "sleeprate222")
async def handle_button(callback: CallbackQuery):
    await callback.message.delete()
    photo = FSInputFile("sleep33.jpg")
    await callback.message.answer_photo(photo=photo, caption="Спите чуть меньше, идеальный сон для вашего возвраста 9 - 12 часов ", reply_markup=sleepmenu)
    await callback.answer()


#назд после всех снов
@callbacks_router.callback_query(F.data == "menu99")
async def handle_button(callback: CallbackQuery):
    await callback.message.delete()
    photo = FSInputFile("robot123.jpg")
    await callback.message.answer_photo(photo=photo, caption="Главное меню.", reply_markup=menu11_kb)
    await callback.answer()

#вам от 13 - 17
@callbacks_router.callback_query(F.data == "sleeprate22")
async def handle_button(callback: CallbackQuery):
    await callback.message.delete()
    photo = FSInputFile("sleep11.jpg")
    await callback.message.answer_photo(photo=photo, caption="Сколько вы спали?", reply_markup=sleeprate13)
    await callback.answer()

#вам от 18 - 60
@callbacks_router.callback_query(F.data == "sleeprate33")
async def handle_button(callback: CallbackQuery):
    await callback.message.delete()
    photo = FSInputFile("sleep123.jpg")
    await callback.message.answer_photo(photo=photo, caption="Сколько вы спали?", reply_markup=sleeprate18)
    await callback.answer()


#кнопка назад оценка сна
@callbacks_router.callback_query(F.data == "back77")
async def handle_button(callback: CallbackQuery):
    await callback.message.delete()
    photo = FSInputFile("spit11.jpg")
    await callback.message.answer_photo(photo=photo, caption="оценка времени сна", reply_markup=sleepbot)
    await callback.answer()
#виджет анализ сна
@callbacks_router.callback_query(F.data == "sleeptime")
async def handle_button(callback: CallbackQuery):
    await callback.message.delete()
    photo = FSInputFile("spit11.jpg")
    await callback.message.answer_photo(photo=photo, caption="сколько вам лет", reply_markup=sleeprate)
    await callback.answer()

#13 - 18
@callbacks_router.callback_query(F.data == "sleeprate1111")
async def handle_button(callback: CallbackQuery):
    await callback.message.delete()
    photo = FSInputFile("sleep11.jpg")
    await callback.message.answer_photo(photo=photo, caption="Ваш сон идеален! Продолжайте в том же духе", reply_markup=sleepmenu)
    await callback.answer()
    
#13 - 18
@callbacks_router.callback_query(F.data == "sleeprate3333")
async def handle_button(callback: CallbackQuery):
    await callback.message.delete()
    photo = FSInputFile("sleep11.jpg")
    await callback.message.answer_photo(photo=photo, caption="Вы недоспали норму! Иеальный сон для вашего возвраста 8 - 10 часов", reply_markup=sleepmenu)
    await callback.answer()
#13 - 18
@callbacks_router.callback_query(F.data == "sleeprate2222")
async def handle_button(callback: CallbackQuery):
    await callback.message.delete()
    photo = FSInputFile("sleep11.jpg")
    await callback.message.answer_photo(photo=photo, caption="Спите чуть меньше, идеальный сон для вашего возвраста 8 - 10 часов ", reply_markup=sleepmenu)
    await callback.answer()


#18 - 60
@callbacks_router.callback_query(F.data == "sleeprate444")
async def handle_button(callback: CallbackQuery):
    await callback.message.delete()
    photo = FSInputFile("sleep123.jpg")
    await callback.message.answer_photo(photo=photo, caption="Ваш сон идеален! Продолжайте в том же духе", reply_markup=sleepmenu)
    await callback.answer()
#18 - 60
@callbacks_router.callback_query(F.data == "sleeprate666")
async def handle_button(callback: CallbackQuery):
    await callback.message.delete()
    photo = FSInputFile("sleep123.jpg")
    await callback.message.answer_photo(photo=photo, caption="Вы недоспали норму! Иеальный сон для вашего возвраста 7 - 9 часов", reply_markup=sleepmenu)
    await callback.answer()
#18 - 60
@callbacks_router.callback_query(F.data == "sleeprate555")
async def handle_button(callback: CallbackQuery):
    await callback.message.delete()
    photo = FSInputFile("sleep123.jpg")
    await callback.message.answer_photo(photo=photo, caption="Спите чуть меньше, идеальный сон для вашего возвраста 7 - 9 часов ", reply_markup=sleepmenu)
    await callback.answer()



#61
@callbacks_router.callback_query(F.data == "sleeprate777")
async def handle_button(callback: CallbackQuery):
    await callback.message.delete()
    photo = FSInputFile("sleep123.jpg")
    await callback.message.answer_photo(photo=photo, caption="Ваш сон идеален! Продолжайте в том же духе", reply_markup=sleepmenu)
    await callback.answer()
#61
@callbacks_router.callback_query(F.data == "sleeprate999")
async def handle_button(callback: CallbackQuery):
    await callback.message.delete()
    photo = FSInputFile("sleep22.jpg")
    await callback.message.answer_photo(photo=photo, caption="Вы недоспали норму! Иеальный сон для вашего возвраста 7 - 8 часов", reply_markup=sleepmenu)
    await callback.answer()

#61
@callbacks_router.callback_query(F.data == "sleeprate888")
async def handle_button(callback: CallbackQuery):
    await callback.message.delete()
    photo = FSInputFile("sleep22.jpg")
    await callback.message.answer_photo(photo=photo, caption="Спите чуть меньше, идеальный сон для вашего возвраста 7 - 8 часов ", reply_markup=sleepmenu)
    await callback.answer()






@callbacks_router.callback_query(F.data == "back88")
async def handle_button(callback: CallbackQuery):
    await callback.message.delete()
    photo = FSInputFile("spit11.jpg")
    await callback.message.answer_photo(photo=photo, caption="сколько вам лет", reply_markup=sleeprate)
    await callback.answer()






@callbacks_router.callback_query(F.data == "taimer")
async def handle_button(callback: CallbackQuery):
    await callback.message.delete()
    photo = FSInputFile("taimer.jpg")
    await callback.message.answer_photo(photo=photo, caption="здесь вы можете увидеть таймеры на разное время и использовать их", reply_markup=taimer11)
    await callback.answer()


@callbacks_router.callback_query(F.data == "taimer111")
async def handle_button(callback: CallbackQuery):
    await callback.message.delete()
    await callback.answer("Напоминалка запущена")
    await asyncio.sleep(3)
    photo = FSInputFile("taimer.jpg")
    await callback.message.answer_photo(photo=photo, caption="пол часа прошло")

@callbacks_router.callback_query(F.data == "taimer222")
async def handle_button(callback: CallbackQuery):
    await callback.message.delete()
    await callback.answer("Напоминалка запущена")
    await asyncio.sleep(6)
    photo = FSInputFile("taimer.jpg")
    await callback.message.answer_photo(photo=photo, caption="час прошел")


@callbacks_router.callback_query(F.data == "taimer333")
async def handle_button(callback: CallbackQuery):
    await callback.message.delete()
    await callback.answer("Напоминалка запущена")
    await asyncio.sleep(12)
    photo = FSInputFile("taimer.jpg")
    await callback.message.answer_photo(photo=photo, caption="2 часа прошло")


@callbacks_router.callback_query(F.data == "back116")
async def handle_button(callback: CallbackQuery):
    await callback.message.delete()
    photo = FSInputFile("robot123.jpg")
    await callback.message.answer_photo(photo=photo, caption="Главное меню.", reply_markup=menu11_kb)
    await callback.answer()




@callbacks_router.callback_query(F.data == "back222")
async def handle_button(callback: CallbackQuery):
    await callback.message.delete()
    photo = FSInputFile("spit11.jpg")
    await callback.message.answer_photo(photo=photo, caption="сколько вам лет.", reply_markup=sleeprate)
    await callback.answer()

@callbacks_router.callback_query(F.data == "back999")
async def handle_button(callback: CallbackQuery):
    await callback.message.delete()
    photo = FSInputFile("spit11.jpg")
    await callback.message.answer_photo(photo=photo, caption="сколько вам лет.", reply_markup=sleeprate)
    await callback.answer()

@callbacks_router.callback_query(F.data == "back111")
async def handle_button(callback: CallbackQuery):
    await callback.message.delete()
    photo = FSInputFile("spit11.jpg")
    await callback.message.answer_photo(photo=photo, caption="сколько вам лет.", reply_markup=sleeprate)
    await callback.answer()

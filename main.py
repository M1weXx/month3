from aiogram import Bot, Dispatcher, types, F 
from aiogram.types import Message 
from aiogram.filters import Command 
import logging, asyncio 
from buttons import start_keyboard, start_baza 
from config import token 

bot = Bot(token=token) 
dp = Dispatcher() 
logging.basicConfig(level=logging.INFO) 
 
@dp.message(Command("start")) 
async def start(message: Message): 
    await message.answer(f"Салам алейкум мой золотой {message.from_user.full_name}", reply_markup=start_baza) 
 
@dp.message(F.text == "Нифиговые Товары тут") 
async def product(message: Message): 
    await message.answer("Базару ноль Хорош, Ознакомься", reply_markup=start_keyboard) 
 
@dp.message(F.text=="О нас") 
async def info_about(message:Message): 
    await message.reply_location (latitude=40.493734, longitude=72.778948) 
    await message.answer("О нас,\nWeXStory-магазин смартфонов, основан в 2024 году 8 aвгуста") 
 
@dp.message(F. text=="Контакты") 
async def a(message:Message): 
    await message.reply_contact(phone_number="+996707310531",first_name= 'Azatbek',last_name='Mitalipov') 
 
@dp.message(F. text=="Товары") 
async def products(message:Message): 
    await message.reply_photo("https://www.myphone.kg/cache/files/21867.webp_w400_h400_resize.webp?t=1713210431") 
    await message.answer(""" 
[Iphone 15] 
Экран: 6.1-дюймовый Super Retina XDR дисплей с поддержкой Always-On Display и ProMotion (частота обновления до 120 Гц). 
Процессор: Apple A16 Bionic (тот же, что и в iPhone 14 Pro). 
Камеры: 
Основная: 48 МП (широкоугольная) с апертурой f/1.6. 
Дополнительная: 12 МП (ультраширокоугольная) с апертурой f/2.4. 
Фронтальная: 12 МП с апертурой f/1.9. 
Оперативная память: 6 ГБ. 
Хранилище: 128 ГБ, 256 ГБ, 512 ГБ. 
Аккумулятор: Улучшенная автономность, до 22 часов воспроизведения видео. 
Операционная система: iOS 17. 
Особенности: 
Dynamic Island (динамический остров) на фронтальной части экрана. 
USB-C порт (первый раз в iPhone). 
Поддержка 5G. 
Face ID. 
Влагозащита по стандарту IP68. 
Улучшенные ночные режимы съёмки и функции фотосъёмки. 
""") 
 
    await message.reply_photo("https://www.myphone.kg/cache/files/17378.webp_w800_h800_resize.webp?t=1716474399") 
    await message.answer(""" 
[IPhone 14] 
Экран: 6.1-дюймовый Super Retina XDR дисплей с разрешением 2532x1170 пикселей. 
Процессор: Apple A15 Bionic. 
Камеры: 
Основная: 12 МП (широкоугольная) с апертурой f/1.6. 
Дополнительная: 12 МП (ультраширокоугольная) с апертурой f/2.4. 
Фронтальная: 12 МП с апертурой f/1.9. 
Оперативная память: 6 ГБ. 
Хранилище: 128 ГБ, 256 ГБ, 512 ГБ. 
Аккумулятор: До 20 часов воспроизведения видео. 
Операционная система: iOS 16. 
Особенности: 
Поддержка 5G. 
Face ID. 
Влагозащита по стандарту IP68. 
 
""") 
     
    await message.reply_photo("https://www.myphone.kg/cache/files/7685.jpg_w800_h800_resize.jpg?t=1716479671") 
    await message.answer (""" 
[IPhone 11] 
Экран: 6.1-дюймовый Liquid Retina HD дисплей с разрешением 1792x828 пикселей. 
Процессор: Apple A13 Bionic. 
Камеры: 
Основная: Двойная камера 12 МП (широкоугольная, апертура f/1.8) + 12 МП (ультраширокоугольная, апертура f/2.4). 
Фронтальная: 12 МП с апертурой f/2.2. 
Оперативная память: 4 ГБ. 
Хранилище: 64 ГБ, 128 ГБ, 256 ГБ. 
Аккумулятор: До 17 часов воспроизведения видео. 
Операционная система: Изначально iOS 13, поддерживает обновления до новейших версий iOS. 
Особенности: 
Поддержка Face ID. 
Влагозащита по стандарту IP68. 
Поддержка ночного режима и 4K видеосъёмки. 
""") 
     
back_1=[ 
    [types.KeyboardButton(text="Назад")] 
] 
back_w1 = types.ReplyKeyboardMarkup(keyboard=back_1, resize_keyboard=True) 
 
 
@dp.message(F. text=="Заказать") 
async def order(message:Message): 
    buuton = [[types.KeyboardButton(text='Мои данные', request_contact=True)]] 
    keyboard = types.ReplyKeyboardMarkup(keyboard=buuton, resize_keyboard=True) 
    await message.reply("Пожалуйста, отправьте свои контактные данные", reply_markup=keyboard, ) 
    # await message.reply(f'Вы в главном меню', reply_markup=start_baza) 
 
 
@dp.message(F.contact) 
async def get_conatct(message:Message):
    contact_info = f'Заявка на товар \nИмя: {message.contact.first_name}\nФамилия: {message.contact.last_name}\nТелефон: {message.contact.phone_number} \nID Товара: 11' 
    await bot.send_message(chat_id=-4255458461, text=contact_info) 
    await message.answer("Спасибо, что оставили заявку") 
    await message.answer('Вы вернулись на главное меню', reply_markup=start_keyboard) 
     
 
async def main(): 
    await dp.start_polling(bot) 
 
if __name__ == "__main__": 
    asyncio.run(main()) 
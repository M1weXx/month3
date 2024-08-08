from aiogram import types 
 
start_buttons= [ 
[types.KeyboardButton(text="Товары"), types.KeyboardButton(text="Заказать")], 
[types.KeyboardButton(text="Контакты"), types.KeyboardButton(text="О нас")] 
 
] 
start_keyboard = types.ReplyKeyboardMarkup(keyboard=start_buttons, resize_keyboard=True) 
 
 
 
bazaru_net=[ 
    [types.KeyboardButton(text="Нифиговые Товары тут")] 
] 
start_baza = types.ReplyKeyboardMarkup(keyboard=bazaru_net, resize_keyboard=True)

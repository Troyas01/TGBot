from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton


# КНОПКИ ДЛЯ ТГ БОТА
kb = ReplyKeyboardMarkup(resize_keyboard=True) # !
btn1 = KeyboardButton('screen')  # сделать и отпр скрин
btn2 = KeyboardButton('lockPC')  # lock экрана
btn3 = KeyboardButton('close google')  # закр гуглХром
btn4 = KeyboardButton('open google')  # откр гуглХром
btn5 = KeyboardButton('sleepPC')  # отправить ПК в сон
btn6 = KeyboardButton('sound+10')  # прибавить звук на 10
btn7 = KeyboardButton('sound-10')  # убавить звук на 10
btn8 = KeyboardButton('closekeyb')  # Скрыть клавиатуру(кнопки)

kb.add(btn1, btn2)
kb.row(btn4, btn3)
kb.row(btn7, btn6)
kb.row(btn5)
kb.row(btn8)

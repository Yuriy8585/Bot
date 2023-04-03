from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


kb_main = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)


btn_start = KeyboardButton(text='/start')
btn_help = KeyboardButton(text='/help')
btn_stop = KeyboardButton(text='/stop')
btn_hello = KeyboardButton(text='/text')
btn_location = KeyboardButton(text='/location')
btn_phone = KeyboardButton(text='new_user', request_contact=True)
btn_find = KeyboardButton(text='/find')
btn_cliker = KeyboardButton(text = '/cliker')

kb_main.add(btn_start, btn_help)
kb_main.add(btn_stop, btn_hello)
kb_main.add(btn_location, btn_cliker)
kb_main.add(btn_find, btn_phone)


remover = ReplyKeyboardRemove()


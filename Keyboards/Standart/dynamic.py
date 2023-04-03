from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, Message



def create_kb(message: Message):
    dynamic = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    #if message.text == 'привет':
    btn_name = KeyboardButton(text=f'{message.from_user.first_name}')
    btn_address = KeyboardButton(text=f'{message.from_user.username}')
    btn_message = KeyboardButton(text=f'{message.from_user.added_to_attachment_menu}')
    btn_location = KeyboardButton(text=f'{message.from_user.id}')

    
    dynamic.add(btn_name, btn_address)
    dynamic.add(btn_message, btn_location)
    
    return dynamic


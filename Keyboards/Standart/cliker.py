from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, Message
from Keyboards.dataclick import counter

def create_cliker(message: Message):
    counter.setdefault(message.from_user.id, 0)
    count = counter.get(message.from_user.id)
    cliker = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    btn_cliker = KeyboardButton(text = f'{count}')

    cliker.add(btn_cliker)
    
    return cliker
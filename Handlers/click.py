from loader import dp
from aiogram.types import Message

from Keyboards import create_cliker
from Keyboards.dataclick import counter




@dp.message_handler(commands=['click'])
async def cliker(message: Message):
    if message.text.isdigit():
        counter[message.from_user.id] +=1
    await message.answer('Привет, кликай', reply_markup=create_cliker(message))
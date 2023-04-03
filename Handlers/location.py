from loader import dp
from aiogram.types import Message
from Keyboards import kb_main



@dp.message_handler(commands=['location'])
async def location_command(message: Message):
    user_location = message.location
    if user_location:
        latitude = user_location.latitude
        longitude = user_location.longitude
        await message.answer(f'Ваше местохождение ({latitude}, {longitude})', reply_markup=kb_main)
    else:
        await message.answer('Поделитесь вашим местонахождением.', reply_markup=kb_main)
   




        

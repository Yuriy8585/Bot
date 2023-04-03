from loader import dp
from aiogram.types import Message
from aiogram.dispatcher import filters
from Keyboards.Standart.dynamic import create_kb



@dp.message_handler(filters.Text('привет'))
async def help_command(message: Message):
    await message.answer(f'И тебе привет',
                         reply_markup=create_kb(message))
'''  
@dp.message_handler()
async def help_command(message: Message):
    await message.answer(f'{message.from_user.first_name}, выберите пункт из списка')'''
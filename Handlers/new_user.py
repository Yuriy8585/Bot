from loader import dp
from aiogram.types import Message
from DataBase import add_new_user, find_user, change_user, delete_user
from Keyboards import kb_main


@dp.message_handler(commands=['new'])
async def add_user(message: Message):
    name, phone, comment, = message.text.split()[1:]
    tg_id = int(message.from_user.id)
    print(name, phone, comment)
    user = (name, tg_id, phone, comment)
    add_new_user(user)

@dp.message_handler(commands=['find'])
async def find_user_command(message: Message):
    name = (message.text.split()[1],)
    result = find_user(name)
    if not result:
        result = 'Пользователь {name} не найден'
    await message.answer(text= result)
    
        

@dp.message_handler(commands=['change'])
async def change_user_command(message: Message):
    name, phone, comment = message.text.split()[1:]
    tg_id = int(message.from_user.id)
    user = (name,phone,comment)
    change_user(user,tg_id)

@dp.message_handler(commands=['delete'])
async def delete_user_command(message: Message):
    name = (message.text.split()[1],)
    tg_id = int(message.from_user.id)
    if tg_id.isdigit():
        delete_user(int(tg_id),)
    else:
        await message.answer('Неверный номер пользователя', reply_markup=kb_main)
    user = (name,tg_id)
    delete_user_command(user)
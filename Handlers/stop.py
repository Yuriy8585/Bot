from loader import dp
from aiogram.types import Message
from Handlers.help import help_helper
from Keyboards import kb_main


@dp.message_handler(commands=['stop'])
def stop_bot(dp):
    
    dp.stop()
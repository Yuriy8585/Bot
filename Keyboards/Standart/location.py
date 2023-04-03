from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, Message

from geopy.geocoders import Nominatim

def add_location(message: Message):
    geolocator = Nominatim(user_agent="my_app")
    location = geolocator.geocode(message.from_user.id)
    latitude = location.latitude
    longitude = location.longitude
    #location = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    btn_location = KeyboardButton(text = f'{message.from_user.username}')

    location.add(btn_location)

    print(latitude, longitude)
    

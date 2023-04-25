from aiogram import types
import requests
from loader import *


@dp.message_handler()
async def random_dog(message: types.Message):
    dog_url = requests.get('https://random.dog/woof.json').json().get('url')
    if dog_url.lower().endswith(('jpg', 'jpeg', 'png')):
        await bot.send_photo(
            chat_id=message.from_user.id,
            photo=dog_url
        )

    elif dog_url.lower().endswith(('mp4', 'gif')):
        await bot.send_video(
            chat_id=message.from_user.id,
            video=dog_url
        )

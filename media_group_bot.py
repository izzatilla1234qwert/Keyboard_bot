"""
This is a echo bot.
It echoes any incoming text messages.
"""

import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = 

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)    
dp = Dispatcher(bot=bot)




@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
     await message.reply("salom")

# @dp.message_handler(commands=['photo'])
# async def send_welcome(message: types.Message):
#     media = types.MediaGroup()
#     media.attach_photo(types.InputFile('maaa.jpg'))
#     media.attach_photo(types.InputFile('maaa2.jpg'))
#     media.attach_photo(types.InputFile('maaa3.jpg'))
#     media.attach_photo(types.InputFile('maaa.jpg'))
#     media.attach_photo(types.InputFile('maaa2.jpg'),caption='TEXT')
#     await message.answer_media_group(media=media)



# @dp.message_handler(commands=['media'])
# async def send_welcome(message: types.Message):
#     media = types.MediaGroup()
#     media.attach_photo(types.InputFile('maaa.jpg'), 'photo1')
#     media.attach_photo(types.InputFile('maaa2.jpg'), 'photo2')
#     media.attach_photo(types.InputFile('maaa3.jpg'), 'photo3')
#     await message.answer_media_group(media=media)

# @dp.message_handler(commands=['document'])
# async def send_welcome(message: types.Message):
#     media = types.MediaGroup()
#     media.attach_document(types.InputFile('bot.py'), 'document1')
#     media.attach_document(types.InputFile('reply_btn.py'), 'document2')
#     await message.answer_media_group(media=media)
#     media.attach_document(types.InputFile('inline_btn.pyx'), 'document3')
# @dp.message_handler(commands=['audio'])
# async def send_welcome(message: types.Message):
#     media = types.MediaGroup()
#     media.attach_audio(types.InputFile('my.m4a'), 'audio1')
#     media.attach_audio(types.InputFile('my.m4a'), 'audio2')
#     await message.answer_media_group(media=media)
    
if __name__ == '__main__':
    executor.start_polling(dp)
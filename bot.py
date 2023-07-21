import logging

from aiogram import Bot, Dispatcher, executor, types
from reply_btn import start_btn
from inline_btn import my_inline_btn


logging.basicConfig(level=logging.INFO)

BOT_TOKEN = "5946381857:AAEGPUPxU-uY4G0PrCeWsDmHCddZuNLvsGA"


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_bot_command(message: types.Message):
    btn = await start_btn()
    await message.answer("Salom", reply_markup=btn)

@dp.message_handler(commands=['inline'])
async def inline_command(messege: types.Message):
    btn = await my_inline_btn()
    await messege.answer('INLINE:',reply_markup=btn)

@dp.message_handler()
async def text_handler(message: types.Message):
    text = message.text
    if text == "Ism":
        ism = message.from_user.first_name
        await message.answer(ism)
        pass
    elif text == "username":
        username = message.from_user.username
        await message.answer(username)
    elif text == "ID":
        id = message.from_user.id
        await message.answer(id)
        pass
    else:
        await message.answer("sss")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
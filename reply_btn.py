from aiogram import types

async def start_btn():
    btn = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=5)
    # btn.add(
    #     types.KeyboardButton('1'),
    #     types.KeyboardButton('2'),
    #     types.KeyboardButton('3'),
    #     types.KeyboardButton('4'),
    #     types.KeyboardButton('5'),
    #     types.KeyboardButton('6'),
    #     types.KeyboardButton('7'),
    #     types.KeyboardButton('8'),
    #     types.KeyboardButton('9'),
    #     types.KeyboardButton('10')
    # )
    btn.row('1')
    btn.row('2','3','4','5','6')
    btn.row('7',)
    btn.row('8','9')
    btn.row('10')
    return btn
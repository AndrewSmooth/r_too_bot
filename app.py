import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart



bot = Bot(token="7091338449:AAER5EguBln8K4m3qvatYefnZBxMlLvBiuM")

dp = Dispatcher() #Этот класс обрабатывает все события


@dp.message(CommandStart()) #фильтрация событий по сообщениям
async def start_cmd(message: types.Message):
    await message.answer('Это была команда старт')

@dp.message() 
async def echo(message: types.Message):
    await message.answer(message.text)



async def main():
    await dp.start_polling(bot)




asyncio.run(main())
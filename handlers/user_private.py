from aiogram import F, types, Router
from aiogram.filters import CommandStart, Command, or_f
from filters.chat_types import ChatTypeFilter

user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(['private']))

@user_private_router.message(CommandStart()) #фильтрация событий по сообщениям
async def start_cmd(message: types.Message):
    await message.answer('Привет, я виртуальный помощник')

@user_private_router.message(F.text.lower() == "меню")
@user_private_router.message(or_f(Command('menu'), (F.text.lower() == "меню"))) 
async def menu_cmd(message: types.Message):
    await message.answer("Вот меню:")

@user_private_router.message(F.text.lower() == 'Меню') #F - магические фильтры
async def menu_cmd(message: types.Message):
    await message.answer("Это магический фильтр")

@user_private_router.message(F.text.lower().contains('доставк'))
@user_private_router.message(Command("shipping"))
async def menu_cmd(message: types.Message):
    await message.answer("Варианты доставки:")
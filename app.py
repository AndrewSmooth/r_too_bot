import asyncio
import os

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

from middlewares.db import DataBaseSession

from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode

from handlers.user_private import user_private_router
from handlers.user_group import user_group_router
from handlers.admin_private import admin_router

from database.engine import create_db, drop_db, session_maker


#Список событий, которые обрабатывает бот
# ALLOWED_UPDATES = ['message, edited_message', 'callback_query']

#Инициализация бота, получение токена из переменных окружения, поддержка форматирования текста в HTML-формате
bot = Bot(token=os.getenv('TOKEN'), parse_mode=ParseMode.HTML)

bot.my_admins_list = []

#Диспетчер отслеживает обновления
dp = Dispatcher()

#подключение роутеров в опрелеленном порядке
dp.include_router(user_private_router)
dp.include_router(user_group_router)
dp.include_router(admin_router) 

async def on_startup(bot):
    # await drop_db()
    await create_db()

async def on_shutdown(bot):
    print('бот лег')


#запуск бота
async def main():
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    dp.update.middleware(DataBaseSession(session_pool=session_maker))

    await bot.delete_webhook(drop_pending_updates=True) #Сброс обновлений, которые бот получал, пока был отключен
    # await bot.delete_my_commands(scope=types.BotCommandScopeAllPrivateChats())  #удаление команд из тг-меню команд
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types()) #запускает отслеживание обновлений

if __name__ == "__main__":
    asyncio.run(main())
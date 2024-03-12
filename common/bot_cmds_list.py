from aiogram.types import BotCommand


private = [ #регистрация команд в меню в лс с ботом
    BotCommand(command='start', description='Запустить бота'),
    BotCommand(command='menu', description='Посмотреть меню'),
    BotCommand(command='about', description='О нас'),
    BotCommand(command='payment', description='Варианты оплаты'),
    BotCommand(command='shipping', description='Варианты доставки'),
]
from aiogram import Bot, Dispatcher, executor
from main import dp


# ЗАПУСК ПРОГРАММЫ
async def on_startup(_):
    print("Bot is starting...")


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
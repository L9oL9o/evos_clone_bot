from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton)
from dotenv import load_dotenv
import os
from buttons import main_menu
from buttons.main_menu import main_menu

dotenv_path = '.env'
load_dotenv(dotenv_path)

API_TOKEN = os.getenv('BOT_TOKEN')
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)



@dp.message_handler(commands="start")
async def start(message: types.Message):
    await message.answer(text="Can we help you ?", reply_markup=main_menu)


if __name__ == '__main__':
    print("bot ishga tushdi")
    executor.start_polling(dp, skip_updates=False)

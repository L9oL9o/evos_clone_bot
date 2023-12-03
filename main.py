from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, ContentTypes)
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
    # await message.answer(text="w", reply_markup=main_menu)
    await bot.send_photo(message.from_user.id,
                         "AgACAgIAAxkBAAN9ZWwRW82ScHfx4akHj1o7RwltOokAAk3PMRuYQmFLHynYJ8VllUEBAAMCAANtAAMzBA",
                         reply_markup=main_menu)


@dp.message_handler(text="Get Photo ID")
async def photo_data(message: types.Message):
    await message.answer(text="Send a photo to get ID of this photo", reply_markup=main_menu)


@dp.message_handler(content_types=ContentTypes.PHOTO)
async def photo_id(message: types.Message):
    await message.answer(message.photo[-1].file_id)
    await message.answer("This is ID of sent photo in Telegram servers")


if __name__ == '__main__':
    print("bot ishga tushdi")
    executor.start_polling(dp, skip_updates=False)

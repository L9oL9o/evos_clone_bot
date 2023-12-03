from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, ContentTypes, message)
from dotenv import load_dotenv
import os
from buttons import main_menu
from buttons.main_menu import main_menu, languages
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
# from evos_main_logics import gif_file_id, company_info

dotenv_path = '.env'
load_dotenv(dotenv_path)

API_TOKEN = os.getenv('BOT_TOKEN')
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def start(message: types.Message):
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


@dp.message_handler(text="Get gif ID")
async def photo_data(message: types.Message):
    await message.answer(text="Send a gif to get ID of this gif", reply_markup=main_menu)


@dp.message_handler(content_types=types.ContentTypes.ANIMATION)
async def handle_animation(message: types.Message):
    # Получаем chat_id пользователя
    chat_id = message.chat.id

    # Отправляем тоже анимацию обратно пользователю
    await bot.send_animation(chat_id, message.animation.file_id, caption="Вы отправили мне GIF", reply_markup=main_menu)
    await message.answer(message.animation.file_id)


gif_file_id = 'CgACAgIAAxkBAAO_ZWwfNJY7S4-qkeziYRmngWKUqgwAAhkzAAKYQmFLgGVcrZ7UZ3AzBA'
company_info = """
Информация о компании:
Сеть ресторанов быстрого обслуживания EVOS® не стоит на месте, а постоянно растет и развивается вместе с вами и для вас!
Мы расширяем свою географию и открываем новые филиалы практически каждый месяц. 
Сейчас в нашей сети насчитывается более 50 филиалов по всему Узбекистану. Поэтому мы всегда в поиске динамичных и 
активных людей, которые хотят стать частью нашей команды и готовы строить свою карьеру в EVOS®. 
EVOS® – это надежный бренд, которому доверяют. Работа в EVOS® – гарантия стабильного заработка и перспективы карьерного
роста. 
Начни свою карьеру в EVOS® уже сейчас!
"""

@dp.message_handler(text="🏢 О компании")
async def about_comp(message: types.Message):
    await bot.send_animation(message.from_user.id, gif_file_id, caption=company_info)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
@dp.message_handler(text="🇺🇿/🇷🇺 Язык")
async def choose_lang(message: types.Message):
    await message.answer(text="Смена языка", reply_markup=languages)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@dp.message_handler(text="🇷🇺 Русский")
async def choose_lang(message: types.Message):
    await message.answer(text="Смена языка", reply_markup=main_menu)

@dp.message_handler(text="🇺🇿 O'zbekcha")
async def choose_lang(message: types.Message):
    await message.answer(text="Смена языка", reply_markup=main_menu)

@dp.message_handler(text="🔙 Назад")
async def choose_lang(message: types.Message):
    await message.answer(text="Смена языка", reply_markup=main_menu)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



if __name__ == '__main__':
    print("bot ishga tushdi")
    executor.start_polling(dp, skip_updates=False)

from dotenv import load_dotenv
import os
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, ContentTypes, message)
# from buttons import main_menu
from buttons.main_menu import *

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


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~BRANCHES~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

branch_text = """
EVOS - крупнейшая фастфуд-компания в Узбекистане. На данный момент открыто 49 торговых точек и современное многопрофильное производство.

Сотрудники компании это большая семья, которая развивается вместе и растет изо дня в день. Компания EVOS расширяется каждый день, сегодня нас более полутора тысяч. Стань частью нашей команды, добро пожаловать в семью EVOS!
"""


@dp.message_handler(text="📍 Филиалы")
async def branches_handler(message: types.Message):
    await bot.send_photo(message.from_user.id,
                         "AgACAgIAAxkBAAIBS2VsVRVh_4FMa8krE2JrOx2lFYk1AAJJ2TEbpsxpS0ZozMeeMa86AQADAgADeAADMwQ",
                         caption=branch_text, reply_markup=branches)


@dp.message_handler(text="☕️ Показать ближайший филиал")
async def near_branch_handler(message: types.Message):
    await message.answer(text="Отправьте свое местоположение для определения ближайшего филиала",
                         reply_markup=near_branch)


@dp.message_handler(content_types=types.ContentTypes.LOCATION)
async def get_location(message: types.Message):
    latitude = message.location.latitude
    longitude = message.location.longitude

    await message.answer(text="""Яккасарайский район, ул.Бобура 40А
+998712031212

📍 Локация (https://maps.google.com/maps?q=41.285560,%2069.253166&ll=41.285560,%2069.253166&z=16)
Дистанция: 0.32 км""")
    await bot.send_photo(message.from_user.id,
                         "AgACAgIAAxkBAAIBkWVsWIg6z2ono_ze0srn1E3_ktMmAAJY2TEbpsxpS_ES0TJoPuFmAQADAgADeAADMwQ",
                         caption="""ул. Шота Руставели, 36
📍 Локация (https://maps.google.com/maps?q=41.289749,%2069.257906&ll=41.289749,%2069.257906&z=16)
Дистанция: 0.60 км""")
    await bot.send_photo(message.from_user.id,
                         "AgACAgIAAxkBAAIBlmVsWQ46RkrCRruOAttxxISvMorfAAJZ2TEbpsxpS6OnR3hIJMQPAQADAgADeQADMwQ",
                         caption="""Узбекистан, Ташкент, ул. Мукими, 7
📍 Локация (https://maps.google.com/maps?q=41.280080,%2069.241594&ll=41.280080,%2069.241594&z=16)
Дистанция: 1.35 км""")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~HEAD OFFICE~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@dp.message_handler(text="🏢 Головной офис")
async def head_office(message: types.Message):
    await bot.send_photo(message.from_user.id,
                         "AgACAgIAAxkBAAIB22VsXRzZUh3muM1QXBTrrvlXQv29AAJ82TEbpsxpS7IStc1V_t-DAQADAgADeQADMwQ",
                         caption="""Адрес:  ул. Фурката 175, 1 подъезд, 4 этаж.
Ориентир: MAKRO THE TOWER""")
    await bot.send_location(message.from_user.id, latitude=.302196, longitude=.248867)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~VACANCIES~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@dp.message_handler(text="💼 Вакансии")
async def vacancies(message: types.Message):
    await message.answer(text="Присоединяйтесь в команду EVOS! \n📍 Выберите регион:", reply_markup=vacanciesss)


@dp.message_handler(text="❌ Отмена ❌")
async def choose_lang(message: types.Message):
    await message.answer(text="Смена языка", reply_markup=main_menu)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~CONTACTS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@dp.message_handler(text="📞 Контакты/Адрес")
async def contact_handler(message: types.Message):
    await bot.send_photo(message.from_user.id,
                         "AgACAgIAAxkBAAIB-GVsatbSikbc1D_Yjd4fuHbj1JntAALF2TEbpsxpSy7uie-e0kWpAQADAgADeAADMwQ",
                         caption="""📍Адрес:  ул. Фурката 175, 1 подъезд, 2 этаж.
📌Ориентир: MAKRO THE TOWER

📲 Контакты: +998 71 203 12 12""")
    await bot.send_location(message.from_user.id, latitude=41.302196, longitude=69.248867 )



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~MENU~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@dp.message_handler(text="📱 Меню")
async def menu_handler(message: types.Message):
    await message.answer(text="")


# ~~~~~~~~~~~~~~~~~~~~~~~~~LANGUAGES HANDLERS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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


@dp.message_handler(text="⬅️ Назад")
async def choose_lang(message: types.Message):
    await message.answer(text="Смена языка", reply_markup=main_menu)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


if __name__ == '__main__':
    print("bot ishga tushdi")
    executor.start_polling(dp, skip_updates=False)

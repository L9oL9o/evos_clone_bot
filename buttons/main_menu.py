from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main_menu = ReplyKeyboardMarkup(
    [
        [KeyboardButton(text="Get Photo ID")],
        [KeyboardButton(text="🏢 О компании"), KeyboardButton("📍 Филиалы")],
        [KeyboardButton(text="💼 Вакансии")],
        [KeyboardButton(text="📱 Меню"), KeyboardButton(text="🗣 Новости")],
        [KeyboardButton(text="📞 Контакты/Адрес"), KeyboardButton(text="🇺🇿/🇷🇺 Язык")],

    ], resize_keyboard=True)



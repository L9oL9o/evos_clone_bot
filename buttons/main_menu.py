from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    [
        [KeyboardButton(text="Get Photo ID"), KeyboardButton(text="Get GIF ID")],
        [KeyboardButton(text="🏢 О компании"), KeyboardButton("📍 Филиалы")],
        [KeyboardButton(text="💼 Вакансии")],
        [KeyboardButton(text="📱 Меню"), KeyboardButton(text="🗣 Новости")],
        [KeyboardButton(text="📞 Контакты/Адрес"), KeyboardButton(text="🇺🇿/🇷🇺 Язык")],

    ], resize_keyboard=True)


branches = ReplyKeyboardMarkup(
    [
        [KeyboardButton("☕️ Показать ближайший филиал")],
        [KeyboardButton("🏢 Головной офис"), KeyboardButton("г. Ташкент")],
        [KeyboardButton("⬅️ Назад")],
    ], resize_keyboard=True)


languages = ReplyKeyboardMarkup(
    [
        [KeyboardButton("🇷🇺 Русский"), KeyboardButton("🇺🇿 O'zbekcha")],
        [KeyboardButton("🔙 Назад")]
    ], resize_keyboard=True
)
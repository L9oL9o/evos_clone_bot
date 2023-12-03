from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    [
        [KeyboardButton(text="Get Photo ID"), KeyboardButton(text="Get GIF ID")],
        [KeyboardButton(text="🏢 О компании"), KeyboardButton("📍 Филиалы")],
        [KeyboardButton(text="💼 Вакансии")],
        [KeyboardButton(text="📱 Меню"), KeyboardButton(text="🗣 Новости")],
        [KeyboardButton(text="📞 Контакты/Адрес"), KeyboardButton(text="🇺🇿/🇷🇺 Язык")],

    ], resize_keyboard=True)

vacanciesss = ReplyKeyboardMarkup(
    [
        [KeyboardButton(text="Ташкент"), KeyboardButton(text="Андижан")],
        [KeyboardButton(text="Коканд"), KeyboardButton(text="Наманган")],
        [KeyboardButton(text="Ташкентская область"), KeyboardButton(text="Самарканд")],
        [KeyboardButton(text="Фергана"), KeyboardButton(text="Хорезмская область")],
        [KeyboardButton(text="Наваи")],
        [KeyboardButton(text="❌ Отмена ❌"), KeyboardButton(text="⬅️ Назад")],

    ], resize_keyboard=True)

branches = ReplyKeyboardMarkup(
    [
        [KeyboardButton(text="☕️ Показать ближайший филиал")],
        [KeyboardButton(text="🏢 Головной офис"), KeyboardButton(text="г. Ташкент")],
        [KeyboardButton(text="⬅️ Назад")],
    ], resize_keyboard=True)

languages = ReplyKeyboardMarkup(
    [
        [KeyboardButton(text="🇷🇺 Русский"), KeyboardButton(text="🇺🇿 O'zbekcha")],
        [KeyboardButton(text="⬅️ Назад")]
    ], resize_keyboard=True
)


near_branch = ReplyKeyboardMarkup(
    [
        [KeyboardButton(text="📍Отправить геолокацию", request_location=True)],
        [KeyboardButton(text="⬅️ Назад")]
    ], resize_keyboard=True
)
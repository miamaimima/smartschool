from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
        KeyboardButton(text='👤 Профиль')
        ],
        [
        KeyboardButton(text='🏫 Наш проект')
        ],
        [
        KeyboardButton(text='🔴 Меню школы'),
        KeyboardButton(text='🟢 Ссылки')
        ],
         
    ],
    resize_keyboard=True,
    input_field_placeholder="Главное меню"
)

registr = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text="Регистрация", callback_data="rg")]]
)


back = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text="Назад")]
    ],
    resize_keyboard=True
)

ggmenu = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text="Главное меню")]
    ],
    resize_keyboard=True


)



menuforrod = ReplyKeyboardMarkup(
    keyboard=[
        [
        KeyboardButton(text='👤 Профиль'),
        KeyboardButton(text='🐙 Мой ребенок')
        ],
        [
        KeyboardButton(text='🏫 Наш проект')
        ],
        [
        KeyboardButton(text='🔴 Меню школы'),
        KeyboardButton(text='🟢 Ссылки')
        ],
         
    ],
    resize_keyboard=True,
    input_field_placeholder="Главное меню"
)
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def welcome_keyboard():
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton("📺 Смотреть видео", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ"))
    return kb

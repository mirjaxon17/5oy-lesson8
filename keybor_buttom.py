from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from database import Database

menu_keyword= ReplyKeyboardMarkup([
    [KeyboardButton("Menyu"), KeyboardButton("Dostavka")]
    ], resize_keyboard=True)

menu_detail = ReplyKeyboardMarkup(resize_keyboard=True)
query = "SELECT * FROM menu;"
for i in Database.connect(query, "select"):
    menu_detail.add(KeyboardButton(i[1]))
menu_detail.add(KeyboardButton("Back"))

category_datail = ReplyKeyboardMarkup([
    [KeyboardButton("Evos")],
    [KeyboardButton("Uzum")],
    [KeyboardButton("Yandex")],
    [KeyboardButton("Safiya")],
    [KeyboardButton("Back")],
], resize_keyboard=True)

menu_1 = ReplyKeyboardMarkup([
    [KeyboardButton("Python")],
    [KeyboardButton("Java")],
    [KeyboardButton("Back")],
], resize_keyboard=True)
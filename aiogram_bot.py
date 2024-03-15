import os
from keybor_buttom import menu_keyword, menu_detail, category_datail, menu_1
from database import Database
import logging
from aiogram import Bot, Dispatcher, executor,  types
from dotenv import load_dotenv
load_dotenv()


API_TOKEN = os.getenv("BOT_TOKEN")
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    customer = message.from_user.username
    chat_id = str(message.chat.id)

    chek_query = f"""SELECT * FROM users WHERE chat_id = '{chat_id}'"""  
    if len(Database.connect(chek_query, "select")) >= 1:
        print(len(Database.connect(chek_query, "select")))
        await message.answer(f"HELLO @{customer}", reply_markup= menu_keyword)
    else:
        print(f"{customer} start bot")
        query = f"""INSERT INTO users(first_name, last_name, user_name, chat_id) VALUES('{first_name}', '{last_name}', '{customer}', '{chat_id}')"""
        Database.connect(query, "insert")
        await message.answer(f"Hi @{customer}", reply_markup=menu_keyword)
        print(f"{customer}")
    

@dp.message_handler(commands=['data'])
async def select(message: types.Message):
    chat_id = message.chat.id
    query_select = f"SELECT * FROM users WHERE chat_id = '{chat_id}'"
    data = Database.connect(query_select, "select")
    print(data)
    await message.reply(f"""
        Hi @{data [0][3]}
        First_name: {data[0][1]}
        Last_name: {data[0][2]}""")


# @dp.message_handler()
# async def echo(message: types.Message):
#     await message.answer(message.text)

@dp.message_handler(lambda message: message.text == "Menyu")
async def show_menu(messege: types.Message):
    # action = button_callback_menu.new(action=messege.text)
    await messege.answer("Menyulardan birini tanlang:", reply_markup=menu_detail)

@dp.message_handler(lambda message: message.text == "Dostavka")
async def show_category(messege: types.Message):
    # action = button_callback_menu.new(action=messege.text)
    await messege.answer("Menyulardan birini tanlang:", reply_markup=category_datail)

@dp.message_handler(lambda message: message.text == "Back")
async def back(messege: types.Message):
    # action = button_callback_menu.new(action=messege.text)
    await messege.answer("Menyulardan birini tanlang:", reply_markup=menu_keyword)

@dp.message_handler(lambda message: message.text == "Menyu")
async def menu_01(messege: types.Message):
    # action = button_callback_menu.new(action=messege.text)
    await messege.answer("Menu 1", reply_markup=menu_1)

@dp.message_handler(lambda message: message.text not in ["Curses", "Modules", "Pyhton"])
async def menu_01(messege: types.Message):
    # action = button_callback_menu.new(action=messege.text)
    await messege.answer("Bundey bolim mavjud emas", reply_markup=menu_detail)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

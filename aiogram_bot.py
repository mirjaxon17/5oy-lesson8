import os
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
    chat_id = message.chat.id

    chek_query = f"""SELECT * FROM users WHERE chat_id = '{chat_id}'"""
    if len(Database.connect(chek_query, "select")) >= 1:
        await message.reply(f"HELLO @{customer}")
    else:
        print(f"{customer} start bot")
        query = f"""INSERT INTO users(first_name, last_name, user_name, chat_id) VALUES('{first_name}', '{last_name}', '{customer}', '{chat_id}')"""
        Database.connect(query, "insert")
        await message.reply(f"Hi @{customer}")
        print(f"{customer}")
    

@dp.message_handler(commands=['data'])
async def select(message: types.Message):
    chat_id = message.chat.id
    query_select = f"SELECT * FROM users WHERE chat_id = '{chat_id}'"
    data = Database.connect(query_select, "select")
    print(data)
    await message.reply(f"""
        Hi @{data [0][3]}
        First_name: {data[0] [1]}
        Last_name: {data[0][2]}""")


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

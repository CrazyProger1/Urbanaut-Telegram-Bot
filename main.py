import asyncio
import os

import aiogram
import dotenv
from aiogram import types

dotenv.load_dotenv()

TOKEN = os.getenv("TOKEN")

dispatcher = aiogram.Dispatcher()


@dispatcher.message()
async def message_handler(message: types.Message):
    button = types.InlineKeyboardButton(
        text="test",
        web_app=types.WebAppInfo(url="https://urbanaut.vercel.app/"),
    )
    markup = types.InlineKeyboardMarkup(inline_keyboard=[[button]])

    print(message.from_user)
    await message.reply("Fuck off. I'm busy bot 🤖", reply_markup=markup)


async def main():
    bot = aiogram.Bot(token=TOKEN)
    await dispatcher.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

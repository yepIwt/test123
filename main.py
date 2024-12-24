from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

TOKEN = "7650905335:AAEHJ_vO6tZx9L-rODes6lw6nWt06-vWQyE"
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    button=InlineKeyboardButton(
        text="Open",
        web_app=WebAppInfo(url="https://127.0.0.1")
    )
    markup = InlineKeyboardMarkup(inline_keyboard=[[button]])
    await message.reply("start", reply_markup=markup)


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
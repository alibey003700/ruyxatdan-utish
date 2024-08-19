import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher,F
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from keyboardbutton import main_button


TOKEN = "6068900832:AAESMuQLAP5P1KlLAcjcTndF5d2qt4eSa7E"

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message):
    full_name = message.from_user.full_name
    text = f"Salom {full_name}, Kompyuter va telefonlar botiga hush kelibsiz"
    await message.answer(text,reply_markup=main_button)


@dp.message(F.text=="💁🏻‍♂️ Biz haqimizda")
async def about_as(message:Message):
    about = "      🎉 Welcom       \nWe are The Best Company. Mr alibek"
    photo_link = "https://picjumbo.com/wp-content/uploads/entrepreneur-working-in-the-office-2210x1473.jpg"
    await message.answer_photo(photo=photo_link,caption=about)

@dp.message(F.text=="💻 Computer")
async def computer(message:Message):
    pass

@dp.message(F.text=="☎️ admin")
async def computer(message:Message):
    await message.answer("Admin : @Tursunov_Alibek")

@dp.message(F.text == "📍 joylashuv")
async def send_location(message: Message):
    
    latitude = 40.10230560142951
    longitude = 65.37350311717934
    await message.answer_location(latitude=latitude, longitude=longitude)


async def main():
    global bot
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

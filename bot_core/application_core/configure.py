from decouple import config
from aiogram import Bot
from aiogram.enums import ParseMode

TOKEN = config("BOT_TOKEN")
bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
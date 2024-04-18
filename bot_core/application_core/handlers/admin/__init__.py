from aiogram import Router, F
from aiogram.filters import CommandStart, StateFilter, Command
from bot_core.application_core.filters import ChatTypeFilter, CallBackSettingsData

from . import handler


def admin_router() -> Router:
    admin = Router()
    admin.message.filter(ChatTypeFilter("private"))
    admin.message.register(handler.test_hello, CommandStart())
    admin.message.register(handler.reconnect_to_site, Command("reconnect"))
    return admin
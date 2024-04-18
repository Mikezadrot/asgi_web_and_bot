import asyncio
from aiogram import Bot, Dispatcher, types
from decouple import config
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from bot_core.application_core import handlers
from bot_core.application_core.configure import bot
from bot_core.application_core.websockets_function import default_send


def setup_handlers(dp: Dispatcher) -> None:
    dp.include_router(handlers.admin.admin_router())


async def setup_aiogram(dp: Dispatcher) -> None:
    setup_handlers(dp)


async def aiogram_on_startup_polling(dispatcher: Dispatcher) -> None:
    await setup_aiogram(dispatcher)
    await default_send("Bot start work")


async def aiogram_on_shutdown_polling(dispatcher: Dispatcher, bot: Bot) -> None:
    # return None
    await default_send("Bot stop work")
    await bot.close()  # Вимкнення бота
    await dispatcher.storage.close()  # Закриття сховища (якщо воно використовується)


def main() -> None:
    dp = Dispatcher()
    dp.startup.register(aiogram_on_startup_polling)

    dp.shutdown.register(aiogram_on_shutdown_polling)
    # logger.info("Bot is up and running")
    asyncio.run(dp.start_polling(bot))

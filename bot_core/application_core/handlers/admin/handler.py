from aiogram import html, types, Bot
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from bot_core.application_core.websockets_function import default_send





from bot_core.application_core.configure import bot




async def test_hello(message: types.Message):
    await message.answer(
        text="Hello"
    )


async def reconnect_to_site(message: types.Message):
    try:
        response = await default_send("Bot start work")
        await message.answer(response)
    except Exception as e:
        print(e)
        await message.answer("Something went wrong")

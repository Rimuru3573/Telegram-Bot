from aiogram import Dispatcher, Bot, F
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.client.session.aiohttp import AiohttpSession
import asyncio
from test3 import getzapros
session = AiohttpSession(proxy='http://proxy.server:3128')
class test(StatesGroup):
    text = State()

bot = Bot(token="8158064890:AAHnV1rescW0qKwdKBJOLSjqp2P3MQclTTQ", session=session)
dp = Dispatcher()

async def main():
    await dp.start_polling(bot)


@dp.message(CommandStart())
async def start_command(message: Message):
    await message.answer("хэлоу епта эта дикпик ой дипсик")

@dp.message(F.text != "/start")
async def text(message: Message, state: FSMContext):
    res = await getzapros(message.text)
    await message.answer(res)

if __name__ == "__main__":
    asyncio.run(main())

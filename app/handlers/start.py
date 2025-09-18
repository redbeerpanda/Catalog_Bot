from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart
from app.keyboards.catalog import welcome_keyboard

router = Router(name="start")


@router.message(CommandStart())
async def start_cmd(message: Message):
    text = (
        "<b>👋 Привет!</b>\n\n"
        "Добро пожаловать в <b>каталог товаров</b>!\n"
        "Здесь вы можете просматривать товары и выбирать то, что вам нужно.\n\n"
        "<i>Нажмите кнопку ниже, чтобы открыть каталог:</i>"
    )
    await message.answer(text, reply_markup=welcome_keyboard(), parse_mode="HTML")

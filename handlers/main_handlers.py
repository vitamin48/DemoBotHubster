from aiogram import Router, types, F
from aiogram.types import Message, ReplyKeyboardRemove

from services.queries import get_lexicon
from services.keyboards import create_start_menu_keyboard
from services.keyboards import kb_back

main_router = Router()


@main_router.callback_query(lambda c: c.data == "kb_back")
async def handle_user_info(callback: types.CallbackQuery):
    user = callback.from_user
    text = get_lexicon(lex_key='start')

    await callback.message.edit_text(
        text=text,
        parse_mode="html",
        reply_markup=create_start_menu_keyboard()
    )
    await callback.answer()


@main_router.message(F.text == "🔙 Назад")
async def handle_back_button(message: Message):
    # print('🔙 Назад')
    back_ms = await message.delete()
    ms = await message.answer(
        "Главное меню",
        reply_markup=ReplyKeyboardRemove()  # Скрывает клавиатуру
    )
    res = await ms.delete()
    await message.answer(
        text=get_lexicon(lex_key='start'),
        parse_mode="HTML",
        reply_markup=create_start_menu_keyboard()
    )

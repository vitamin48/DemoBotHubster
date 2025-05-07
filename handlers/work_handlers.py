from aiogram import Router, types
from services.keyboards import get_user_phone_number_and_geo
from services.queries import get_lexicon
from services.keyboards import kb_back
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardRemove

work_router = Router()


@work_router.callback_query(lambda c: c.data == "information_about_you")
async def handle_user_info(callback: types.CallbackQuery):
    user = callback.from_user
    text = get_lexicon(lex_key='information_about_you')

    await callback.message.edit_text(
        text=text,
        parse_mode="html",
        reply_markup=kb_back.as_markup()
    )
    await callback.answer()


@work_router.callback_query(lambda c: c.data == "information_about_bot_users")
async def handle_user_info(callback: types.CallbackQuery):
    user = callback.from_user
    text = get_lexicon(lex_key='information_about_bot_users')
    text2 = get_lexicon(lex_key='information_about_bot_users2')

    await callback.message.edit_text(
        text=text,
        parse_mode="html"
    )
    await callback.message.answer(text=text2,
                                  parse_mode='html',
                                  reply_markup=get_user_phone_number_and_geo())
    await callback.answer()

from aiogram import Router, types
from aiogram import Bot
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardRemove
import asyncio
from datetime import datetime, timedelta
from services.utils import send_logs_by_button

from services.keyboards import get_user_phone_number_and_geo
from services.config import config
from services.queries import get_lexicon, get_user_date_start
from services.keyboards import kb_back, create_back_gift_keyboard, create_back_order_bot_keyboard

from functions.replacing_placeholders import (replace_placeholder_information_about_bot_users,
                                              replace_placeholder)

work_router = Router()


@work_router.callback_query(lambda c: c.data == "information_about_you")
async def handle_user_info(callback: types.CallbackQuery, bot: Bot):
    user = callback.from_user
    text = get_lexicon(lex_key='information_about_you')

    await callback.message.edit_text(
        text=text,
        parse_mode="html",
        reply_markup=kb_back.as_markup()
    )
    await send_logs_by_button(callback_query=callback,
                              bot=bot)
    await callback.answer()


@work_router.callback_query(lambda c: c.data == "information_about_bot_users")
async def handle_user_info(callback: types.CallbackQuery, bot: Bot):
    """👥 Пользователи"""
    # Получаем объект пользователя
    user = callback.from_user
    # Текст Это пример популярных данных...
    text = get_lexicon(lex_key='information_about_bot_users')
    # Текст Дополнительные данные...
    text2 = get_lexicon(lex_key='information_about_bot_users2')
    # Получаем дату старта
    date_start = get_user_date_start(user.id)
    # Формируем словарь с данными пользователя
    user_data = {
        'USER_ID': user.id,
        'FULL_NAME': user.full_name,
        'USERNAME': user.username,
        'BIO': callback.message.chat.bio,
        'BIRTH_DATE': callback.message.chat.birthdate,
        'BOT_START_DATE': date_start
    }
    # При помощи внешней функции формируем текст на основе user_data и шаблона text
    formatted_text = replace_placeholder_information_about_bot_users(text, user_data)

    await callback.message.edit_text(
        text=formatted_text,
        parse_mode="html"
    )
    await asyncio.sleep(5)
    await callback.message.answer(text=text2,
                                  parse_mode='html',
                                  reply_markup=get_user_phone_number_and_geo())
    await send_logs_by_button(callback_query=callback,
                              bot=bot)
    await callback.answer()


@work_router.callback_query(lambda c: c.data == "pricing")
async def handle_user_info(callback: types.CallbackQuery, bot: Bot):
    user = callback.from_user
    text = get_lexicon(lex_key='pricing')

    await callback.message.edit_text(
        text=text,
        parse_mode="html",
        reply_markup=kb_back.as_markup()
    )
    await send_logs_by_button(callback_query=callback,
                              bot=bot)
    await callback.answer()


@work_router.callback_query(lambda c: c.data == "faq")
async def handle_user_info(callback: types.CallbackQuery, bot: Bot):
    user = callback.from_user
    text = get_lexicon(lex_key='faq')

    await callback.message.edit_text(
        text=text,
        parse_mode="html",
        reply_markup=kb_back.as_markup()
    )
    await send_logs_by_button(callback_query=callback,
                              bot=bot)
    await callback.answer()


@work_router.callback_query(lambda c: c.data == "bot_management_commands")
async def handle_user_info(callback: types.CallbackQuery, bot: Bot):
    user = callback.from_user
    text = get_lexicon(lex_key='bot_management_commands')
    user_data = {'USER_ID': user.id}
    defaults = {'USER_ID': 'USER_ID_TO_SEND'}
    formatted_text = replace_placeholder(text, user_data, defaults)

    await callback.message.edit_text(
        text=formatted_text,
        parse_mode="html",
        reply_markup=kb_back.as_markup()
    )
    await send_logs_by_button(callback_query=callback,
                              bot=bot)
    await callback.answer()


@work_router.callback_query(lambda c: c.data == "technical_information")
async def handle_user_info(callback: types.CallbackQuery, bot: Bot):
    user = callback.from_user
    text = get_lexicon(lex_key='technical_information')

    await callback.message.edit_text(
        text=text,
        parse_mode="html",
        reply_markup=create_back_gift_keyboard()
    )
    await send_logs_by_button(callback_query=callback,
                              bot=bot)
    await callback.answer()


@work_router.callback_query(lambda c: c.data == "get_gift")
async def handle_user_info(callback: types.CallbackQuery, bot: Bot):
    user = callback.from_user
    date_start = get_user_date_start(user.id)
    # Преобразуем строку date_start в datetime
    dt = datetime.strptime(date_start, '%Y-%m-%d %H:%M:%S')
    # Добавляем временной интервал
    dt += timedelta(days=5, hours=3)
    # Получаем в исходном формате
    date_promo = dt.strftime('%Y-%m-%d %H:%M')

    # Раздел с placeholder
    text = get_lexicon(lex_key='get_gift')
    user_data = {'BOT_DATE_PROMO': date_promo}
    defaults = {'BOT_DATE_PROMO': 'Нет данных о дате регистрации'}
    formatted_text = replace_placeholder(text, user_data, defaults)

    await callback.message.edit_text(
        text=formatted_text,
        parse_mode="html",
        reply_markup=create_back_order_bot_keyboard()
    )
    await send_logs_by_button(callback_query=callback,
                              bot=bot)
    await callback.answer()


@work_router.callback_query(lambda c: c.data == "order_bot")
async def handle_user_info(callback: types.CallbackQuery, bot: Bot):
    user = callback.from_user
    text = get_lexicon(lex_key='order_bot')

    await callback.message.edit_text(
        text=text,
        parse_mode="html",
        reply_markup=kb_back.as_markup()
    )
    await send_logs_by_button(callback_query=callback,
                              bot=bot)
    await callback.answer()

from aiogram.types import Message, CallbackQuery
from aiogram import Bot

from services.logger import logger
from services.config import config
from services.queries import get_lexicon


def format_message_info(message: Message) -> str:
    """
    Формирует текст на основе объекта Message.
    """
    return (
        f'Пользователь с id={message.chat.id}, ником: @{message.chat.username} и именем: {message.chat.full_name} '
        f'отправил сообщение:\n\n{message.text}\n\n<code>/send {message.chat.id} </code>')


def format_callback_query_info(callback_query: CallbackQuery) -> str:
    """
    Формирует текст на основе объекта CallbackQuery.
    """
    return (f'Пользователь с id={callback_query.message.chat.id}, ником: @{callback_query.message.chat.username}  '
            f'и именем: {callback_query.message.chat.full_name} нажал на кнопку:'
            f'\n\n{callback_query.data}\n\n<code>/send {callback_query.message.chat.id} </code>')


async def handle_callback_query(callback_query: CallbackQuery,
                                bot: Bot,
                                lex_key: str,
                                reply_markup=None):
    """Функция обработки при нажатии кнопок из меню. Лог и отправка"""
    # Отправка сообщения в лог
    await bot.send_message(chat_id=config.logs_chat,
                           text=format_callback_query_info(callback_query),
                           parse_mode='html')

    # Получение текста из лексикона и отправка пользователю
    response_text = get_lexicon(lex_key=lex_key)
    await bot.send_message(chat_id=callback_query.from_user.id, text=response_text, parse_mode='html',
                           reply_markup=reply_markup, disable_web_page_preview=True)


async def send_logs_by_button(callback_query: CallbackQuery,
                              bot: Bot):
    """Функция обработки при нажатии кнопок из меню. Лог и отправка в чат-лог"""
    text = format_callback_query_info(callback_query)
    logger.info(text)
    # Отправка сообщения в лог
    await bot.send_message(chat_id=config.logs_chat,
                           text=text,
                           parse_mode='html', reply_markup=None)

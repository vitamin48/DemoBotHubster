from aiogram import Router, Bot
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import CallbackQuery
from aiogram import F
from aiogram.filters import CommandStart
import asyncio

from services.config import config
from services.logger import logger
from utils.format_message_info import format_message_info, format_callback_query_info
from services.queries import add_user, get_lexicon
from services.keyboards import create_start_menu_keyboard, get_user_phone_number_and_geo

send_command = Router()


# Обработчик команды /start
@send_command.message(CommandStart())
async def start_command(message: Message, bot: Bot):
    add_user(message)
    log_text = f"Пользователь {message.from_user.id} отправил команду /start"
    logger.info(log_text)
    await bot.send_message(chat_id=config.logs_chat, text=format_message_info(message),
                           parse_mode='html')
    await message.answer(text=f'👋 Здравствуйте, {message.from_user.full_name}!')
    await asyncio.sleep(3)
    await message.answer(text=get_lexicon(lex_key='start'),
                         reply_markup=create_start_menu_keyboard(),
                         parse_mode='html')


# Обработчик команды /send
@send_command.message(Command(commands=["send"]))
async def send_message(message: Message, bot: Bot):
    user_id = message.from_user.id
    if user_id in config.admins:
        try:
            # Разделяем текст команды
            command_parts = message.text.split(' ', 2)  # Разделяем по пробелам
            if len(command_parts) < 3:
                await message.answer("Неправильный формат команды. Используйте: /send <chat_id> <текст>")
                return
            chat_id = command_parts[1]
            text = command_parts[2]
            keyboard = InlineKeyboardBuilder()
            if '<btn>' in text:
                # Разделяем сообщение на текст и кнопки
                text, buttons = text.split('<btn>', 1)
                # кнопки в свою очередь тоже разделяем, получаем список из кнопок
                buttons = buttons.split('<btn>')
                # Создаем инлайн-клавиатуру с помощью InlineKeyboardBuilder
                for button in buttons:
                    keyboard.button(text=button, callback_data=f'btn_{button}')
                keyboard.adjust(1)  # Устанавливаем количество кнопок в строке (1 кнопка на строку)
            # Попробуем отправить сообщение
            await bot.send_message(chat_id, text, reply_markup=keyboard.as_markup())
            await message.answer(f"Сообщение отправлено в чат ID {chat_id}: {text}")
            logger.info(f"Сообщение отправлено в чат ID {chat_id} от пользователя {message.from_user.id}: {text}")
        except Exception as exp:
            logger.error(f"Ошибка при отправке сообщения: {exp}")
            await message.answer(f"Произошла ошибка при отправке сообщения: {exp}")
    else:
        await bot.send_message(chat_id=config.logs_chat, text='Кто-то не из админов отправил команду /send',
                               parse_mode='html')


# Хэндлер для обработки нажатий на кнопки
@send_command.callback_query(F.data.startswith("btn_"))
async def button_pressed(callback_query: CallbackQuery, bot: Bot):
    # Извлекаем текст кнопки из callback_data
    button_text = callback_query.data.split("_", 1)[1]

    # Отвечаем на нажатие кнопки
    # await callback_query.answer(f"Вы нажали на кнопку: {button_text}")

    # Дополнительно можно отправить сообщение в чат
    # await bot.send_message(callback_query.from_user.id, f"Вы выбрали: {button_text}")
    await bot.send_message(chat_id=config.logs_chat, text=format_callback_query_info(callback_query),
                           parse_mode='html')
    await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)

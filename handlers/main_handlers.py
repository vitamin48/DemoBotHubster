from aiogram import Router, types
from services.keyboards import get_user_info_keyboard
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardRemove

main_router = Router()


@main_router.callback_query(lambda c: c.data == "information_about_you")
async def handle_user_info(callback: types.CallbackQuery):
    user = callback.from_user

    # Формируем текст с информацией о пользователе
    text = (
        f"👤 <b>Ваши данные:</b>\n\n"
        f"🆔 <b>ID:</b> {user.id}\n"
        f"👤 <b>Имя:</b> {user.full_name}\n"
        f"🔖 <b>Ник:</b> @{user.username if user.username else 'не указан'}\n\n"
    )

    # Отправляем сообщение с клавиатурой
    await callback.message.edit_text(
        text,
        parse_mode="HTML",
        reply_markup=None
    )

    await callback.message.answer(
        "Выберите действие:",
        reply_markup=get_user_info_keyboard()
    )
    await callback.answer()

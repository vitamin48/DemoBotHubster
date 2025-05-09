from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import Router, types
from aiogram.utils.keyboard import ReplyKeyboardBuilder

kb_back = InlineKeyboardBuilder()
kb_back.button(text='⬅️ Назад',
               callback_data=f'kb_back')

kb_cancel = InlineKeyboardBuilder()
kb_cancel.button(text='❌ Отмена',
                 callback_data=f'kb_cancel')


def phone_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Отправить номер телефона",
                            request_contact=True)]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )


def create_start_menu_keyboard():
    """
    Создает инлайн-клавиатуру для главного меню бота
    Возвращает InlineKeyboardMarkup объект
    """
    builder = InlineKeyboardBuilder()

    builder.button(
        text="ℹ️ Информация",
        callback_data="information_about_you"
    )
    builder.button(
        text="👥 Пользователи",
        callback_data="information_about_bot_users"
    )
    builder.button(
        text="💰 Тарифы",
        callback_data="pricing"
    )
    builder.button(
        text="❓ F.A.Q.",
        callback_data="faq"
    )
    builder.button(
        text="⚙️ Команды управления ботом",
        callback_data="bot_management_commands"
    )
    builder.button(
        text="🛠️ Техническая информация",
        callback_data="technical_information"
    )
    builder.button(
        text="🛒 Заказать бота",
        callback_data="order_bot"
    )
    # builder.button(
    #     text="🎁 Получить подарок",
    #     callback_data="get_gift"
    # )

    # Распределяем кнопки по 2 в ряд для лучшего отображения
    builder.adjust(2, 2, 1, 1, 1)

    return builder.as_markup()


def get_user_phone_number_and_geo():
    builder = ReplyKeyboardBuilder()
    builder.button(text="📱 Отправить номер", request_contact=True)
    builder.button(text="📍 Отправить геолокацию", request_location=True)
    builder.button(text="🔙 Назад")
    builder.adjust(1, 1, 1)
    return builder.as_markup(resize_keyboard=True)


def create_back_gift_keyboard():
    """
    Создает инлайн-клавиатуру назад+ЗАКАЗАТЬ БОТА
    Возвращает InlineKeyboardMarkup объект
    """
    builder = InlineKeyboardBuilder()

    builder.button(
        text="🎁 Получить подарок",
        callback_data="get_gift"
    )
    builder.button(
        text="⬅️ Назад",
        callback_data="kb_back"
    )

    # Распределяем кнопки по 2 в ряд для лучшего отображения
    builder.adjust(1, 1)

    return builder.as_markup()


def create_back_order_bot_keyboard():
    """
    Создает инлайн-клавиатуру назад+подарок
    Возвращает InlineKeyboardMarkup объект
    """
    builder = InlineKeyboardBuilder()

    builder.button(
        text="🛒 Заказать бота",
        callback_data="order_bot"
    )
    builder.button(
        text="⬅️ Назад",
        callback_data="kb_back"
    )

    # Распределяем кнопки по 2 в ряд для лучшего отображения
    builder.adjust(1, 1)

    return builder.as_markup()

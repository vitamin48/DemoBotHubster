import sqlite3
from datetime import datetime
from aiogram.types import Message, CallbackQuery

NAME_DB = 'db_bot.db'


# def get_start_data():
#     """
#     Получаем токен, чат для логов и список админов.
#     """
#     with sqlite3.connect(NAME_DB) as conn:
#         cursor = conn.cursor()
#         cursor.execute("SELECT TOKEN_BOT FROM TOKENS_BOT")
#         token = str(cursor.fetchone()[0])
#         cursor.execute("SELECT ADMIN_ID FROM ADMINS_ID")
#         admins_lst = [row[0] for row in cursor.fetchall()]
#         cursor.execute("SELECT LOGS_CHAT_ID FROM LOGS_CHATS_ID")
#         logs_chats_lst = [row[0] for row in cursor.fetchall()]
#     return token, admins_lst, logs_chats_lst


def add_user(message):
    """
    Добавляет нового пользователя в базу данных.
    """
    # Получаем информацию о пользователе
    user = message.from_user
    user_id = user.id
    username = user.username
    first_name = user.first_name
    last_name = user.last_name
    language_code = user.language_code
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    with sqlite3.connect(NAME_DB) as conn:
        cursor = conn.cursor()

        # Вставляем данные о пользователе
        cursor.execute('''
            INSERT OR IGNORE INTO users (date_start, user_id, username, first_name, last_name, language_code)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (date, user_id, username, first_name, last_name, language_code))

        # Сохраняем изменения
        conn.commit()


def get_lexicon(lex_key):
    """Получаем текстовое сообщение на основе ключа и языка"""
    # language_code = message.from_user.language_code
    #
    # # Определяем таблицу на основе кода языка
    # if language_code == 'ru':
    #     table_name = 'lexicon_ru'
    # elif language_code == 'uk':
    #     table_name = 'lexicon_ua'
    # else:
    #     table_name = 'lexicon_en'

    # Подключение к базе данных и выполнение запроса
    with sqlite3.connect(NAME_DB) as conn:
        cursor = conn.cursor()
        cursor.execute(f"SELECT text FROM 'lexicon_ru' WHERE key = ?", (lex_key,))
        result = cursor.fetchone()

        if result:
            return str(result[0])
        else:
            return None


def get_user_date_start(user_id: int):
    """Получает дату начала использования бота (date_start) по user_id

    Args:
        user_id: ID пользователя в Telegram

    Returns:
        Строка с датой в формате 'YYYY-MM-DD HH:MM:SS' или None,
        если пользователь не найден или поле пустое
    """
    with sqlite3.connect(NAME_DB) as conn:
        conn.row_factory = sqlite3.Row  # Для доступа к полям по именам
        cursor = conn.cursor()

        cursor.execute(
            "SELECT date_start FROM users WHERE user_id = ?",
            (user_id,)
        )

        if result := cursor.fetchone():
            return result['date_start'] if result['date_start'] else None

    return None

from typing import Dict, Optional
from datetime import datetime
from html import escape


def replace_placeholder_information_about_bot_users(template: str,
                                                    user_data: Dict[str, Optional[str]]) -> str:
    """Форматирует текст от information_about_bot_users
    с плейсхолдерами, сохраняя HTML-разметку

    Args:
        template: Шаблон текста с плейсхолдерами
        (%USER_ID%, %FULL_NAME% и т.д.)
        user_data: Словарь с данными пользователя

    Returns:
        Отформатированная строка с HTML-разметкой
    """
    # Значения по умолчанию для отсутствующих данных
    defaults = {
        'USER_ID': 'не указано',
        'FULL_NAME': 'не указано',
        'USERNAME': 'не указано',
        'BIO': 'не указано',
        'BIRTH_DATE': 'не указано',
        'BOT_START_DATE': 'не доступно'
    }
    # Безопасная замена плейсхолдеров
    for key, default in defaults.items():
        placeholder = f'%{key}%'
        value = user_data.get(key, default)

        # Экранирование, кроме None (который заменяется на default)
        safe_value = escape(str(value)) if value is not None else default

        # Для username добавляем @ если он есть
        if key == 'USERNAME' and value and value != default:
            safe_value = f'@{safe_value}'

        template = template.replace(placeholder, safe_value)

    return template


def replace_placeholder_bot_management_commands(template: str,
                                                user_data: Dict[str, Optional[str]]) -> str:
    """Форматирует текст от bot_management_commands
    с плейсхолдерами, сохраняя HTML-разметку

    Args:
        template: Шаблон текста с плейсхолдерами
        (%USER_ID%)
        user_data: Словарь с данными пользователя

    Returns:
        Отформатированная строка с HTML-разметкой
    """
    # Значения по умолчанию для отсутствующих данных
    defaults = {'USER_ID': 'USER_ID_TO_SEND'}
    # Безопасная замена плейсхолдеров
    for key, default in defaults.items():
        placeholder = f'%{key}%'
        value = user_data.get(key, default)
        # Экранирование, кроме None (который заменяется на default)
        safe_value = escape(str(value)) if value is not None else default
        template = template.replace(placeholder, safe_value)

    return template

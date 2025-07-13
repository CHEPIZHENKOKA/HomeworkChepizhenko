from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(user_input_number: str) -> str:
    """Функция проверяет тип введенных пользователем данных и использует маску"""
    if user_input_number.lower().startswith("счет"):
        return get_mask_account(user_input_number)
    return get_mask_card_number(user_input_number)


def get_date(user_input_date: str) -> str:
    """Функция преобразует введенную дату в формат ДД.ММ.ГГГГ"""
    if not user_input_date:
        return "Дата не введена"

    try:
        # Извлечь часть с датой (первые 10 символов)
        date_str = user_input_date[:10]
        parts = date_str.split('-')
        if len(parts) != 3:
            return user_input_date
        year, month, day = parts
        return f"{day}.{month}.{year}"
    except:
        return user_input_date


# Пример использования
if __name__ == '__main__':
    user_input_number = input("Введите номер карты или счета: ")
    print(mask_account_card(user_input_number))
    user_input_date = input("Введите дату: ")
    print(get_date(user_input_date))

from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(user_input_number: str) -> str:
    # Копируем входную строку
    result = user_input_number

    # Проверяем, начинается ли строка с "счет" (регистронезависимо)
    if user_input_number.lower().startswith("счет"):
        # Берем последние 20 символов
        number = user_input_number[-20:].strip()
        # Создаем маску для счета: **** и последние 4 цифры
        masked_number = get_mask_account(user_input_number)
        # Заменяем последние 20 символов на маску
        result = user_input_number[:-20] + masked_number
    else:
        # Берем последние 16 символов
        number = user_input_number[-16:].strip()
        # Создаем маску для карты
        masked_number = get_mask_card_number(number)
        # Заменяем последние 16 символов на маску
        result = user_input_number[:-16] + masked_number

    return result


def getdate(user_input_date: str) -> str:
    # Извлекаем дату из строки (первые 10 символов: ГГГГ-ММ-ДД)
    datepart = user_input_date[:10]
    # Разделяем по дефису
    year, month, day = datepart.split('-')
    # Формируем строку в формате ДД.ММ.ГГГГ
    return f"{day}.{month}.{year}"


# Пример использования
if __name__ == '__main__':
    user_input_number = input("Введите номер карты или счета: ")
    print(mask_account_card(user_input_number))
    user_input_date = input("Введите дату: ")
    print(getdate(user_input_date))

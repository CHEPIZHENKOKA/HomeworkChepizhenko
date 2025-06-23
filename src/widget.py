from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(user_input):
    # Копируем входную строку
    result = user_input

    # Проверяем, начинается ли строка с "счет" (регистронезависимо)
    if user_input.lower().startswith("счет"):
        # Берем последние 20 символов
        number = user_input[-20:].strip()
        # Создаем маску для счета: **** и последние 4 цифры
        masked_number = get_mask_account(user_input)
        # Заменяем последние 20 символов на маску
        result = user_input[:-20] + masked_number
    else:
        # Берем последние 16 символов
        number = user_input[-16:].strip()
        # Создаем маску для карты
        masked_number = get_mask_card_number(number)
        # Заменяем последние 16 символов на маску
        result = user_input[:-16] + masked_number

    return result


# Пример использования
if __name__ == '__main__':
    user_input = input("Введите номер карты или счета: ")
    print(mask_account_card(user_input))

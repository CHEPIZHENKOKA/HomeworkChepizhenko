import re


def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты и возвращает маску номера по правилу
        XXXX XX** **** XXXX. Если номер не содержит ровно 16 цифр - возвращает сообщение об ошибке."""
    if not card_number:
        return "Номер счета/карты не введен"

    # Извлечь все цифры из строки
    digits = ''.join(filter(str.isdigit, card_number))

    # Проверка длины номера карты
    if len(digits) != 16:
        return "Введен некорректный номер карты"

    # Форматирование: первые 4, следующие 2, последние 4
    first_4_card_characters = digits[:4]
    middle_2_card_characters = digits[4:6]
    last_4_card_characters = digits[-4:]

    # Сохранение нечисловых символов
    match = re.search(r'\d+', card_number)
    if match:
        start, end = match.span()
        return card_number[
               :start] + f"{first_4_card_characters} {middle_2_card_characters}** **** {last_4_card_characters}" + card_number[
                                                                                                                   end:]
    return f"{first_4_card_characters} {middle_2_card_characters}** **** {last_4_card_characters}"


def get_mask_account(account: str) -> str:
    """Функция принимает на вход номер счета и возвращает маску номера по правилу
        **XXXX. Если номер не содержит ровно 20 цифр - возвращает сообщение об ошибке."""
    if not account:
        return "Номер счета/карты не введен"

    # Извлечь все цифры из строки
    digits = ''.join(filter(str.isdigit, account))

    # Проверка длины номера счета
    if len(digits) != 20:
        return "Введен некорректный номер счета"

    last_four_account_characters = digits[-4:]
    formatted = "**" + last_four_account_characters

    # Сохранение нечисловых символов
    match = re.search(r'\d+', account)
    if match:
        start, end = match.span()
        return account[:start] + formatted + account[end:]
    return formatted


# Пример использования
#if __name__ == '__main__':
#    user_input_card = input("Введите номер карты: ")
#    print(get_mask_card_number(user_input_card))
#
#    user_input_account = input("Введите номер счета: ")
#    print(get_mask_account(user_input_account))
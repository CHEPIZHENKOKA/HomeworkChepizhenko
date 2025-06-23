from typing import Union


def get_mask_card_number(card_number: Union[str, int]) -> str:
    """Функция принимает на вход номер карты в виде числа и возвращает маску номера по правилу
    XXXX XX** **** XXXX"""
    card_str = str(card_number)
    first_four = card_str[:4]
    next_two = card_str[4:6]
    last_four = card_str[-4:]
    masked_card_number = f"{first_four} {next_two}** **** {last_four}"
    return masked_card_number


def get_mask_account(account_number: Union[str, int]) -> str:
    """Функция принимает на вход номер счета в виде числа и возвращает маску номера по правилу
    **XXXX"""
    account_str = str(account_number)
    last_four = account_str[-4:]
    masked_account_number = f"**{last_four}"
    return masked_account_number


if __name__ == '__main__':
    user_input_card = int(input("Введите номер карты: "))
    print(get_mask_card_number(user_input_card))

    user_input_account = int(input("Введите номер счета: "))
    print(get_mask_account(user_input_account))

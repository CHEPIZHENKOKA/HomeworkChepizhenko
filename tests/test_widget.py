import pytest
from src.widget import mask_account_card, get_date

# Тесты для mask_account_card
@pytest.mark.parametrize("input_str, expected", [
    ("Счет 12345678901234567890", "Счет **7890"), # Распознавание счета
    ("Счет 1234567890123456", "Введен некорректный номер счета"), # Распознавание счета
    ("Visa Platinum 1234567890123456", "Visa Platinum 1234 56** **** 3456"),  # Распознавание карты
    ("Maestro 123456789012", "Введен некорректный номер карты"),   # Нестандартная длина карты
    ("Счет 123", "Введен некорректный номер счета"),                               # Короткий счет
    ("", "Номер счета/карты не введен"),                                                 # Пустая строка
])
def test_mask_account_card(input_str, expected):
    assert mask_account_card(input_str) == expected


# Тесты для get_date
@pytest.mark.parametrize("input_date, expected", [
    ("2018-07-11T02:26:18.671407", "11.07.2018"),  # Стандартный формат
    ("2023-01-01T00:00:00.000000", "01.01.2023"),  # Граничная дата
    ("", "Дата не введена"),                                      # Пустая строка
    ("2023-12-31T23:59:59.999999", "31.12.2023"),  # Конец года
    ("invalid-date", "invalid-date"),              # Некорректные данные
])
def test_get_date(input_date, expected):
    assert get_date(input_date) == expected
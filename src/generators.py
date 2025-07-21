from typing import Iterator, Iterable, Dict, Any, Optional, List


def filter_by_currency(transactions: Iterable[Dict[str, Any]],
                       currency: str) -> Iterator[Dict[str, Any]]:
    """Возвращает итератор транзакций с заданной валютой"""
    for transaction in transactions:
        # Получаем вложенные данные о валюте
        operation_amount = transaction.get("operationAmount", {})
        currency_info = operation_amount.get("currency", {})
        currency_code = currency_info.get("code")

        # Проверяем совпадение с заданной валютой
        if currency_code == currency:
            yield transaction


def transaction_descriptions(transactions: Iterable[Dict[str, Any]]) -> Iterator[Optional[str]]:
    """Генератор, возвращающий описания транзакций"""
    for transaction in transactions:
        yield transaction.get("description")


def card_number_generator(start: int, end: int) -> Iterator[str]:
    """Генератор номеров банковских карт в формате XXXX XXXX XXXX XXXX"""
    for num in range(start, end + 1):
        # Пропускаем числа вне допустимого диапазона
        if num < 0 or num > 9999999999999999:
            continue
        card_str: str = str(num).zfill(16)
        yield f"{card_str[:4]} {card_str[4:8]} {card_str[8:12]} {card_str[12:]}"
from typing import List, Dict, Any
from datetime import datetime

transactions_list = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                     {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                     {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                     {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]


def filter_by_state(items: List[Dict[str, Any]], state: str = 'EXECUTED') -> List[Dict[str, Any]]:
    """Функция возвращает новый список словарей, содержащий только те словари, у которых ключ state
 соответствует указанному значению"""
    filtered_items: List[Dict[str, Any]] = []
    for item in items:
        if item.get('state') == state:
            filtered_items.append(item)
    return filtered_items


def sort_by_date(items: List[Dict[str, Any]], ascending: bool = True) -> List[Dict[str, Any]]:
    """Сортирует список словарей по полю 'date'.
    Параметр ascending: True — по возрастанию, False — по убыванию (по умолчанию)."""
    # Определяем порядок сортировки: убывание (reverse=True), если ascending=False
    reverse_order = ascending

    # Функция для получения даты из словаря
    def get_date(item: Dict[str, Any]) -> datetime:

        # Извлекаем первые 10 символов строки даты (ГГГГ-ММ-ДД)
        date_str = item['date'][:10]

        # Преобразуем строку даты в объект datetime
        return datetime.strptime(date_str, '%Y-%m-%d')

    # Сортируем список словарей, используя get_date как ключ
    sorted_by_date = sorted(items, key=get_date, reverse=reverse_order)
    return sorted_by_date


if __name__ == "__main__":
    state_input = input("Введите искомый статус транзакции (EXECUTED или CANCELED): ").upper()
    state = state_input if state_input else 'EXECUTED'  # Используем 'EXECUTED' при пустом вводе
    ascending_input = bool(input("Сортировать по возрастанию даты? (True или False): "))
    ascending = ascending_input if ascending_input else True
    sorted_transactions = filter_by_state(transactions_list, state)

    print(sort_by_date(sorted_transactions, ascending))

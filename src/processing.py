from typing import List, Dict, Any
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


if __name__ == "__main__":
    state_input = input("Введите искомый статус транзакции (EXECUTED или CANCELED): ").upper()
    state = state_input if state_input else 'EXECUTED'  # Используем 'EXECUTED' при пустом вводе
    sorted_transactions = filter_by_state(transactions_list, state)
    print(sorted_transactions)
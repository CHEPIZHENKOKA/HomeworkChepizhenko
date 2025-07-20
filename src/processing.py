from typing import List, Dict, Any

transactions_list = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                     {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                     {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                     {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]


def filter_by_state(data: List[Dict[str, Any]], state: str) -> List[Dict[str, Any]]:
    """Функция возвращает новый список словарей, содержащий только те словари, у которых ключ state
     соответствует указанному значению"""
    return [item for item in data if item.get('state') == state]

def sort_by_date(data: List[Dict[str, Any]], ascending: bool = False) -> List[Dict[str, Any]]:
    """Сортирует список словарей по полю 'date'.
        Параметр ascending: True — по возрастанию, False — по убыванию (по умолчанию)."""
    valid_data = [item for item in data if 'date' in item]
    return sorted(
        valid_data,
        key=lambda x: x['date'],
        reverse=not ascending  # Исправлено: not ascending вместо ascending
    )


# Пример использования
#if __name__ == "__main__":
#    state_input = input("Введите искомый статус транзакции (EXECUTED или CANCELED): ").upper()
#    state = state_input if state_input else 'EXECUTED'  # Используем 'EXECUTED' при пустом вводе
#    ascending_input = bool(input("Сортировать по возрастанию даты? (True или False): "))
#    ascending = ascending_input if ascending_input else False
#    sorted_transactions = filter_by_state(transactions_list, state)
#
#    print(sort_by_date(sorted_transactions, ascending))

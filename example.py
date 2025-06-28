with open('log.txt', 'w', encoding='utf-8') as file:
    file.write('Log Entry 1\n')

# 2. Чтение содержимого файла
with open('log.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print("Содержимое файла после первой записи:")
    print(content)

# 3. Добавление нового лог-сообщения
with open('log.txt', 'a', encoding='utf-8') as file:
    file.write('Log Entry 2\n')

# 4. Чтение содержимого файла после добавления
with open('log.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print("Содержимое файла после добавления нового лог-сообщения:")
    print(content)


("Visa Platinum 7000792289606361"))  # Вывод: Visa Platinum 7000 79 **** 6361
    print(mask_account_card("Maestro 7000792289606361"))  # Вывод: Maestro 7000 79 **** 6361
    print(mask_account_card("Счет 73654108430135874305"))  # Вывод: Счет **** 4305
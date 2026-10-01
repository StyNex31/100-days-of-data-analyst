
# # Запись в файл
# file = open("data.txt", "w", encoding="utf-8")
# file.write("Привет, файл!\n")
# file.close()
#
# # Чтение из файла
# file = open("data.txt", "r", encoding="utf-8")
# content = file.read()
# file.close()
# print(content)

# "w" (write) — открыть на запись; если файла нет, создаётся новый; если есть — содержимое стирается
# "r" (read) — открыть на чтение
# "a" (append) — открыть на дозапись в конец, не стирая старое
# \n — перенос строки
# file.close() — обязательно закрывать файл после работы

# Более безопасный способ (закрывает файл автоматически, даже если будет ошибка):
# with open("data.txt", "w", encoding="utf-8") as file:
#     file.write("Привет!\n")

# # Открытие файла для записи (режим 'w' создаст файл или перезапишет существующий)
# with open("cities_data.txt", "w", encoding="utf-8") as file:
#     for city in cities_ry:
#         # Записываем строку в формате "Название,Население" и переходим на новую строку
#         file.write(f"{city['name']},{city['population']}\n")

# open("cities_data.txt", "w", encoding="utf-8") — создает файл cities_data.txt =>
# => в режиме записи (w). Параметр encoding="utf-8" нужен, чтобы кириллица отображалась корректно.
# with — автоматически закроет файл после завершения работы кода.
# • f"{city['name']},{city['population']}\n" — =>
# => формирует строку нужного формата. Знак \n осуществляет перенос на новую строку.

# # Открытие файла для чтения (режим 'r')
# with open("cities_data.txt", "r", encoding="utf-8") as file:
#     # Читаем все содержимое файла
#     content = file.read()
#
# # Выводим содержимое на экран
# print(content)

# mode="r" — открывает файл исключительно для чтения.
# file.read() — считывает весь текст из файла в одну строковую переменную, сохраняя все переносы строк.


# # Открываем файл для чтения
# with open("cities_data.txt", "r", encoding="utf-8") as file:
#     # Читаем файл построчно с помощью цикла for
#     for line in file:
#         # Убираем невидимый символ переноса строки \n в конце строки
#         clean_line = line.strip()
#
#         # Если строка пустая (например, в конце файла), пропускаем её
#         if not clean_line:
#             continue
#
#         # Разбиваем строку по запятой на две части
#         name, population = clean_line.split(",")
#
#         # Превращаем население из строки в целое число (int)
#         population = int(population)
#
#         # Выводим результат на экран
#         print(f"Город: {name}, Население: {population:,} чел.")















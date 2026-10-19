# day 17

import csv

# Запись
with open("cities.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "population"])   # строка заголовков
    writer.writerow(["Алматы", 2000000])
    writer.writerow(["Астана", 1200000])

# Чтение
with open("cities.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["name"], row["population"])



import csv

# Твой исходный список городов (пример структуры)
cities_py = [
    ["Алматы", 2000000],
    ["Астана", 1200000],
    ["Шымкент", 1100000]
]

# Запись списка в CSV-файл
with open("cities.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)

    # 1. Записываем строку заголовков
    writer.writerow(["name", "population"])

    # 2. Записываем все города из списка за раз
    writer.writerows(cities_py)

print("Файл cities.csv успешно создан и заполнен!")

import csv

# Чтение CSV-файла через DictReader
with open("cities.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    print("Список городов из файла:")
    print("-" * 25)

    for row in reader:
        # Ключи "name" и "population" автоматически берутся из первой строки файла
        name = row["name"]
        population = row["population"]

        print(f"Город: {name} | Население: {population}")

import csv

# Переменная для хранения общей суммы
total_population = 0

# Чтение файла и подсчёт
with open("cities.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        # Превращаем строку в целое число и добавляем к общей сумме
        total_population += int(row["population"])

print(f"Общее население всех городов: {total_population} человек.")

import csv

# Наш настоящий список словарей из Дня 14
cities_py = [
    {"name": "Алматы", "population": 2000000},
    {"name": "Астана", "population": 1200000},
    {"name": "Талдыкорган", "population": 70000}
]

# Запись списка словарей в файл cities.csv
with open("cities.csv", "w", encoding="utf-8", newline="") as file:
    # Используем специальный DictWriter для работы со словарями
    # Обязательно передаем fieldnames — это будущие заголовки (ключи словаря)
    fieldnames = ["name", "population"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    # Записываем строку заголовков на основе fieldnames
    writer.writeheader()

    # Записываем весь список словарей за один раз
    writer.writerows(cities_py)

print("Файл cities.csv успешно создан на основе списка словарей!")

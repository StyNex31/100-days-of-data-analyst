


# Day 14

# def describe_student(student):
#     return student["name"] + " - " + str(student["grade"])
#
# student = {"name": "Тимур", "grade": 85}
# print(describe_student(student))  # Выведет: Тимур - 85
#
# almaty = {'name': 'Almaty', 'population': 2000000}
#
# # Правильная функция по заданию:
# def get_population(city_dict):
#     return city_dict["population"]
#
# # Вызываем функцию для города almaty:
# result = get_population(almaty)
# print(result)  # Выведет: 2000000



# # 1. Функция проверки миллионника
# def is_big_city(city_dict):
#     return city_dict["population"] > 1000000
#
#
# # 2. Список городов (cities_py)
# cities_py = [
#     {"name": "Алматы", "population": 2000000},
#     {"name": "Астана", "population": 1200000},
#     {"name": "Талдыкорган", "population": 300000},
# ]
#
# # 3. Проверка функции для каждого города
# for city in cities_py:
#     status = is_big_city(city)
#     print(f"{city['name']}: {status}")




# # 1. Функция проверки отдельного города (из Задания 2)
# def is_big_city(city_dict):
#     return city_dict["population"] > 1000000
#
#
# # 2. Новая функция для подсчета больших городов в списке
# def count_big_cities(cities_list):
#     count = 0
#     for city in cities_list:
#         if is_big_city(city):  # Используем функцию из Задания 2
#             count += 1
#     return count
#
#
# # 3. Список городов для проверки
# cities_py = [
#     {"name": "Алматы", "population": 2000000},
#     {"name": "Астана", "population": 1200000},
#     {"name": "Талдыкорган", "population": 300000},
# ]
#
# # 4. Вызов функции и вывод результата
# big_cities_count = count_big_cities(cities_py)
# print("Количество больших городов:", big_cities_count)









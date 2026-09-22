# День 6

person = {"name": "Timur", "age": 20, "city": "Almaty"}
print(person["name"])
person["age"] = 21
print(person)

# Список хранит значения по порядковому номеру(индексу)

numbers = [10, 20, 30]
print(numbers[0])  # 10 — обращение по позиции

# Словарь хранит значения по имени(ключу)

person = {"name": "Timur", "age": 20, "city": "Almaty"}
print(person["name"])  # "Ivan" — обращение по ключу, не по позиции

# Словарь в фигурных скобках не в обычных круглых

print(person["name"])  # Timur
print(person["age"])   # 20

# Изменение существующего значения

person["age"] = 21

# Добавление нового ключа

person["job"] = "student"

# Итог

person = {"name": "Timur", "age": 20, "city": "Almaty"}
person["age"] = 21
person["job"] = "student"
print(person)
# {'name': 'Timur', 'age': 21, 'city': 'Almaty', 'job': 'student'}

# Список — как пронумерованные ячейки шкафчика (ячейка №0, №1, №2...).
# Словарь — как шкафчик с наклейками: документы, деньги, ключи — ты ищешь по названию не по номеру

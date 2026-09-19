



expenses = [1500, 3000, 500, 12000, 800]
print("Все траты:", expenses)
print("Общая сумма:", sum(expenses))
print("Самая крупная трата:", max(expenses))

# это дает возможность сложить весь список(list) "sum(expenses)"
# это показывает самое большое число в переменной "max(expenses)"
# это показывает количество чисел в переменной "len(expenses)"

# каждое число внутри переменной имеет свой индекс от 0
print(expenses[0])   # 1500 — первый элемент
print(expenses[1])   # 3000 — второй элемент
print(expenses[-1])  # 800 — последний элемент (удобно для "последняя трата")

expenses = [1500, 3000, 500, 12000, 800]

for expense in expenses:
    if expense < 500:
        print("Мелкая трата:", expense)
    elif expense <= 1500:
        print("Обычная трата:", expense)
    else:
        print("Крупная покупка:", expense)

# Логика если меньше 500 мелкая иначе если ≤1500 обычная(не нужно снова писать >= 500 потому что если бы было меньше 500 сработал бы уже if) иначе (то есть больше 1500) крупная

for expense in expenses:
    if expense > 1000:
        print("Крупная покупка:", expense)
    else:
        print("Обычная трата:", expense)


expenses = [1000, 3333, 222, 55555, 1332, 444, 120, 12]

for expense in expenses:
    if expense > 1500:
        print("Крупная покупка:", expense)
    elif expense > 500:
        print("Обычная трата:", expense)
    else:
        print("Мелкая трата:", expense)






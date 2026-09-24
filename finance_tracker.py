


expenses = [
    {"category": "еда", "amount": 1900, "date": "22.08.2026"},
    {"category": "транспорт", "amount": 240, "date": "22.08.2026"},
    {"category": "еда", "amount": 700, "date": "22.08.2026"},
    {"category": "еда", "amount": 250, "date": "22.08.2026"},
    {"category": "еда", "amount": 4050, "date": "22.08.2026"},
    {"category": "друзья", "amount": 4000, "date": "22.08.2026"},
    {"category": "еда", "amount": 705, "date": "23.08.2026"},
    {"category": "развлечения", "amount": 649, "date": "23.08.2026"},
    {"category": "развлечения", "amount": 56, "date": "23.08.2026"},
    {"category": "развлечения", "amount": 100, "date": "23.08.2026"},
    {"category": "развлечения", "amount": 500, "date": "23.08.2026"},
    {"category": "развлечения", "amount": 98, "date": "23.08.2026"},
    {"category": "друзья", "amount": 4404, "date": "23.08.2026"},
    {"category": "еда", "amount": 1120, "date": "25.08.2026"},
    {"category": "друзья", "amount": 880, "date": "25.08.2026"},
    {"category": "транспорт", "amount": 200, "date": "25.08.2026"},
    {"category": "транспорт", "amount": 200, "date": "25.08.2026"},
    {"category": "развлечения", "amount": 1000, "date": "25.08.2026"},
    {"category": "друзья", "amount": 800, "date": "25.08.2026"},
    {"category": "друзья", "amount": 500, "date": "26.08.2026"},
    {"category": "еда", "amount": 420, "date": "26.08.2026"},
    {"category": "еда", "amount": 8725, "date": "27.08.2026"},
    {"category": "транспорт", "amount": 200, "date": "27.08.2026"},
    {"category": "друзья", "amount": 900, "date": "27.08.2026"},
    {"category": "еда", "amount": 1730, "date": "28.08.2026"},
    {"category": "квартира", "amount": 210000, "date": "28.08.2026"},
    {"category": "друзья", "amount": 3000, "date": "28.08.2026"},
    {"category": "еда", "amount": 680, "date": "28.08.2026"},
    {"category": "транспорт", "amount": 1360, "date": "28.08.2026"},
    {"category": "друзья", "amount": 5000, "date": "29.08.2026"},
]

def sum_by_category(expenses, category):
    total = 0
    for expense in expenses:
        if expense["category"] == category:
            total += expense["amount"]
    return total

def count_levels(expenses):
    small = 0
    normal = 0
    big = 0
    for expense in expenses:
        amount = expense["amount"]
        if amount < 500:
            small += 1
        elif amount < 2000:
            normal += 1
        else:
            big += 1
    print("Мелких:", small)
    print("Обычных:", normal)
    print("Крупных:", big)

def show_menu():
    print("1 - Показать все траты")
    print("2 - Добавить трату")
    print("3 - Сумма по категории")
    print("4 - Статистика по уровням")
    print("5 - Выход")



def add_expense(expenses):
    category = input("Категория: ")
    amount = input("Сумма: ")
    amount = int(amount)
    date = input("Дата: ")
    new_expense = {"category": category, "amount": amount, "date": date}
    expenses.append(new_expense)

def add_multiple_expenses(expenses):
    category = input("Категория: ")
    date = input("Дата: ")
    while True:
        amount = input("Сумма (или 'стоп' чтобы закончить): ")
        if amount == "стоп":
            break
        amount = int(amount)
        new_expense = {"category": category, "amount": amount, "date": date}
        expenses.append(new_expense)

def save_expenses(expenses, filename="expenses.txt"):
    file = open(filename, "w", encoding="utf-8")
    for expense in expenses:
        line = expense["category"] + "," + str(expense["amount"]) + "," + expense["date"] + "\n"
        file.write(line)
    file.close()


while True:
    show_menu()
    choice = input("Выбери действие: ")

    if choice == "1":
        for expense in expenses:
            print(expense["date"], "-", expense["category"], "-", expense["amount"])
    elif choice == "2":
        add_expense(expenses)
    elif choice == "3":
        category = input("Какую категорию посчитать? ")
        print(sum_by_category(expenses, category))
    elif choice == "4":
        count_levels(expenses)
    elif choice == "5":
        print("Выход")
        break
    else:
        print("Неверный выбор, попробуй снова")







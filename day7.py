
expenses = [
    {"category": "еда", "amount": 1900, "date": "22.08.2026"},
    {"category": "транспорт", "amount": 240, "date": "22.08.2026"},
    {"category": "еда", "amount": 700, "date": "22.08.2026"},
    {"category": "еда", "amount": 250, "date": "22.08.2026"},
    {"category": "еда", "amount": 4050, "date": "22.08.2026"},
    {"category": "друзья", "amount": 4000, "date": "22.08.2026"},
]
# def classify_expenses(expenses):
#     for expense in expenses:
#         amount = expense["amount"]
#         if amount < 500:
#             level = "мелкая"
#         elif amount < 2000:
#             level = "обычная"
#         else:
#             level = "крупная"
#         print(expense["date"], "-", expense["category"], "-", expense["amount"], "-", level)
#
# classify_expenses (expenses)



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
count_levels(expenses)

# Использовал части следующего кода из дня 4

# numbers = [1, 2, 3, 4, 5]
# count = 0
# for number in numbers:
#     count += 1
# print(count)








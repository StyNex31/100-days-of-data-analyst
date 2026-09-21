def average(numbers):
    return sum(numbers) / len(numbers)

def total_expenses(expenses):
    total = 0
    for expense in expenses:
        total += expense
    return total

def count_big_expenses(expenses, threshold=1000):
    count = 0
    for expense in expenses:
        if expense > threshold:
            count += 1
    return count

def average_expense(expenses):
    return total_expenses(expenses) / len(expenses)

expenses = [1500, 200, 3000, 400, 1200, 50]

print("Все траты:", expenses)
print("Общая сумма:", total_expenses(expenses))
print("Крупных трат:", count_big_expenses(expenses))
print("Средняя трата:", average_expense(expenses))





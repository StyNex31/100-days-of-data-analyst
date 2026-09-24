# def average(numbers):
#     return sum(numbers) / len(numbers)
#
# def total_expenses(expenses):
#     total = 0
#     for expense in expenses:
#         total += expense
#     return total
#
# def count_big_expenses(expenses, threshold=1000):
#     count = 0
#     for expense in expenses:
#         if expense > threshold:
#             count += 1
#     return count
#
# def average_expense(expenses):
#     return total_expenses(expenses) / len(expenses)
#
# expenses = [1500, 200, 3000, 400, 1200, 50]
#
# print("Все траты:", expenses)
# print("Общая сумма:", total_expenses(expenses))
# print("Крупных трат:", count_big_expenses(expenses))
# print("Средняя трата:", average_expense(expenses))
#
# expense = {"category": "еда", "amount": 5000}
# print(expense["category"])
# print(expense["amount"])
# from finance_tracker import show_menu, choice
# from day4 import count
from finance_tracker import show_menu

# calculator



# print('Привет!')
# name = input('Как твое имя?')
# count = int(input('Сколько оценок ты хочешь?'))
#
# grades = []
# for i in range(count):
#     grade = int(input('Введи свою оценку:'))
#     grades.append(grade)
#
# print(grades)
#
# average = sum(grades) / count
# if average >= 90:
#     print('Отлично')
# elif average >= 60:
#     print('Хорошо')
# else:
#     print('Плохо')
#
# def count_high_grades(grades, threshold=80):
#     count = 0
#     for grade in grades:
#         if grade > threshold:
#             count += 1
#     return count
#
# print("Оценок выше 80:", count_high_grades(grades))




# print('Привет, меня зовут Тимур')

# age = int(input('Сколько тебе лет?'))
# print(age + 10)


# grades = []
# for i in range(5):
#     grade = int(input('Введи 5 чисел'))
#     grades.append(grade)
# print(grades)
# print(sum(grades))



# numbers = []
# for i in range(4):
#     number = int(input('введи 4 числа '))
#     numbers.append(number)
# number_1 = sum(numbers) / len(numbers)
# if number_1 > 50:
#     print('Высокий результат')
# elif number_1 > 20:
#     print('Средний результат')
# else :
#     print('Низкий результат')


#
# numbers = []
# for i in range(6):
#     number = int(input('Введи температуру за 6 дней'))
#     numbers.append(number)
#
# cold_days = 0
# normal_days = 0
# hot_days = 0
#
# for expense in numbers:
#     if expense < 10:
#         cold_days += 1
#     elif expense <= 25:
#         normal_days += 1
#     else:
#         hot_days += 1
#
# print("Холодных дней:", cold_days)
# print("Нормальных дней:", normal_days)
# print("Жарких дней:", hot_days)
#
# if cold_days > normal_days and cold_days > hot_days:
#     print("Больше всего холодных дней")
# elif normal_days > hot_days and normal_days > cold_days:
#     print('Больше всего нормальных дней')
# else:
#     print('Больше всего жарких дней')
#
#
#
#
#
#
#
#
#

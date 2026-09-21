# День 2

numbers = [5, 12, 8, 20, 3]
print(sum(numbers)) #это сумма всех чисел в той или иной переменной
print(max(numbers)) #это показывает максимальное число в переменной
print(len(numbers)) #это показывает количество чисел в переменной
print(min(numbers)) #это показывает минимально число в переменной

# попытка использовать знания из мини проекта finance_tracker

expenses = [120, 1920, 1090, 100, 1200]

print("Сколько я потратил 18.09.2026", sum(expenses))
print("Минимальная трата за день",min(expenses))
print("Максимальная трата за день",max(expenses))
print("Средняя трата",sum(expenses)/len(expenses))

expenses.append(2000)

print(expenses)
print(sum(expenses))




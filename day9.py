
count = int(input('Сколько чисел ты хочешь ввести?'))

numbers = []
for i in range(count):
    number = int(input('ещё одно число'))
    numbers.append(number)

threshold = int(input('Введи порог: '))

count_above = 0

for number in numbers:
    if number > threshold:
        count_above += 1

print(count_above)


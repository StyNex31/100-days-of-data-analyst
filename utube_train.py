# начинаю урок с utube канал "Bot Anica" course name "Python full course for beginner"

#                                      УРОК 4

# Правила названия переменных

# 1. Начинается с буквы или с _
# 2. Может содержать буквы, цифры, _
# 3. Нельзя использовать ключевые слова (if, for, while, etc.)

width = 10
name_0 = "John"
article_title = "My article"

# Правила хорошего тона названия переменных

# Осмысленные названия переменных по типу (width, height, length, etc.)
# Нужно делать названия переменных не сильно длинными
# Если делать название из нескольких слов то писать как myName or my_name (правильнее через _ )

name_1 = "Johannah"
my_age = 19

his_age = my_age

print(id(his_age))
print(id(my_age))

# id показывает момент точнее место той или иной переменной (момент зависит в какое время была написана переменная(в какой момент времени python выделяет этот адрес))
# говоря точнее id дает системе ссылку на место (но сильно надеяться на это не стоит ведь это зависит еще зависит от части оперативной памяти которую он использует)


#                                      УРОК 5


# Типы данных

# int - целые числа (Integer) Просто целые числа может быть как  1 2 3 4 так и -1 -2 -3 -4 или даже 0
# float - числа с плавающий точкой (Float) Число не целым значением
# str - строки (String) Строки слов возможно с числами (для работы с текстом)
# boll - логические значения (Boolean) Boolean в python ставится факт того или иного значения (Пример 'is_married = False' )

age = 25 # int (integer)
height = 1.75 # float (Float)
name_2 = "John" # str (String)
is_married = False # bool (Boolean)
is_student = True #boll (Boolean)

# Виды кавычек для записи значений строковых переменных

#1. ' обычные не отличаются от "
#2. " обычные не отличаются от '
#3.''' можно писать много строчные записи (str(string)) нет разницы от """
#4.""" можно писать много строчные записи (str(string)) нет разницы от '''

"""
То самое чудное мгновение 
Когда я лицезрел твой милый лик 
То чудное мгновение в котором что то умерло
От улыбки твоей, от глаз 
Ну вы поняли
"""

# type() - определяет тип данных

print(type(age))
print(type(height))
print(type(name_2))
print(type(is_married))
print(type(is_student))


#                                      УРОК 6

# Преобразование типов данных

# int() - преобразование типа данных int
# float() - преобразование типа данных float
# str() - преобразование типа данных str
# bool() - преобразование типа данных bool

age = 25 # int (integer)
height = 1.75 # float (Float)
name_2 = "John" # str (String)
is_married = False # bool (Boolean)
is_student = True #boll (Boolean)

# При преобразовании False в float или в int получаем 0 и 0.0 при преобразовании True мы бы получили 1 и 1.0

print(float(age))
print(int(height))
print(bool(name_2))
print(int(is_married))
print(float(is_married))
print(str(is_student))
print(type(str(is_student)))

# Все значения кроме ниже перечисленных дают истинные значения (True)
# 0, '', None, [], (), {} - ложные значения (False)
# [] - пустой список
# () - пустой картеж
# {} - пустой словарь

print(bool(0))
print(bool(""))


#                                      УРОК 7

# Математические операторы

# + - сложение
# - - вычитание
# * - умножение
# / - деление
# ** - возведение в степень
# % - остаток деления
# // - целочесленое деление

number_1 = 7
number_2 = 2

print(number_1 + number_2)
print(number_1 - number_2)
print(number_1 * number_2)
print(number_1 / number_2)
print(number_1 ** number_2)
print(number_1 % number_2)
print(number_1 // number_2)

# Округление

# round(number, ndigits)
# number - число
# ndigits - количество цифр после запятой

print(round(7.75, 1)) # если остаток меньше 0.5 то округления не будет и будет в итоге 7.7
print(round(7.75, 0)) #
print(round(7.75)) # по умолчанию идет ноль поэтому ответ 8 у второго и третьего примера
print(round(7, -1)) # идет округление в десятичном
print(round(7.75, -1)) # идет округление как и выше
print(round(67, -2)) # если брат -2 тогда округление идет до 100


#                                      УРОК 8

# Логические операторы

# not - логическое НЕ
# and - логическое И
# or - логическое ИЛИ

print('\nЛогическое И\n' + '-' * 50) # Выводит True только если оба варианта True если же один или оба варианта False то выводится False
print(True and True)
print(True and False)
print(False and False)

print('\nЛогическое ИЛИ\n' + '-' * 50) # Выводится True если хотя бы один из вариантов True если оба False то выходит False
print(True or True)
print(True or False)
print(False or False)

print('\nЛогическое НЕ\n' + '-' * 50) # Выводит противоположное значение
print(not True)
print(not False)

# Приоритет логических операторов
# not > and > or
print('\nПриоритет логических операторов\n' + '-' * 50)
print(not False or False and False)
print(True or False and False)
print(True or False)
print(True)

# Изменение приоритета с помощью скобок
print('\nИзменение приоритета с помощью скобок\n' + '-' * 50)
print(not (False or (False and False)))
print(not (False or False))
print(not False)
print(True)

# Сравнение чисел
print('\nСравнение чисел\n' + '-' * 50)

# == - равенство (length == 10)
# != - неравенство (length != 10)
# > - больше
# < - меньше
# >= - больше или равно (length >= 10)
# <= - меньше или равно (length <= 10)

print(1 == 1)
print(1 != 1)
print(1 > 1)
print(1 < 1)
print(1 >= 1)
print(1 <= 1)

# Математическое сравнение и логические операторы
print('\Математические сравнение и логические операторы\n' + '-' * 50)

print(1 < 2 and 2 <3)
print(True and True)
print(True)

print(1 < 2 or 5 <3)
print(True or False)
print(True)

print(not 1 < 2)
print(not True)
print(False)

print(1 < 2 or 5 < 3 and 2 < 3)
print(True or False and True)
print(True or False)
print(True)



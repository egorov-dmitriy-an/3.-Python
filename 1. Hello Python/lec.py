print()
print('---------- Лекция 1 ----------')
# print('Hello \nworld \n2342323')
# a = 2
# b = 3
# c = a + b
# print('a =', a, 'b =',  b, 'c = a + b =', c) # разные стили вывода
# print('c = {2} b = {1} a = {0}'.format(a, b, c)) # формат
# print(f'{c} {b} {a}') # интерполяция
# print('type a =', type (a))


# print ('Выводим массив')
# List = [a, b, c, 'aaaa']
# print (List)


# print('Введите f')
# f = int(input())
# print('Введите d')
# d = int(input())
# print(f+d)


# print(a/b)    # деление
# print(a//b)   # целочисленное деление
# print(a % b)  # остаток от деления
# print(2**5)   # возведение в степень
# c = round(a/b, 6) # окргуление до 6 знака


# a = 3
# a *= 5 = a * 5 # сокращенный оператор присваивания

# >, >=, <, <=, ==, !=
# not, and, or – не путать с &, |, ^
# Кое-что ещё: is, is not, in, not in


# a = 1 > 3
# print(a)


# сравнение списков
# a = [1, 3]
# b = [1, 4]
# print(a == b)

# print(3 < 6 > 5) # многоуровневые неравенства

# print(3 < 4 and 5 > 6) # логическое И
# print(3 < 4 or 5 > 6) # логическое ИЛИ

# f = [1, 2, 3, 4]  # поиск заначение в списке
# print(2 in f)
# print(not 3 in f)

# is_odd = not f[0] % 2 # определение четности
# print(is_odd)


# if / else
# a = int(input('a = ')) # if / else
# b = int(input('b = '))
# if a > b:
#     print(a)
# else:
#     print(b)


# if / elif / else
# name = input('Введите имя: ')
# if name == 'Маша':
#     print('Ура, это Маша')
# elif name == 'Марина':
#     print('О, Марина')
# elif name == 'Дима':
#     print('Прив Дим')
# else:
#     print('Привет,', name)


# Цикл while
# original = 123456789
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
#     print(inverted)
# else:
#     print('Получилось')
# print(inverted)


# Цикл for
# for i in 1, 2, 10, 4, 5:
#     print(i**3)

# list = [1, 2, 3, 6, 8]
# for i in list:
#     print(i*10)

# Создание range
# r = range(10)  # набор от 0 до 9 - десять чисел
# for i in r:
#     print(i*100)

# Второй вариант
# for i in range(3, 7): # задание интервала
#     print (i**2)

# for i in range(3, 8, 2): # задание интервала с шагом 2
#     print (i**2)

# Вложенные циклы
# line = ""
# for i in range(3):
#     line = ""
#     for j in range(5):
#         line += "a" + ' '
#     print(line)


# Цикл for в строке
# for i in 'd-i m-a':
#     print (i)


# Немного о строках
# text = 'съешь ещё этих мягких французских булок'
# print(len(text)) # 39 - длина строки
# print('ещё' in text) # True - содержится "ещё" в тексте
# print(text.isdigit()) # False - проверка являются ли все символы - числами 
# print(text.islower()) # True - проверка являются ли все символы нижнего регистра
# print(text.replace('ещё','ЕЩЁ')) # замена местами
# for c in text:
#     print(c)


# print(text[0]) # c
# print(text[1]) # ъ
# print(text[len(text)-1]) # к
# print(text[-5]) # б
# print(text[:]) # print(text)
# print(text[:2]) # съ
# print(text[len(text)-2:]) # ок
# print(text[2:9]) # ешь ещё
# print(text[6:-18]) # ещё этих мягких
# print(text[0:len(text):6]) # сеикакл
# print(text[::6]) # сеикакл
# text = text[2:9] + text[-5] + text[:2] # ...


# Список – пронумерованная, изменяемая коллекция
# объектов произвольных типов
# Списки: введение
# numbers = [1, 2, 3, 4, 5]
# print(numbers)  # [1, 2, 3, 4, 5]
# numbers = list(range(1, 6))
# print(numbers)  # [1, 2, 3, 4, 5]
# numbers[0] = 10
# print(numbers)  # [10, 2, 3, 4, 5]
# for i in numbers:
#     i *= 2
#     print(i)  # [20, 4, 6, 8, 10]
# print(numbers)  # [10, 2, 3, 4, 5]


# Список строк
# colors = ['red', 'green', 'blue']
# for e in colors:
#     print(e) # red green blue
# for e in colors:
#     print(e*2) # redred greengreen blueblue
# colors.append('gray') # добавить в конец
# print(colors == ['red', 'green', 'blue', 'gray']) # True
# colors.remove('red') #del colors[0] # удалить элемент
# print (colors)


# # Функции
# def f(x):
#     return x**2

# def f(x):
#     if x == 1:
#         return 'Целое'
#     elif x == 2.3:
#         return 23
#     else:
#         return
# print(f(1)) # Целое
# print(f(2.3)) # 23
# print(f(28)) # None
# print(type(f(1))) # str
# print(type(f(2.3))) # int
# print(type(f(28))) # NoneType




print('----------- Конец ------------')
print()

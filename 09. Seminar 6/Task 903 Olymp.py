# Задано трехзначное число. Какая цифра в нем больше: первая или последняя?
# Входные данные
# Одно трехзначное число.
# Выходные данные
# Вывести большую из указанных цифр. В случае их равенства вывести знак "=" (без кавычек).

n = int(input())
if n // 100 > n % 10:
    print(n // 100)
elif n // 100 < n % 10:
    print(n % 10)
else:
    print('=')

# На уроках информатики вас, наверное, учили переводить числа из одних систем счисления в другие
# и выполнять другие подобные операции. Пришло время продемонстрировать эти знания.
# Найдите количество единиц в двоичной записи заданного числа.

# Входные данные
# Одно целое число n (0 ≤ n ≤ 2 ∙10^9).

# Выходные данные
# Вывести количество единиц в двоичной записи числа n.

n = int(input())
temp = 0
while n > 0:
    if n % 2 == 1:
        temp += 1
    n //= 2
print(temp)

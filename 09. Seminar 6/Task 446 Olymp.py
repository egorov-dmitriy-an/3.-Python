# Натуральное число m называется ровным делителем числа n, если частное и остаток от деления n на m равны.
# По заданному натуральному числу n найти количество его ровных делителей.
# Входные данные
# Натуральное число n (1 ≤ n ≤ 10^6).
# Выходные данные
# Выведите искомое количество ровных делителей числа n.


n = int(input())
count = 0
for i in range(1, n):
    if n % i == n // i:
        count += 1
print(count)
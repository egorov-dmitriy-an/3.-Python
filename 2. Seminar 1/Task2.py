print()
print('---------- Лекция 1 ----------')

list = [0, 0, 0, 0, 0]
for i in range(0, 5):
    list[i] = int(input(f'Введите элемент {i}: '))

print(list)

a = list[0]

for i in range(1, 5):
    if list[i] > a:
        a = list[i]
print(f'Максимальное значение равно = {a}')
print('----------- Конец ------------')
print()


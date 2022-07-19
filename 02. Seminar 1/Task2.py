print()
print('------------ Лекция 1 ------------')
coll = []
for i in range(0, 5):
    coll.append(int(input(f'Введите элемент {i}: ')))
print(coll)

a = coll[0]



for i in coll[1:]:
    if i > a:
        a = i
print(f'Максимальное значение равно = {a}')
print('------------- Конец --------------')
print()

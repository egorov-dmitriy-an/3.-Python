#Задача 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#Пример:
#- [1.1, 1.2, 3.1, 5, 10.01] => 0.19

coll =[1.1, 1.2, 3.1, 5, 10.01]
print(coll, end =' => ')
new = []
point = 0
for i in coll:
    temp = i - int(i)
    if temp != 0 :
        new.append(temp)
    if str(i)[::-1].find('.') > point:
        point = str(i)[::-1].find('.')

max = new[0]
min = new[0]

for i in new:
    if i > max:
        max = i
    if i < min:
        min = i
print(round(max - min, point))

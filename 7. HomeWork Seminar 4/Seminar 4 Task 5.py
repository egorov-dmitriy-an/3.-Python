# Задача 5. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

from tkinter.font import nametofont


x = open('Seminar_4_Task_4_Polynom_1.txt', 'r')
polynom_1 = x.readline()
x.close()

x = open('Seminar_4_Task_4_Polynom_2.txt', 'r')
polynom_2 = x.readline()
x.close()

def Polypoly(polynom):
    coefList = []
    i = 0
    while True:
        if polynom[i] == '^':
            while str(polynom[i+1]).isdigit() == True:
                polynom = polynom[:i+1] + polynom[i+2:]
        if polynom[i] == '=':
            break
        i += 1

    polynom = polynom[:-1]
    
    numb = ''
    for i in range(0, len(polynom)):
        s = str(polynom[i])
        if s.isdigit() == True:
            numb += s
        elif len(numb) != 0:
            coefList.append(int(numb))
            numb = ''
    return(coefList)

coef_1 = Polypoly(polynom_1)
coef_2 = Polypoly(polynom_2)

delta = len(coef_1) - len(coef_2)
if delta <= 0:
    count = len(coef_1)
    index = len(coef_2)
    result = coef_2
else:
    count = len(coef_2)
    index = len(coef_1)
    result = coef_1

for i in range(0, count):
    differ = index - i - 1
    if delta <= 0:
        result[differ] = result[differ] + coef_1[differ + delta]
    else:
        result[differ] = result[differ] + coef_2[differ - delta]

poly = ''
for i in range(0, index):
    if i == index - 1:
        poly = poly + str(result[i]) + ' = 0'
    elif i == index-2:
        poly = poly + str(result[i]) + 'x' + ' + '
    elif i <= index-2:
        poly = poly + str(result[i]) + 'x^' + str(index - i - 1) + ' + '

f = open('Seminar_4_Task_5_Polynom.txt', 'w+')
f.write(polynom_1 + '\n')
f.write(polynom_2 + '\n')
f.write(poly)
f.close()
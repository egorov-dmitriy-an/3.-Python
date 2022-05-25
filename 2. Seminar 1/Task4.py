n = int(input('Введите число для проверки: '))
if((n % 5 == 0 and n % 10 == 0) or n % 15 == 0) and not n % 30 == 0:
    print('yes')
else:
    print('no')
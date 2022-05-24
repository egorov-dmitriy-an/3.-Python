n = int(input('Введите число N: '))
print ( n, ' -> ',  end=' ')

for i in range(-n, n + 1):
    print ( i,  end=' ')
print()

# print ([i for i in range(-n, n + 1)]) вариант 2
 
# coll =[] вариант 3
# i = -n
# while i != n+1:
#     coll.append(i)
#     i += 1
# print(coll)

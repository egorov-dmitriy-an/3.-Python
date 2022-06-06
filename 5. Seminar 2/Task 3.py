a = 'Напишите программу, удаляющую из текста все слова.'
b = 'Создайте программу, для игры с конфетами человек против человека все слова.'
for i, j in (',', ''), ('.', ''), ('!', ''), ('?', ''), ('-', ''):
    a = a.replace(i, j)
    b = b.replace(i, j)
print(a)
print(b)


words_a = a.split()
words_b = b.split()

c = words_a
d = words_b


for i in c :
    for j in d:
        if i == j:
            words_a.remove(i)
            words_b.remove(j)

print(words_a)
print(words_b)

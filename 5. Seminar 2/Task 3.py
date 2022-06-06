a = 'Напишите программу, удаляющую из текста все слова.'
b = 'Создайте программу, для игры с конфетами человек против человека все слова.'
for i, j in (',', ''), ('.', ''), ('!', ''), ('?', ''), ('-', ''):
    a = a.replace(i, j)
    b = b.replace(i, j)

print(a)
print(b)

words_a = a.split()
words_b = b.split()

len_a = len(words_a)
len_b = len(words_b)

new_c = []

for i in words_a:
    for j in words_b:
        if i == j:
            new_c.append(i)

for i in new_c:
    words_a.remove(i)
    words_b.remove(i)

print(words_a)
print(words_b)

a = " ".join(words_a)
b = " ".join(words_b)

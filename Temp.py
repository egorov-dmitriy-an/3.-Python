# Напишите программу, удаляющую из текста все слова, содержащие "абв".
print()
print('--------------------- Семинар 5 ----------------------')
text = input('Введите текст: ')
words_text = text.split()

def Find_Liter(original):
    for i in original:
        if original.find('а' б ) != -1 or original.find('б') != -1 or original.find('в') != -1: return False
        else: return True
temp = []
for i in words_text:
    if Find_Liter(i) == True:
        temp.append(i)
text_new = " ".join(temp)
print(f'Отсортированный список без слов содержащих "а", "б", "в": {text_new}')
print('----------------------- Конец ------------------------')
print()
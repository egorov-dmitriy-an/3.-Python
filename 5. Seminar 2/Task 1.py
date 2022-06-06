import zipfile                              # импорт модуля zip
import os                                   # импорт модуля для работы с ОС
os.getcwd()                                 # дает абсолютный путь
dir_path = os.getcwd()                      # присвоим переменной путь
os.listdir(dir_path)                        # получаем содержимое папки по указанному пути
os.path.isfile(os.listdir(dir_path)[0])     # проверка является ли файлом или нет
os.path.isfile(os.listdir(dir_path)[1])     # проверка является ли файлом или нет в более глубокой директории
files_path = [file_path for file_path in os.listdir(dir_path) if os.path.isfile(file_path)] # проверяем является ли файлом
zip_path = os.path.join(dir_path, 'new.zip')# указываем адрес для нового архива
zip_file = zipfile.ZipFile(zip_path, 'w')   # собираем архив
for file_path in files_path:                # проходим по всем папкам
    zip_file.write(file_path)               # записываем файлы
zip_file.close                              # закрываем архив
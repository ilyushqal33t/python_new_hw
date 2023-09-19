# Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.

def path(str_):
    path = str_
    name_file = str_.split('/')[-1].split('.')[0]
    file_extension = str_.split('/')[-1].split('.')[1]
    return (path, name_file, file_extension)


str_ = 'Users/mike/Documents/Notes/tasks.md'
print(path(str_))

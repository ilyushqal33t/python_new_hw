# Напишите функцию группового переименования файлов. Она должна:
# принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# принимать параметр количество цифр в порядковом номере.
# принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
# принимать параметр расширение конечного файла.
# принимать диапазон сохраняемого оригинального имени.
# Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
# К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение


import os


def group_rename(new_name: str, extension: str, new_extension: str):
    ser_num = 1
    for file in os.listdir():
        if os.path.isfile(file) and file.split('.')[1] == extension:
            file_name = f'{new_name}{ser_num}.{new_extension}'
            os.rename(file, file_name)
            ser_num += 1

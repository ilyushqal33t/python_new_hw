# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
# Результаты обхода сохраните в файлы json, csv и pickle.
# Для дочерних объектов указывайте родительскую директорию.
# Для каждого объекта укажите файл это или директория.
# Для файлов сохраните его размер в байтах,
# а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.
import json
import os
import csv
import pickle


def dir_size(path):
    full_size = 0
    for root, dir, files in os.walk(path):
        for f in files:
            full_path = os.path.join(root, f)
            full_size += os.path.getsize(full_path)
    return full_size

def walker(path: str = os.getcwd()):
    res = []
    for root, dir, file in os.walk(path):
        for name in file:
            full_path = os.path.join(root, name)
            res.append({'main_dir': root, 'is_dir': False, 'is_file': True, 'size': os.path.getsize(full_path)})

        for name in dir:
            full_path = os.path.join((root, name))
            res.append(({'main_dir': root, 'is_dir': True, 'is_file': False, 'size': dir_size(full_path)}))

    with open('result.json', 'w', encoding='UTF-8') as file:
        json.dump(res, file, indent=2,ensure_ascii=False)

    with open('result.csv', 'w') as csv_file:
        writer = csv.DictWriter(csv_file, dialect='excel-tab', fieldnames=res[0].keys())
        writer.writeheader()
        writer.writerows(res)

    with open('result.pickle', 'wb') as file:
        pickle.dump(res, file)

walker()

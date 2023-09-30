# Напишите следующие функции:
# Нахождение корней квадратного уравнения
# Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.


import cmath
import csv
import json
from random import uniform
from typing import Callable


def decor_find_qdr(func: Callable):
    def wrapper():
        results = []
        with open('lines.csv', 'r', newline='') as file:
            reader = csv.DictReader(file, dialect='excel-tab')
            for row in reader:
                a = row['a']
                b = row['b']
                c = row['c']
                roots = func(float(a), float(b), float(c))
                results.append({'equation': f'{a} * x2 + {b} * x + {c} = 0', 'x1': str(roots[0]), 'x2': str(roots[1])})
        return results

    return wrapper


def decor_json_dump(func: Callable):
    def wrapper():
        result = func()
        with open('result.json', 'w') as f:
            json.dump(result, f, indent=2)
        return result

    return wrapper


@decor_json_dump
@decor_find_qdr
def find_quadratic_equation(a: float, b: float, c: float):
    d = (b ** 2) - (4 * a * c)
    sol1 = (-b - cmath.sqrt(d)) / (2 * a)
    sol2 = (-b + cmath.sqrt(d)) / (2 * a)
    return sol1, sol2


def generate_csv(line_count: int = 100):
    fieldnames = ['a', 'b', 'c']
    with open('lines.csv', 'w', newline='') as file:
        csv_writer = csv.DictWriter(file, dialect='excel-tab', fieldnames=fieldnames)
        csv_writer.writeheader()
        for _ in range(line_count):
            csv_writer.writerow({i: round(uniform(0, 10), 2) for i in fieldnames})


generate_csv(10)
find_quadratic_equation()

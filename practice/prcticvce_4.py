# 1. Напишите функцию, которая принимает строку текста. Вывести функцией каждое слово с новой строки.
# ✔Строки нумеруются начиная с единицы. ✔Слова выводятся отсортированными согласно кодировки Unicode.
# ✔Текст выравнивается по правому краю так, чтобы у самого длинного слова был один пробел между ним и номером строки.

# def my_func(data: str):
#     data_split = data.split()
#     len_max = len(max(data_split, key=len))
#     data_split.sort()

#     for num, word in enumerate(data_split):
#         print(f'{num}. {word:>{len_max}}')

# my_func(input('Введите строку: '))

# 2. Напишите функцию, которая принимает строку текста.
# ✔Сформируйте список с уникальными кодами Unicode каждого символа введённой строки отсортированный по убыванию.

# def my_func(data: str):
#     lst = [ord(i) for i in set(data)]
#     lst.sort(reverse=True)
#     print(lst)


# my_func(input('Введите строку: '))


# 3. ✔Функция получает на вход строку из двух чисел через пробел.
# ✔Сформируйте словарь, где ключом будет символ из Unicode, а значением — целое число.
# ✔Диапазон пар ключ-значение от наименьшего из введённых пользователем чисел до наибольшего включительно.


# def my_func(data: str):
#     lims = sorted(list(map(int, data.split())))
#     dict = {chr(k):k for k in range(lims[0], lims[1] + 1)}
#     print(dict)

# #     # ------------------------------------

# #     # dict = {}
# #     # for i in sorted(data.split()):
# #     #     dict[chr(int(i))] = int(i)
# #     # print(dict)

# my_func(input('Введите строку: '))


# 4. ✔Функция получает на вход словарь с названием компании в качестве ключа и списком с доходами и расходами (3-10 чисел) в качестве значения.
# ✔Вычислите итоговую прибыль или убыток каждой компании.
# Если все компании прибыльные, верните истину, а если хотя бы одна убыточная — ложь.

# import random

# companies = {name: [random.randint(-10000, 10000) for _ in range(random.randint(3, 5 ))]
#               for name in ['adidas', 'nike', 'reebok']}

# def func(dct_comp: dict) -> bool:
#     for i in dct_comp:
#         dct_comp[i] = sum(dct_comp[i])
#     print(dct_comp)
#     return all(map(lambda x: x>0, dct_comp.values()))

# # -------------------------------------------

# # def func(dct_comp: dict) -> bool:
# #     for i in dct_comp.values():
# #         print(sum(i))
# #         if sum(i) < 0:
# #             return False
# #     return True


# print(func(companies))


# 5. ✔Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
# ✔Напишите функцию, которая при запуске заменяет содержимое переменных оканчивающихся на s (кроме переменной из одной буквы s) на None.
# ✔Значения не удаляются, а помещаются в одноимённые переменные без s на конце.

# from typing import Callable

# start = 100
# s = 'letter'
# apples = 25
# codes = 11101010

# def func():
#     temp_dict = {}
#     for item in globals():
#         if not item.startswith('__'):
#             if item.endswith('s') and len(item) > 1:
#                 temp_dict[item[:-1]] = globals()[item]
#                 temp_dict[item] = None
#     globals().update(temp_dict)

# func()
# print(globals())
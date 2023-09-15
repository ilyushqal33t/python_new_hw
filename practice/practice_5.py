# 1. ✔Пользователь вводит строку из четырёх или более целых чисел, разделённых символом “/”.
# Сформируйте словарь, где: ✔второе и третье число являются ключами. ✔первое число является значением для первого ключа.
# ✔четвертое и все возможные последующие числа хранятся в кортеже как значения второго ключа.

# def str_todict(a, b, c, *args):
#     return {b: a, c: args}


# def str_to_dict(str_):
#     a, b, c, *args = str_
#     return {b: a, c: tuple(args)}


# input_ = tuple(
#     map(int, (input(f'введите 4 числа либо больше через "/": ').split("/"))))
# print(str_to_dict(input_))

# 2. ✔Самостоятельно сохраните в переменной строку текста.
# ✔Создайте из строки словарь, где ключ — буква, а значение — код буквы. ✔Напишите преобразование в одну строку.

# def str_to_dict(str: str) -> dict:
#     dict_ = {i: ord(i) for i in str}
#     return dict_


# str = 'Строка тестового текста'
# dict_ = str_to_dict(str)
# print(dict_)


# 3. ✔Возьмите словарь, который вы получили.
#  Сохраните его итераторатор. ✔Далее выведите первые 5 пар ключ-значение, обращаясь к итератору, а не к словарю.

# def str_to_dict(str: str) -> dict:
#     dict_ = {i: ord(i) for i in str}
#     return dict_


# str = 'Строка тестового текста'
# dict_ = str_to_dict(str)
# print(dict_)
# iter_dict = iter(dict_.items())
# print(next(iter_dict))
# print(next(iter_dict))
# print(next(iter_dict))

# 4. ✔Создайте генератор чётных чисел от нуля до 100.
# ✔Из последовательности исключите числа, сумма цифр которых равна 8. ✔Решение в одну строку.

# gen = (i for i in range(0, 101, 2) if sum(map(int, str(i))) != 8)
# # gen = (i for i in range(0, 101, 2) if i//10 + i % 10 != 8)
# print(*gen)

# 5. ✔Напишите программу, которая выводит на экран числа от 1 до 100.
# ✔При этом вместо чисел, кратных трем, программа должна выводить слово «Fizz» ✔Вместо чисел, кратных пяти — слово «Buzz».
# ✔Если число кратно и 3, и 5, то программа должна выводить слово «FizzBuzz». ✔*Превратите решение в генераторное выражение.


# gen = []
# for i in range(1, 101):
#     if not i % 3 and not i % 5:
#         gen.append('FizzBuzz')
#     elif not i % 3:
#         gen.append('Fizz')
#     elif not i % 5:
#         gen.append('Buzz')
#     else:
#         gen.append(i)
# print(gen)
# # ~~~~~~~~~~~~~~~~~~~~~~~
gen_2 = ('FizzBuzz' if not i % 3 and not i % 5 else 'Fizz' if not i %
         3 else 'Buzz' if not i % 5 else i for i in range(1, 101))
print(type(gen_2))


# 6. ✔Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.
# ✔Таблицу создайте в виде однострочного генератора, где каждый элемент генератора — отдельный пример таблицы умножения.
# ✔Для вывода результата используйте «принт» без перехода на новую строку.


# for i in range(2, 11):
#     for j in range(2, 6):
#         print(f'{j} x {i}', ' '*(1 - i//10), f'= {i*j}', end='\t\t')
#     print('')

# print('\n')
# for i in range(2, 11):
#     for j in range(6, 10):
#         print(f'{j} x {i}', ' '*(1 - i//10), f'= {i*j}', end='\t\t')
#     print('')
# print('\n'*2)

# print(*(f'\n {j} x {i}= {i*j}' for j in range(2, 6) for i in range(2, 10)))
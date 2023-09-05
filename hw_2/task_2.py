# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.

from decimal import *
from fractions import Fraction

fraction_1 = input('Введите первую дробь вида "a/b": ')
fraction_2 = input('Введите вторую дробь вида "a/b: ')
num1, denom1 = map(int, fraction_1.split("/"))
num2, denom2 = map(int, fraction_2.split("/"))

sum = f"{num1 * denom2 + num2 * denom1}/{denom1 * denom2}"
mult = f"{num1 * num2}/{denom1 * denom2}"
# print(sum , mult)
mult_fractions = Fraction(num1, denom1) * Fraction(num2, denom2)
sum_fractions = Fraction(num1, denom1) + Fraction(num2, denom2)
print(f'Сумма дробей {fraction_1} и {fraction_2} составляет:{sum}. Произведение - {mult}')
print(f'Проверка модулем fractions: Сумма - {sum_fractions}, произведение - {mult_fractions}')

# ✔ Создайте функцию-генератор. Функция генерирует N простых чисел, начиная с числа 2.
# Для проверки числа на простоту используйте
# правило: «число является простым, если делится
# нацело только на единицу и на себя».


def is_prime(num):
    count = 2
    while (num % count != 0):
        count += 1
        print(count)
    return num == count


# def gPrimes(last):
#     c=1
#     while True:
#         if c>last:
#             return
#         if is_prime(c):
#             yield c
#         c+=1    
 
# primes=list(gPrimes(100))
# print(primes)
print(is_prime(5))

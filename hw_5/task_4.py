# Создайте функцию генератор чисел Фибоначчи
def fibonacci(n):
    fib1, fib2 = 0, 1
    for _ in range(n):
        fib1, fib2 = fib2, fib1 + fib2
        yield fib1



for i in fibonacci(6):
    print(i)
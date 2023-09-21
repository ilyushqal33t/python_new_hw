from random import randint
from random import uniform


L_LIMIT = -1000
H_LIMIT = 1000

def func(lines: int, file_name: str):
    with open(file_name, 'a+') as file:
        for _ in range(lines):
            a = randint(L_LIMIT ,H_LIMIT)
            b = uniform(L_LIMIT, H_LIMIT)
            file.write(f'{a:>4} | {b}\n')

func(10, 'test_file')
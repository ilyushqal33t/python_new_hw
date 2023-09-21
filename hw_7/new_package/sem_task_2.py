import random as rnd
import string


vowels = set('aeiouy')
cons = set(string.ascii_lowercase).difference(vowels)


def random_name():
    len_name = rnd.randint(4, 7)
    name = ''
    for i in range(len_name):
        name += rnd.choice(list(vowels)) if i % 2 else rnd.choice(list(cons))
    return name.title()

def write_names_to_file(count: int, file_name: str):
    with open(file_name, 'a+', encoding='utf-8') as f:
        for _ in range(count):
            f.write(f'{random_name()}\n')

write_names_to_file(6, 'random_name')
# Создайте модуль с функцией внутри.
# Функция получает на вход загадку, список с возможными вариантами отгадок и количество попыток на угадывание.
# Программа возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны
# Добавьте в модуль с загадками функцию, которая принимает на вход строку (текст загадки) и число
# (номер попытки, с которой она угадана).
# Функция формирует словарь с информацией о результатах отгадывания.
# Для хранения используйте защищённый словарь уровня модуля.
# Отдельно напишите функцию, которая выводит результаты угадывания из защищённого словаря в удобном для чтения виде.
# Для формирования результатов используйте генераторное выражение.


import random


_results = {}


def gen_puzzle():
    dict_ = {'Зимой и летом одним цветом': ['ёлка', "ель", "ёлочка"],
            'Висит груша, нельзя скушать': ["лампочка", "лампа", "лампа накаливания"],
            'Не лает, не кусает - в дом не пускает': ["замок", "засов", "щеколда"]}
    while dict_:
        key = random.choice(list(dict_))
        yield key, dict_.pop(key)


def game(count: int):
    global _results
    for puzzle in gen_puzzle():
        riddle, answer = puzzle
        _try = 1
        answer = list(map(lambda x: x.lower(), answer))
        while _try <= count:
            user_answer = input(riddle + ': ').lower()
            if user_answer in answer:
                _results[riddle] = _try
                break
            _try += 1
        else:
            _results[riddle] = 0



def show_results():
    global _results
    result = ['Результаты:']
    max_len = len(max(list(_results), key=len))
    for riddle, count in _results.items():
        result.append(f'{riddle:<{max_len}}: Отгадана с {count} попытки')
    return '\n'.join(result)

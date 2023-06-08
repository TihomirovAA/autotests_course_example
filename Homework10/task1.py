# Напишите генератор generate_random_name(), используя модуль random,
# который генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
# Например при исполнении следующего кода:
# gen = generate_random_name()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# Выводится:
# tahxmckzexgdyt ocapwy
# dxqebbukr jg
# aym jpvezfqexlv
# iuy qnikkgxvxfxtxv

import random
import string


# Здесь пишем код
def generate_random_name(start, end=None):
    if end is None:
        start, end = 0, start
    while start < end:
        letters = string.ascii_lowercase
        rand_string_1 = ''.join(random.choice(letters) for i in range(random.randint(1, 15)))
        rand_string_2 = ''.join(random.choice(letters) for i in range(random.randint(1, 15)))
        yield rand_string_1 + ' ' + rand_string_2
        start += 1


gen = generate_random_name(1, 5)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

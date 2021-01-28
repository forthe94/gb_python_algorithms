"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""

import random
import sys

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

min_element = sys.maxsize
max_element = -sys.maxsize - 1
pos_min = pos_max = -1

for pos, elem in enumerate(array):
    if elem < min_element:
        min_element = elem
        pos_min = pos

    if elem > max_element:
        max_element = elem
        pos_max = pos

print(f'{pos_min=}, {pos_max=}')



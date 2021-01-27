"""
В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
Это два абсолютно разных значения.
"""

import random
import sys

SIZE = 15
MIN_ITEM = -1000
MAX_ITEM = 1000
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

max_element = -sys.maxsize - 1
max_pos = -1

for pos, elem in enumerate(array):
    if elem < 0:
        if elem > max_element:
            max_element = elem
            max_pos = pos

print(max_element)
print(pos)
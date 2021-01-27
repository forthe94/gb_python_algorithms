"""
Определить, какое число в массиве встречается чаще всего.
"""

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

numbers = []
count = []


for pos, elem in enumerate(array):
    if elem not in numbers:
        numbers.append(elem)
        count.append(1)
    else:
        count[numbers.index(elem)] += 1


print(numbers)
print(count)

"""
В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
"""

FIRST_ELEM = 2
LAST_ELEM = 99

FIRST_NUM = 2
LAST_NUM = 9

array = list(range(FIRST_ELEM, LAST_ELEM + 1))

numbers = list(range(FIRST_NUM, LAST_NUM + 1))

count_array = [0 for _ in range(FIRST_NUM, LAST_NUM + 1)]

print(numbers, count_array)

for elem in array:
    for number in numbers:
        if elem % number == 0:
            count_array[number - 2] += 1

print(count_array)

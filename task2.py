"""
Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
"""

import random

N = 100
array = [random.randint(0, 50) for _ in range(N)]
print(array)


def merge(arr1, arr2):
    ret = []
    p1 = 0
    p2 = 0
    while p1 < len(arr1) and p2 < len(arr2):
        if arr1[p1] < arr2[p2]:
            ret.append(arr1[p1])
            p1 += 1
        else:
            ret.append(arr2[p2])
            p2 += 1
    else:
        if p1 < len(arr1):
            ret.extend(arr1[p1:])
        else:
            ret.extend(arr2[p2:])
    return ret


def merge_sort(data):
    if len(data) == 1:
        return data
    split = len(data) // 2
    return merge(merge_sort(data[:split]), merge_sort(data[split:]))


array = merge_sort(array)

print(array)

print(f'Sorted? {all(array[i] <= array[i + 1] for i in range(len(array) - 1))}')

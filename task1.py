"""
Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
"""
import random
N = 10
array = [random.randint(-100, 100) for _ in range(N)]
print(array)


def bubble_sort(array):
    n = 1
    while n < len(array):
        for i in range(len(array) - n):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        n += 1
        # print(array)

bubble_sort(array)
print(array)

print(f'Sorted? {all(array[i] <= array[i+1] for i in range(len(array)-1))}')
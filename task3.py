"""
Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
которые не меньше медианы, в другой — не больше медианы.
"""
import random

M = 2
N = 2 * M + 1
array = [random.randint(-100, 100) for _ in range(N)]


def partition(arr, l, r):
    x = arr[r]
    i = l
    for j in range(l, r):

        if arr[j] <= x:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[r] = arr[r], arr[i]
    return i


# finds the kth position (of the sorted array)
# in a given unsorted array i.e this function
# can be used to find both kth largest and
# kth smallest element in the array.
# ASSUMPTION: all elements in arr[] are distinct
def kthSmallest(arr, l, r, k):
    # if k is smaller than number of
    # elements in array
    if k > 0 and k <= r - l + 1:

        # Partition the array around last
        # element and get position of pivot
        # element in sorted array
        index = partition(arr, l, r)

        # if position is same as k
        if index - l == k - 1:
            return arr[index]

        # If position is more, recur
        # for left subarray
        if index - l > k - 1:
            return kthSmallest(arr, l, index - 1, k)

        # Else recur for right subarray
        return kthSmallest(arr, index + 1, r,
                           k - index + l - 1)
    return INT_MAX


print(array)
# Driver Code
n = len(array)
k = n // 2
print("Медиана равна ", end="")
print(kthSmallest(array, 0, n - 1, k))

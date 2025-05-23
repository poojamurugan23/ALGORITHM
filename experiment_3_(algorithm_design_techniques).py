# -*- coding: utf-8 -*-
"""Experiment : 3 - (Algorithm_Design_Techniques).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1y-Fslv-PlcgU0Fkx_JcZQRpReV05dJ_c
"""

import time
def findMinMax(arr, low, high):
    if low == high:
        return arr[low], arr[low]
    if low + 1 == high:
        return (min(arr[low], arr[high]), max(arr[low], arr[high]))
    mid = (low + high) // 2
    min1, max1 = findMinMax(arr, low, mid)
    min2, max2 = findMinMax(arr, mid + 1, high)
    return (min(min1, min2), max(max1, max2))
def findMaxMin(arr):
    n = len(arr)
    return findMinMax(arr, 0, n - 1)
def time_taken(arr):
    print("Time of my program:")
    s = time.time()
    min_val, max_val = findMaxMin(arr)
    return time.time() - s
arr = [3, 5, 2, 1, 4, 6, 8, 9, 10, 7]
print("Minimum: ", findMaxMin(arr)[0])
print("Maximum: ", findMaxMin(arr)[1])
print("Time taken: ", time_taken(arr))

import random
import time
import matplotlib.pyplot as plt
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr
def time_taken(arr):
    start_time = time.time()
    merge_sort(arr)
    return time.time() - start_time
def plot_graph(n_values, merge_sort_times):
    plt.plot(n_values, merge_sort_times, label="Merge sort")
    plt.xlabel("Number of elements in the list (n)")
    plt.ylabel("Time taken (in seconds)")
    plt.title("Merge sort")
    plt.legend()
    plt.show()
if __name__ == '__main__':
    n_values = [100, 1000, 5000, 10000, 50000, 100000]
    merge_sort_times = [time_taken([random.randint(0, 100) for i in range(n)]) for n in n_values]
    print(n_values)
    print(merge_sort_times)
    plot_graph(n_values, merge_sort_times)

import time
import matplotlib.pyplot as plt
def quick_sort(arr, start, end):
    if start < end:
        pivot = partition(arr, start, end)
        quick_sort(arr, start, pivot - 1)
        quick_sort(arr, pivot + 1, end)
def median_of_three(arr, start, end):
    mid = (start + end) // 2
    a, b, c = arr[start], arr[mid], arr[end]
    if a > b:
        if b > c:
            return mid
        elif a > c:
            return end
        else:
            return start
    else:
        if a > c:
            return start
        elif b > c:
            return end
        else:
            return mid
def partition(arr, start, end):
    pivot_index = median_of_three(arr, start, end)
    arr[pivot_index], arr[end] = arr[end], arr[pivot_index]
    pivot = arr[end]
    i = start - 1
    for j in range(start, end):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1
def time_quick_sort(n):
    arr = [i for i in range(n, 0, -1)]
    start_time = time.time()
    quick_sort(arr, 0, n - 1)
    return time.time() - start_time
n_values = [100, 200, 500, 1000, 2000, 5000, 10000]
times = []
for n in n_values:
    times.append(time_quick_sort(n))
print(n_values)
print(times)
plt.plot(n_values, times, marker='o')
plt.xlabel("Number of elements (n)")
plt.ylabel("Time taken (s)")
plt.title("Quick Sort Performance with Median-of-Three Pivot")
plt.show()
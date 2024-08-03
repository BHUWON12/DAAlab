import time
import matplotlib.pyplot as plt
import random

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def measure_sort_time(n):
    arr = [random.randint(1, 10000) for _ in range(n)]
    start = time.time()
    quicksort(arr)
    end = time.time()
    return (end - start) * 1000

n_values = list(range(100, 2100, 100))
times = [measure_sort_time(n) for n in n_values]

plt.plot(n_values, times, '-o')
plt.xlabel('Number of Elements')
plt.ylabel('Time Taken (milliseconds)')
plt.title('Quick Sort Time Complexity')
plt.grid(True)
plt.show()

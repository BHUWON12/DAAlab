import random
import time
import matplotlib.pyplot as plt

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def measure_time_for_selection_sort(n_values):
    time_taken = []
    
    for n in n_values:
        arr = [random.randint(0, 10000) for _ in range(n)]
        start_time = time.time()
        selection_sort(arr)
        end_time = time.time()
        time_taken.append((end_time - start_time) * 1000)  # Convert to milliseconds
    
    return time_taken

def plot_graph(n_values, time_taken):
    plt.plot(n_values, time_taken, '-o')
    plt.xlabel("Number of Elements (n)")
    plt.ylabel("Time Taken (milliseconds)")
    plt.title("Selection Sort Time Complexity")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    n_values = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]  # Example values for n
    time_taken = measure_time_for_selection_sort(n_values)
    plot_graph(n_values, time_taken)

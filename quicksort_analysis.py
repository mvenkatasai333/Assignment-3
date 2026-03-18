import random
import time
import sys
sys.setrecursionlimit(20000)
# Randomized Quicksort
def randomized_partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
def randomized_quicksort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low < high:
        pi = randomized_partition(arr, low, high)
        randomized_quicksort(arr, low, pi - 1)
        randomized_quicksort(arr, pi + 1, high)
# Deterministic Quicksort
def deterministic_partition(arr, low, high):
    pivot = arr[low]
    i = low + 1
    j = high

    while True:
        while i <= j and arr[i] <= pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break
    arr[low], arr[j] = arr[j], arr[low]
    return j
def deterministic_quicksort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low < high:
        pi = deterministic_partition(arr, low, high)
        deterministic_quicksort(arr, low, pi - 1)
        deterministic_quicksort(arr, pi + 1, high)
# Performance Testing
def measure_sort_time(sort_func, arr):
    start = time.time()
    sort_func(arr)
    end = time.time()
    return end - start
def test_quicksort_performance():
    sizes = [1000, 2000, 5000, 10000]
    array_types = {
        "Random": lambda n: [random.randint(0, n) for _ in range(n)],
        "Sorted": lambda n: list(range(n)),
        "Reverse": lambda n: list(range(n, 0, -1)),
        "Repeated": lambda n: [random.choice([1, 2, 3, 4, 5]) for _ in range(n)]
    }
    for n in sizes:
        for name, generator in array_types.items():
            arr1 = generator(n)
            arr2 = arr1.copy()
            rand_time = measure_sort_time(randomized_quicksort, arr1)
            det_time = measure_sort_time(deterministic_quicksort, arr2)
            print(f"Size={n}, Type={name}: Randomized={rand_time:.4f}s, Deterministic={det_time:.4f}s")
# Main Execution
if __name__ == "__main__":
    print("=== Testing Quicksort Performance ===")
    test_quicksort_performance()
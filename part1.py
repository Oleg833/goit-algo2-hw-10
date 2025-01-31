import time
import random
import numpy as np
import matplotlib.pyplot as plt

# Implementing QuickSort Algorithms
def randomized_quick_sort(arr):
    """Randomized QuickSort using a randomly chosen pivot."""
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)


def deterministic_quick_sort(arr):
    """Deterministic QuickSort using the last element as pivot."""
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return deterministic_quick_sort(left) + middle + deterministic_quick_sort(right)


# Function to measure execution time
def measure_time(sort_function, arr):
    times = []
    for _ in range(5):  # Repeat sorting 5 times for accuracy
        arr_copy = arr.copy()
        start_time = time.time()
        sort_function(arr_copy)
        end_time = time.time()
        times.append(end_time - start_time)
    return np.mean(times)


# Generating test arrays
sizes = [10_000, 50_000, 100_000, 500_000]
results = []

for size in sizes:
    test_array = [random.randint(0, 1_000_000) for _ in range(size)]
    
    rand_time = measure_time(randomized_quick_sort, test_array)
    det_time = measure_time(deterministic_quick_sort, test_array)
    
    results.append([size, rand_time, det_time])

# Printing results in a formatted table
print(f"{'Array Size':<15}{'Randomized QuickSort':<25}{'Deterministic QuickSort':<25}")
print("=" * 65)
for row in results:
    print(f"{row[0]:<15}{row[1]:<25.6f}{row[2]:<25.6f}")

# Plotting results
plt.figure(figsize=(10, 6))
plt.plot([r[0] for r in results], [r[1] for r in results], marker='o', linestyle='-', label="Randomized QuickSort")
plt.plot([r[0] for r in results], [r[2] for r in results], marker='s', linestyle='-', label="Deterministic QuickSort")
plt.xlabel("Array Size")
plt.ylabel("Execution Time (seconds)")
plt.title("Performance Comparison of QuickSort Algorithms")
plt.legend()
plt.grid()
plt.show()

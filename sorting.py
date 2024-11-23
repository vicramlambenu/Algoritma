import random
import time

# Merge Sort Implementation
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursively sort both halves
        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        # Merge the sorted halves
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Copy remaining elements of left_half, if any
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Copy remaining elements of right_half, if any
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Bubble Sort Implementation
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Generate 100 random integers
random_numbers = [random.randint(0, 1000) for _ in range(100)]

# Measure time for Merge Sort
merge_sort_data = random_numbers.copy()
start_time = time.time()
merge_sort(merge_sort_data)
merge_sort_time = time.time() - start_time

# Measure time for Bubble Sort
bubble_sort_data = random_numbers.copy()
start_time = time.time()
bubble_sort(bubble_sort_data)
bubble_sort_time = time.time() - start_time

# Print results
print("Original Data: ", random_numbers)
print("\nSorted with Merge Sort: ", merge_sort_data)
print("Time taken by Merge Sort: {:.6f} seconds".format(merge_sort_time))

print("\nSorted with Bubble Sort: ", bubble_sort_data)
print("Time taken by Bubble Sort: {:.6f} seconds".format(bubble_sort_time))

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

# ---- PSEUDOCODE ----

# FUNCTION MergeSort(array):
#     IF length(array) > 1:
#         mid = length(array) // 2
#         left_half = array[0:mid]
#         right_half = array[mid:length(array)]
#
#         CALL MergeSort(left_half)
#         CALL MergeSort(right_half)
#
#         i = j = k = 0
#         WHILE i < length(left_half) AND j < length(right_half):
#             IF left_half[i] < right_half[j]:
#                 array[k] = left_half[i]
#                 i = i + 1
#             ELSE:
#                 array[k] = right_half[j]
#                 j = j + 1
#             k = k + 1
#
#         WHILE i < length(left_half):
#             array[k] = left_half[i]
#             i = i + 1
#             k = k + 1
#
#         WHILE j < length(right_half):
#             array[k] = right_half[j]
#             j = j + 1
#             k = k + 1
#
# FUNCTION BubbleSort(array):
#     n = length(array)
#     FOR i FROM 0 TO n-1:
#         FOR j FROM 0 TO n-i-2:
#             IF array[j] > array[j+1]:
#                 SWAP(array[j], array[j+1])

# ---- ANALYSIS ----
# Merge Sort Analysis:
#algoritma divide-and-conquer yang membagi array menjadi dua bagian yang lebih kecil, mengurutkan setiap bagian secara rekursif, 
# dan kemudian menggabungkannya menjadi satu array terurut. Kompleksitas waktunya adalah O(n log n) pada kasus terbaik, terburuk, dan rata-rata. 
# Ini karena array dibagi menjadi dua bagian (O(log n)) dan proses penggabungan memerlukan O(n) waktu.
# Merge Sort membutuhkan ruang tambahan O(n) untuk menyimpan hasil penggabungan.
# Bubble Sort Analysis:
#algoritma sederhana yang membandingkan elemen-elemen yang berdekatan dan menukarnya jika mereka tidak dalam urutan yang benar. 
# Kompleksitas waktunya adalah O(n^2) dalam kasus terburuk dan rata-rata, karena membandingkan semua pasangan elemen yang berdekatan. 
# Kasus terbaik adalah O(n), ketika array sudah terurut. Bubble Sort tidak memerlukan ruang tambahan selain beberapa variabel untuk menukar elemen, 
# sehingga kompleksitas ruangnya adalah O(1).


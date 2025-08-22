<<<<<<< HEAD
def insertion_sort(arr):
    n = len(arr)
    for k in range(1, n):
        y = arr[k]
        i = k - 1
        while i >= 0 and y < arr[i]:
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = y

numbers = [9, 3, 7, 6, 2, 8, 5]
print("Original array:", numbers)

insertion_sort(numbers)
=======
def insertion_sort(arr):
    n = len(arr)
    for k in range(1, n):
        y = arr[k]
        i = k - 1
        while i >= 0 and y < arr[i]:
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = y

numbers = [9, 3, 7, 6, 2, 8, 5]
print("Original array:", numbers)

insertion_sort(numbers)
>>>>>>> 45b5ba4 (First Commit)
print("Sorted array:", numbers)
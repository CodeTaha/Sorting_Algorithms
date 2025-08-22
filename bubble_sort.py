def bubble_sort(array):
    n = len(array)
    for pass_num in range(n - 1):
        for i in range(n - pass_num - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]

numbers = [5, 3, 8, 4, 2]
print("Original array:", numbers)

bubble_sort(numbers)
print("Sorted array:", numbers)
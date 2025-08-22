def selection_sort(array):
    n = len(array)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]

numbers = [64, 25, 12, 22, 11]
print("Original array:", numbers)

selection_sort(numbers)
print("Sorted array:", numbers)
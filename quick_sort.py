def quicksort(array, left, right):
    pivot = partition(array, left, right)
    if left < pivot:
        quicksort(array, left, pivot - 1)
    if right > pivot:
        quicksort(array, pivot + 1, right)

def partition(numbers, left, right):
    pivot = numbers[left]

    while left < right:
        while numbers[right] >= pivot and left < right:
            right -= 1
        if left != right:
            numbers[left] = numbers[right]
            left += 1
        while numbers[left] <= pivot and left < right:
            left += 1
        if left != right:
            numbers[right] = numbers[left]
            right -= 1

    numbers[left] = pivot
    pivot = left

    return pivot

numbers = [5, 3, 8, 4, 2]
print("Original array:", numbers)

quicksort(numbers, 0, len(numbers) - 1)
print("Sorted array:", numbers)
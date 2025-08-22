<<<<<<< HEAD
def insertion_sort(bucket):
    for i in range(1, len(bucket)):
        key = bucket[i]
        j = i - 1
        while j >= 0 and key < bucket[j]:
            bucket[j + 1] = bucket[j]
            j -= 1
        bucket[j + 1] = key


def bucket_sort(arr):
    if len(arr) == 0:
        return arr

    max_value = max(arr)
    size = max_value / len(arr)

    buckets = [[] for _ in range(len(arr))]

    for i in range(len(arr)):
        j = int(arr[i] / size)
        if j != len(arr):
            buckets[j].append(arr[i])
        else:
            buckets[len(arr) - 1].append(arr[i])

    for bucket in buckets:
        insertion_sort(bucket)

    result = []
    for bucket in buckets:
        result.extend(bucket)

    return result


if __name__ == "__main__":
    data = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
    print("Unsorted Array:", data)
    sorted_data = bucket_sort(data)
=======
def insertion_sort(bucket):
    for i in range(1, len(bucket)):
        key = bucket[i]
        j = i - 1
        while j >= 0 and key < bucket[j]:
            bucket[j + 1] = bucket[j]
            j -= 1
        bucket[j + 1] = key


def bucket_sort(arr):
    if len(arr) == 0:
        return arr

    max_value = max(arr)
    size = max_value / len(arr)

    buckets = [[] for _ in range(len(arr))]

    for i in range(len(arr)):
        j = int(arr[i] / size)
        if j != len(arr):
            buckets[j].append(arr[i])
        else:
            buckets[len(arr) - 1].append(arr[i])

    for bucket in buckets:
        insertion_sort(bucket)

    result = []
    for bucket in buckets:
        result.extend(bucket)

    return result


if __name__ == "__main__":
    data = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
    print("Unsorted Array:", data)
    sorted_data = bucket_sort(data)
>>>>>>> 45b5ba4 (First Commit)
    print("Sorted Array:", sorted_data)
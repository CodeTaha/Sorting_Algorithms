def _merge(left, right):
    result = []
    x = y = 0

    while x < len(left) and y < len(right):
        if left[x] < right[y]:
            result.append(left[x])
            x += 1
        else:
            result.append(right[y])
            y += 1

    result.extend(left[x:])
    result.extend(right[y:])

    return result


class MergeSort:
    def __init__(self, list_to_sort):
        self.list = list_to_sort

    def get_list(self):
        return self.list

    def sort(self):
        self.list = self._sort(self.list)

    def _sort(self, whole):
        if len(whole) == 1:
            return whole
        else:
            left = whole[:len(whole) // 2]
            right = whole[len(whole) // 2:]

            left = self._sort(left)
            right = self._sort(right)

            return _merge(left, right)

if __name__ == "__main__":
    array_to_sort = [15, 19, 4, 3, 18, 6, 2, 12, 7, 9, 11, 16]
    print("Unsorted:")
    for num in array_to_sort:
        print(num, end=" ")
    print()

    sort_obj = MergeSort(array_to_sort)
    sort_obj.sort()

    print("Sorted:")
    sorted_array = sort_obj.get_list()
    for num in sorted_array:
        print(num, end=" ")
    print()
<<<<<<< HEAD
def shellsort():
    array = [9, 5, 8, 3, 1]
    n = len(array)
    h = 1

    while (h * 3 + 1) < n:
        h = 3 * h + 1

    while h > 0:
        for i in range(h, n):
            temp = array[i]
            j = i

            while j >= h and array[j - h] > temp:
                array[j] = array[j - h]
                j -= h

            array[j] = temp

        h //= 3

    for element in array:
        print(element)

if __name__ == "__main__":
    shellsort()
=======
def shellsort():
    array = [9, 5, 8, 3, 1]
    n = len(array)
    h = 1

    while (h * 3 + 1) < n:
        h = 3 * h + 1

    while h > 0:
        for i in range(h, n):
            temp = array[i]
            j = i

            while j >= h and array[j - h] > temp:
                array[j] = array[j - h]
                j -= h

            array[j] = temp

        h //= 3

    for element in array:
        print(element)

if __name__ == "__main__":
    shellsort()
>>>>>>> 45b5ba4 (First Commit)

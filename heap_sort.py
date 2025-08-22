def downheap(array, k, N):
    T = array[k - 1]
    while k <= N // 2:
        j = k + k
        if (j < N) and (array[j - 1] < array[j]):
            j += 1
        if T >= array[j - 1]:
            break
        else:
            array[k - 1] = array[j - 1]
            k = j
    array[k - 1] = T

def heapsort():
    array = [9, 5, 8, 3, 1]
    N = len(array)

    for k in range(N // 2, 0, -1):
        downheap(array, k, N)

    while N > 1:
        array[0], array[N - 1] = array[N - 1], array[0]
        N -= 1
        downheap(array, 1, N)

    for element in array:
        print(element)

if __name__ == "__main__":
    heapsort()
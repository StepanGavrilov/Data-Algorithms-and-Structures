def get_minrun(data_size: int) -> int:
    min_merge = 32
    base = 0
    while data_size >= min_merge:
        base |= data_size & 1
        data_size >>= 1
    return data_size + base


def insertion_sort(data, left, right):
    """Сортирует от левого индекса до правого"""
    for i in range(left+1, right+1):
        j = i
        while j > left and data[j] < data[j-1]:
            data[j], data[j-1] = data[j-1], data[j]
            j -= 1


def merge(arr, l, m, r):
    len1, len2 = m - l + 1, r - m
    left = []
    right = []
    for i in range(0, len1):
        left.append(arr[l+1])
    for i in range(0, len2):
        right.append(arr[m + 1 + i])

    i, j, k = 0, 0, l

    while i < len1 and j < len2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len1:
        arr[k] = left[i]
        k += 1
        i += 1

    while j < len2:
        arr[k] = right[j]
        k += 1
        j += 1


def tim_sort(arr):
    n = len(arr)
    min_run = get_minrun(n)

    for start in range(0, n, min_run):
        end = min(start + min_run - 1, n - 1)
        insertion_sort(arr, start, end)

    size = min_run
    while size < n:  # Если меньше минимального merge проходим

        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))

            merge(arr, left, mid, right)

        size = 2 * size


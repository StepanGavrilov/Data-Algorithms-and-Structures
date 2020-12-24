

def get_minrun(data_size: int) -> int:
    """Минимальный размер упорядоченной последовательности"""
    min_merge = 32
    base = 0
    while data_size >= min_merge:
        base |= data_size & 1
        data_size >>= 1
    return data_size + base


def insertion_sort(data, left, right):
    """Сортирует от левого индекса до правого"""
    for i in range(left + 1, right + 1):
        j = i
        while j > left and data[j] < data[j - 1]:
            data[j], data[j - 1] = data[j - 1], data[j]
            j -= 1


def merge(arr, l, m, r):
    """
    :param arr: массив
    :param l: начало первого массива
    :param m: конец первого массива
    :param r: второй массив
    :return:
    """
    len1, len2 = m - l + 1, r - m
    left = []
    right = []
    for i in range(0, len1):
        left.append(arr[l + 1])
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
    # слияние
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
        end = min(start + min_run - 1, n - 1)  # 0, 4
        insertion_sort(arr, start, end)
    size = min_run  # Если меньше минимального merge проходим
    while size < n:  # min run > size array
        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))
            merge(arr, left, mid, right)
        size = 2 * size


if __name__ == '__main__':
    l = [213, 1, 54, 24, 0, -23423, 13123, 12312, 0, 0, 12312, 12312,3, 543, 234, 25423, 23423, 23423, 234234, 65756754, 234, 234]
    tim_sort(l)
    print(l)

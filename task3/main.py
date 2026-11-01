import timeit
import random

def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array

def main():
    sizes = [100, 1000, 10000]

    for size in sizes:
        data = [random.randint(0, 100000) for _ in range(size)]
        print(f"--- Розмір масиву: {size} ---")

        # Insertion Sort (пропускаємо для великих даних через O(n^2))
        if size <= 1000:
            time_insertion = timeit.timeit(lambda: insertion_sort(data.copy()), number=10)
            print(f"Insertion Sort: {time_insertion:.5f} с")
        else:
            print("Insertion Sort: Пропущено (занадто повільно)")

        # Merge Sort
        time_merge = timeit.timeit(lambda: merge_sort(data.copy()), number=10)
        print(f"Merge Sort:     {time_merge:.5f} с")

        # Timsort (вбудований sorted)
        time_timsort = timeit.timeit(lambda: sorted(data.copy()), number=10)
        print(f"Timsort:        {time_timsort:.5f} с")

if __name__ == "__main__":
    main()

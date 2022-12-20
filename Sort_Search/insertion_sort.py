def insertion_sort(arr):
    for i in range(len(arr)):
        key = arr[i]

        j = i - 1
        while j >= 0 and key > arr[j]:
            arr[j + 1] = arr[j]     # swap
            j -= 1
        arr[j + 1] = key
    return arr


print(insertion_sort([1,5,2,3,4]))        # [5, 4, 3, 2, 1]

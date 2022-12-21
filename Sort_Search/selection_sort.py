def selection_sort(arr):
    for i in range(len(arr)):
        # Initialize minimum value(min_idx) to location 0.
        min = i

        # Traverse the array to find the minimum element in the array.
        for j in range(i+1, len(arr)):
            # While traversing if any element smaller than min_idx is found then swap both the values.
            if arr[min] > arr[j]:
                # Then, increment min_idx to point to the next element.
                min = j

        # swap
        arr[i], arr[min] = arr[min], arr[i]
    return arr

print(selection_sort([1,5,2,3,4]))

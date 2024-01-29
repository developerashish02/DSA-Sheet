def cyclic_sort(arr):

    i = 0

    while i < len(arr):
        correctPos = arr[i] - 1
        if arr[i] != arr[correctPos]:
            arr[i], arr[correctPos] = arr[correctPos], arr[i]

        else:
            i += 1

    return arr


arr = [5, 4, 3, 2, 1]
result = cyclic_sort(arr)

print(result)

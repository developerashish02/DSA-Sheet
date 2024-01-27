def rotateArray(arr: [], n: int) -> []:

    if n == 0:
        return arr

    rightShift = arr[0]
    for index in range(0, n):
        # handle for the last element
        if index == n - 1:
            break
        arr[index] = arr[index + 1]

    arr[n-1] = rightShift

    return arr


n = 5
arr = [4, 0, 3, 2, 5]

result = rotateArray(arr, n)
print(result)

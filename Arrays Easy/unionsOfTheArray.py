def sortedArray(arr1: [int], arr2: [int]) -> [int]:
    my_set = set()
    unions = []

    for element in arr1:
        my_set.add(element)

    for element in arr2:
        my_set.add(element)

    for element in my_set:
        unions.append(element)

    return unions


def sortedArrayBetter(arr1: [int], arr2: [int]) -> [int]:
    i = 0
    j = 0
    unions = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            if len(unions) == 0 or unions[-1] != arr1[i]:
                unions.append(arr1[i])
            i += 1
        else:
            if len(unions) == 0 or unions[-1] != arr2[j]:
                unions.append(arr2[j])
            j += 1

    while i < len(arr1):
        if arr1[i] != unions[-1]:
            unions.append(arr1[i])
        i += 1

    while j < len(arr2):
        if arr2[j] != unions[-1]:
            unions.append(arr2[j])
        j += 1

    return unions


arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr2 = [2, 3, 4, 4, 5, 11, 12]
res = sortedArray(arr1, arr2)
print(res)

def isSorted(a: [int]) -> int:

    for index in range(len(a)):
        if index + 1 == len(a):
            return 1

        if a[index] > a[index+1]:
            return 0

    return 1


a = [1, 2, 3, 4, 5]

ans = isSorted(a)
print(ans)

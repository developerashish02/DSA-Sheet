def getSecondOrderElements(arr: [int]) -> [int]:
    # Write your code here.

    firstMaxi = arr[0]
    secondMaxi = -1

    for ele in arr:
        if ele > firstMaxi:
            firstMaxi = ele

    for ele in arr:
        if ele > secondMaxi and ele < firstMaxi:
            secondMaxi = ele

    return secondMaxi


# optimal approach
def secondMaxiOptimal(arr: [int]) -> int:
    firstMax = arr[0]
    secondMax = -1

    for ele in arr:
        if ele > firstMax:
            secondMax = firstMax
            firstMax = ele

        if ele > secondMax and ele < firstMax:
            secondMax = ele

    return secondMax


arr = [4, 2, 7, 2, 9, 4, 6]
secondMaxi = getSecondOrderElements(arr)
print("The Second Maximum element is the array: ", secondMaxi)

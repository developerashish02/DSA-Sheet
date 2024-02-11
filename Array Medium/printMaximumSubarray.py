def maxSubArray(nums) -> int:
    sum = 0
    maxi = float('-inf')
    ansStart = -1
    ansEnd = -1

    for i in range(len(nums)):
        if sum == 0:
            ansStart = i
        sum += nums[i]

        if sum > maxi:
            maxi = sum
            ansEnd = i

        if sum < 0:
            sum = 0

    print("Maximum sum subarray:")
    for i in range(ansStart, ansEnd + 1):
        print(nums[i], end=" ")
    print()

    return maxi


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = maxSubArray(nums)
print("Maximum sum:", result)

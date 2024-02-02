def longestSubarrayWithSumK(nums: [int], target: int) -> int:

    maxLength = 0

    for i in range(len(nums)):
        sum = 0
        for j in range(i, len(nums)):
            sum += nums[j]

            if sum == target:
                maxLength = max(maxLength, j - i + 1)

    return maxLength

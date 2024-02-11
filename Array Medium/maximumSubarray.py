# Function definition
def maxSubArray(nums) -> int:
    # Initialize variables
    sum = 0  # Current sum of subarray
    maxi = float('-inf')  # Maximum sum found so far

    # Iterate through the array
    for num in nums:
        sum += num  # Add the current number to the sum

        # Update maxi if the current sum is greater
        if sum > maxi:
            maxi = sum

        # If sum becomes negative, reset it to 0
        if sum < 0:
            sum = 0

    return maxi  # Return the maximum sum found


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = maxSubArray(nums)

print(result)

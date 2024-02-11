

def rearrangeArray(nums):
    # Initialize a result list with None values of the same length as nums
    result = [None] * len(nums)
    positive = 0  # Initialize the index for positive numbers
    negative = 1  # Initialize the index for negative numbers

    # Iterate through each number in the input list nums
    for num in nums:
        if num > 0:
            # If the number is positive, assign it to the next available position
            result[positive] = num
            positive += 2  # Move to the next available position for positive numbers
        else:
            # If the number is negative, assign it to the next available position
            result[negative] = num
            negative += 2  # Move to the next available position for negative numbers

    return result


nums = [-1, 2, -3, 4, -5, 6]
rearranged_nums = rearrangeArray(nums)
print(rearranged_nums)

# Time Complexity: O(n)
# The time complexity is linear because we iterate through the input list nums once,
# and each iteration performs constant-time operations (comparison and assignment).

# Space Complexity: O(n)
# The space complexity is also linear because we create an additional list, result,
# which has the same length as the input list nums. Thus, the space used is proportional
# to the size of the input list.

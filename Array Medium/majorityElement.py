
def majorityElementOptimal(nums) -> int:
    # Initialize variables to track the majority element and its count
    ele = None
    count = 0

    # Iterate through the list of numbers
    for num in nums:
        # If count is 0, no majority element found so far
        # Set the current element as potential majority element and start count from 1
        if count == 0:
            ele = num
            count += 1
        # If current number is equal to potential majority element, increment count
        elif num == ele:
            count += 1
        # If current number is not equal to potential majority element, decrement count
        else:
            count -= 1

    # Return the potential majority element as the result
    return ele


def majorityElement(nums) -> int:

    hashMap = {}

    for num in nums:
        hashMap[num] = hashMap.get(num, 0) + 1

    for key, value in hashMap.items():
        if value > len(nums) // 2:
            return key
    return 0


nums = [2, 2, 1, 1, 1, 2, 2]

res = majorityElementOptimal(nums)

print(res)

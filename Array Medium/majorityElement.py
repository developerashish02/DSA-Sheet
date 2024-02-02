def majorityElement(nums) -> int:

    hashMap = {}

    for num in nums:
        hashMap[num] = hashMap.get(num, 0) + 1

    for key, value in hashMap.items():
        if value > len(nums) // 2:
            return key
    return 0


nums = [2, 2, 1, 1, 1, 2, 2]

res = majorityElement(nums)

print(res)

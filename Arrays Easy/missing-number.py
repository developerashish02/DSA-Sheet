class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        i = 0

        while i < len(nums):
            correctPos = nums[i]

            if nums[i] >= len(nums):
                i += 1
                continue

            if nums[i] != nums[correctPos]:
                nums[i], nums[correctPos] = nums[correctPos], nums[i]

            else:
                i += 1

        for i in range(len(nums)):
            if nums[i] != i:
                return i

        return len(nums)

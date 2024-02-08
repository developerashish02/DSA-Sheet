from typing import List


class Solution:
    # Brute Force Solution
    # Time Complexity: O(n^2) - nested loops iterate over all pairs of numbers
    # Space Complexity: O(1) - no extra space used
    def twoSum_brute_force(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return [-1, -1]

    # Better Solution
    # Time Complexity: O(n) - single pass through the list
    # Space Complexity: O(n) - extra space used for the dictionary
    def twoSum_better(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        for i, num in enumerate(nums):
            difference = target - num
            if difference in my_dict:
                return [my_dict[difference], i]
            my_dict[num] = i
        return [-1, -1]


sol = Solution()

# Test the brute force solution
print(sol.twoSum_brute_force([2, 7, 11, 15], 9))  # Output: [0, 1]

# Test the better solution
print(sol.twoSum_better([2, 7, 11, 15], 9))  # Output: [0, 1]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        my_dict = {}
        result = []

        for i in range(len(nums)):
            element = target - nums[i]

            if element in my_dict:
                value = my_dict.get(element)
                result.append(value)
                result.append(i)
                return result

            else:
                my_dict[nums[i]] = i

        return [-1, -1]

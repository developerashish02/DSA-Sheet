

from ast import List


def reverse(nums, start, end):

    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1

    return nums


def rotate(self, nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """

    if len(nums) == 0 or len(nums) == 1:
        return nums

    if k > len(nums):
        k = k % len(nums)

    reverse(nums, 0, len(nums))
    reverse(nums, 0, k - 1)
    reverse(nums, k, len(nums))

    return nums

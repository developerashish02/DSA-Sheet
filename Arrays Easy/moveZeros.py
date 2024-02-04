from typing import List


def moveZeroesBetter(self, nums: List[int]) -> None:
    """
    Moves all zero elements in the input array to the end while maintaining
    the order of non-zero elements. Returns the modified array.

    Time Complexity: O(n) - Iterates through the array twice.
    Space Complexity: O(n) - Uses additional space for the 'result' list.
    """
    result = []

    # First loop: Append non-zero elements to the 'result' list.
    for element in nums:
        if element != 0:
            result.append(element)

    # Second loop: Append zero elements to the 'result' list.
    for element in nums:
        if element == 0:
            result.append(element)

    # Third loop: Update the input array with elements from 'result'.
    for index in range(len(result)):
        nums[index] = result[index]

    return nums


def moveZeroesOptimal(nums: List[int]) -> None:
    """
    Moves all zero elements in the input array to the end while maintaining
    the order of non-zero elements. Modifies the input array in-place.

    Time Complexity: O(n) - Finds the index of the first zero and iterates through the array once.
    Space Complexity: O(1) - Uses constant space, modifies the input array in-place.
    """
    i = -1

    # Find the index of the first zero element.
    for j in range(len(nums)):
        if nums[j] == 0:
            i = j
            break

    if i == -1:
        return nums

    # Iterate through the array, swapping non-zero elements with the first zero element.
    for j in range(i, len(nums)):
        if nums[j] == 0:
            j += 1
        else:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1

    return nums

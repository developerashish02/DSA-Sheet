def removeDuplicatesBrute(arr) -> int:
    st = set()
    for i in range(len(arr)):
        st.add(arr[i])
    k = len(st)
    j = 0
    for x in st:
        arr[j] = x
        j += 1
    return k


def removeDuplicates(nums) -> int:

    i = 0

    for j in range(len(nums)):
        if nums[i] != nums[j]:
            nums[i + 1] = nums[j]
            i += 1

    return i + 1


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

res = removeDuplicates(nums)

print("Remove Duplicates: ", nums)

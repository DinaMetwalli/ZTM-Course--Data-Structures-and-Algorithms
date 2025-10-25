def sum_of_list(nums) -> int:
    if not nums:
        return 0
    return nums[0] + sum_of_list(nums[1:])

print(sum_of_list([1,4,6]))

def product_of_list(nums) -> int:
    if not nums:
        return 1
    return nums[0] * product_of_list(nums[1:])

# [2,3,4]
#  2 1 0 -> 4, 12, 24

print(product_of_list([2,3,4]))

def sum_nested_list(nums) -> int:
    if not nums:
        return 0
    if type(nums[0]) == list:
        nums[0] = nums[0][0] + sum_nested_list(nums[0][1:])
    return nums[0] + sum_nested_list(nums[1:])

# [1, [2, 3], 4] -> 10
#  3   2  1   0  -> 4 + (3, 5) -> 9 + 1 -> 10

print(sum_nested_list([1,[2,3,[5,[5]]],4]))
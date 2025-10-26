# Merge Sort Algorithm Implementation

count = 0

def merge_sort(nums): # recusrively split list (divide and conquer)
    if len(nums) == 1: # base case for returning when split list contains only 1 element
        return nums
    else:
        mid = len(nums)//2
        left_nums = nums[:mid]
        right_nums = nums[mid:]
        print(f'Left : {left_nums}')
        print(f'Right : {right_nums}')
        return merge(merge_sort(left_nums),merge_sort(right_nums)) # merge the lists into a sorted list


def merge(left, right): # merge and compare smaller lists
    l = len(left)
    r = len(right)
    left_index = 0
    right_index = 0
    sorted_nums = []
    while (left_index < l and right_index < r):
        global count
        count += 1
        if left[left_index] < right[right_index]: # compare elements of each list
            sorted_nums.append(left[left_index])
            left_index += 1
        else:
            sorted_nums.append(right[right_index])
            right_index += 1
    print(sorted_nums + left[left_index:] + right[right_index:])
    return sorted_nums + left[left_index:] + right[right_index:]



nums = [5,9,3,10,45,2,0]
merge_sort(nums)
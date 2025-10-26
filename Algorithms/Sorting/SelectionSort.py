# Selection Sort Algorithm Implementation

def selection_sort(nums): # O(n^2)
    for i in range(len(nums)):
        smallest_item = nums[i]
        for j in range(i, len(nums)):
            if nums[j] <= smallest_item:
                smallest_item = nums[j]
                id = j
        nums[id] = nums[i]
        nums[i] = smallest_item

numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

selection_sort(numbers)
print(numbers)
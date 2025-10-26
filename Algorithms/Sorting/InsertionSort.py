# Insertion Sort Algorithm Implementation

def insertion_sort(nums) -> int: # O(n^2) - O(n) depending on array
    for i in range(1,len(nums)):
        print(nums)
        insert_index = i
        current_value = nums[i]
        for j in range(i-1, -1, -1): # loop backwards through sorted part of list to determine where to insert
            if nums[j] > current_value:
                nums[j+1] = nums[j]
                insert_index = j
            else:
                break
        nums[insert_index] = current_value
            

numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
insertion_sort(numbers)
print(numbers)
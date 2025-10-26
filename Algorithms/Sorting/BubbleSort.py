# Bubble Sort Algorithm Implementation

import time

def bubble_sort(nums): # O(n^2)
    itr = len(nums) - 1
    for _ in range(len(nums)):
        for i in range(itr):
            if i == len(nums):
                break
            if nums[i] > nums[i+1]:
                temp = nums[i]
                nums[i] = nums[i+1]
                nums[i+1] = temp
        itr-=1 # -> comment out this line to see time difference

numbers = []
for i in range(2000):
    numbers.append(2000-i)

start = time.time()
bubble_sort(numbers)
end = time.time()

print(numbers, end-start)
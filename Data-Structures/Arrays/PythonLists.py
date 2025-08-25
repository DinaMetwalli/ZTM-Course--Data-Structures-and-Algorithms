# Time Complexities:
# access        -> O(1)
# push/pop      -> O(1)*
# search/lookup -> O(n)
# insert/delete -> O(n)

array = [1,2,3,4,5,6,7,8,9,10]

# access
first_element = array[0] # O(1)
seventh_element = array[6] # O(1)

# push/pop
array.append(11) # O(1)
array.pop() # O(1)

# * in some special cases, the append(push) operation may take greater time. This is because Python has dynamic arrays
# so when an element is to be appended and the array is full, the entire array has to be copied to a new location
# with more space allocated this time so that more items can be appended. Therefore, some individual operations
# may reuire O(n) time or greater, but when averaged over a large number of operations, The complexity can be
# safely considered to be O(1) - amortized worst case time complexity.

print(array)

# insert/delete
array.insert(6, 0) # O(n)
array.pop(3) # removes the 3rd element in the array. O(n)

print(array)

array.remove(9) # removes the first occurence of the element 9, not the 9th element. this requires traversing the array meaning O(n)
del array[3:5] # removes the elements in the array from positions 3 to 5. also requires traversal so O(n)

print(array)
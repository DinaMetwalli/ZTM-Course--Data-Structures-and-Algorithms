from copy import copy

# Python lists are mutable 
list1 = [1,2,3]
list2 = copy(list1)
list2[2] = 4

print(list1)
print(list2)

# Tuples are immutable but faster
tuple1 = (1,2,[])
tuple2 = copy(tuple1)
tuple2[2].append("123")

print(tuple1)
print(tuple2)
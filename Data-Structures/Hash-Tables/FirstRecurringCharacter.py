# Google Interview Question
# Given an array, return the first recurring character
# Example1 : array = [2,1,4,2,6,5,1,4]
# return 2
# Example 2 : array = [2,6,4,6,1,3,8,1,2]
# return 6
# Example 3 : array = [1,2,3,4]
# return None

def naive_recurring_char(array) -> int | None: # O(n^2)
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] == array[j]:
                return array[i]
        
    return None

def find_recurring_char(array) -> int | None: # O(n) - improved time complexity, but increased space complexity due to new dictionary
    try:
        map = dict()

        for item in array: # O(n)
            if item in map: # O(1) lookup
                return item
            map[item] = True

        return None
    
    except TypeError:
        return "Input must be an array."

# testing naive method:
print(naive_recurring_char([7,1,4,2,6,5,1,4]))
print(naive_recurring_char([1,2,3,4]))
print(naive_recurring_char([2,1,4,2,6,5,1,4]))
# testing improved method:
print(find_recurring_char([2,1,4,2,6,5,1,4]))
print(find_recurring_char([2,6,4,6,1,3,8,1,2]))
print(find_recurring_char([1,2,3,4]))
print(find_recurring_char(0))

print(naive_recurring_char([2,5,5,2,6,5,1,4])) # -> returns correct output
print(find_recurring_char([2,5,5,2,6,5,1,4])) # -> returns incorrect output
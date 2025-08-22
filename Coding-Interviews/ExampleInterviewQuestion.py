# We are given two arrays. We have to find if these two arrays contain any matching elements.
# For example, array1 = ['a','b','c','x'] , array2 = ['x','y','z']
# This should return True as element 'x' appears in both arrays.

array1 = ['a','b','c','x']
array2 = ['x','y','z']

# first solution that comes to mind - O(m x n) quadratic time complexity:

def brute_force_matching_element(arr1, arr2) -> str:
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i] == arr2[j]:
                return f"The matching element is: {arr1[i]}"
    return "no matching elements found."

# print(brute_force_matching_element(array1, array2))

# -------------------------------------------------------------------------------
# improved solution - O(n + m) linear time complexity:

# first, we convert the first array into a hash table (python dict) for easier lookup.
# this allows looking through the second array only to check if any of its items exist in the hash table.
# this method will lead to a linear time solution of O(n + m) by removing the nested for loops.

def improved_matching_element(arr1, arr2) -> bool:
    try:
        dictionary = dict()
        for i in range(len(arr1)):
            dictionary[arr1[i]] = True
        print(dictionary)

        for i in range(len(arr2)):
            if dictionary[arr2[i]]:
                return True
        return False
    
    except TypeError:
        return "An input of two arrays is required."

improved_matching_element(array1, array2)
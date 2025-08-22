# Example Google interview question.
# You are given an array of integers and a particular sum.
# You have to check if there are any two elements in the array that add up to the given sum.
# For example, array = [1,2,4,4] ,sum = 8 will return True as 4+4 = 8.

array = [1,2,4,6]
sum = 8

# First brute force solution that comes to mind - O(n^2) quadratic time complexity:

def brute_force_pair_sum(array, sum) -> bool:
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] + array[j] == sum:
                return True
    return False

# brute_force_pair_sum(array, sum)

# -------------------------------------------------------------------------------

# improving the solution - O(n) linear time complexity:

# keeping a set of complements for each of the array's items and returning true if that complement is found in the array.

def improved_pair_sum(array, sum) -> bool:
        comps = set()
        for item in array:
            if item in comps:
                return True
            comps.add(sum - item)
        print(comps)
        return False

improved_pair_sum(array, sum)
# Quadratic Time Complexity Exercises

# log all pairs of array:
array = ['a','b','c','d','e']

def log_all_pairs(array) -> None:
    for i in range(len(array)):
        for j in range(len(array)):
            print(array[i],array[j])

log_all_pairs(array)

# O(n*n) = O(n^2) -> quadratic time.

#---------------------------------------

# log all numbers of array and their sum:
def log_all_numbers_and_sum(numbers) -> None:
    for number in numbers:
        print(number)

    for firstNum in numbers:
        for secondNum in numbers:
            print(firstNum + secondNum)

log_all_numbers_and_sum([1,2,3,4,5])

# O(n + n^2) = O(n^2) -> non-dominants are dropped (n) and the complexity 
# most affected by the input is considered instead: quadratic time.
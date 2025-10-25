# Given a number N, return the index value of the fibonacci sequence for that index.
# series: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...
# index : 0  1  2  3  4  5  6  7   8   9   10  11  12   ...
# example: N = 7 returns 13

def fibonacci_iterative(n) -> int: # O(n) Linear time
    fibonacci = [0, 1]
    for i in range(n):
        fibonacci.append(fibonacci[i] + fibonacci[i+1])
    return fibonacci[n]

def fibonacci_recursive(n) -> int: # O(2^n) Exponential time
    if n < 2:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

print(fibonacci_iterative(40))
print(fibonacci_recursive(40)) # takes significantly longer
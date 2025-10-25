# Write two functions that find the factorial of any number.
# One should use a recursive approach, the other should use a for loop.

def find_factorial_recursive(num) -> int: # O(n)
    if num == 2:
        return num
    return num * find_factorial_recursive(num - 1)

    # 5 * (4 * (3 * (2 * (1))))

# 3 * 2
# 4 * 6
# 5 * 24
# 120

def find_factorial_iterative(num) -> int: # O(n)
    result = num
    for i in range(1, num):
        result *= num - i
    return result

print(find_factorial_iterative(5))
print(find_factorial_recursive(5))
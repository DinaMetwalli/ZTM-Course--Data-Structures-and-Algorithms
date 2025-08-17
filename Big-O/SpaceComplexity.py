# Space Complexity Exercises & Examples

def boooo(n) -> None:
    for _ in n:
        print('booo!')

boooo([1,2,3,4,5])

# space complexity of O(1)

# -------------------------------------------

def assign_string_to_list(n) -> list:
    array = []
    for _ in range(n):
        array.append('hi')

    return array

print(assign_string_to_list(6))

# space complexity of O(n) -> the number of assignments grows linearly with the size of the input.
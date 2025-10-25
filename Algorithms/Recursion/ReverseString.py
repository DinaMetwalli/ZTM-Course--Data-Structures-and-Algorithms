def reverse_string_iterative(s):
    reversed_string = ""
    for i in range(1, len(s)+1):
        reversed_string+= s[-i]
    return reversed_string

def reverse_string_recursive(s):
    if s == "":
        return ""
    return reverse_string_recursive(s[1:]) + s[0] 

print(reverse_string_iterative("hello"))
print(reverse_string_recursive("hello"))
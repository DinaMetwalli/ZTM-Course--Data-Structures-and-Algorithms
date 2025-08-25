# Create a function that reverses a string:
# 'Hi, my name is Andrei' should be:
# 'ierdnA si eman ym ,iH'

# brute force/naive method:
def reverse(string) -> str:
    try:
        if len(string) < 2:
            return "hmm... that's not good."
        
        reversed_str = []
        for i in range(len(string)-1, -1, -1): # O(n)
            reversed_str.append(string[i])
        return ''.join(reversed_str)
    
    except TypeError:
        return "Input must be a string."

def simpler_reverse(string) -> str:
    return string[::-1] # O(n) using inbuilt python slice function.


print(reverse('Hi, my name is Andrei'))
print(simpler_reverse('Hi, my name is Andrei'))
# Implementation of Stack Data Structure

class Stack:
    def __init__(self):
        self.stack = []

    def peek(self): # O(1)
        if len(self.stack) == 0:
            return None
        return self.stack[-1]
    
    def push(self, value): # O(1)
        self.stack.append(value)
        
    
    def pop(self): # O(1)
        if len(self.stack) == 0:
            return None
        self.stack.pop()
    
    def print_list(self):
        print(f"Stack: {self.stack} Length: {len(self.stack)}")
    
my_stack = Stack()

my_stack.push("google.com")
my_stack.print_list()
my_stack.push("udemy.com")
my_stack.print_list()
my_stack.push("stackoverflow.com")
my_stack.print_list()

my_stack.pop()
my_stack.print_list()
my_stack.pop()
my_stack.print_list()
my_stack.pop()
my_stack.print_list()


print(my_stack.peek())
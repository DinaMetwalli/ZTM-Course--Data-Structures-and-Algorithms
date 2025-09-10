# Implementation of Stack Data Structure using Linked List

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self): # O(1)
        if self.length == 0:
            return None
        return self.top.value
    
    def push(self, value): # O(1)
        new_node = Node(value)
        if self.length == 0: # add first node if the stack is empty
            self.top = new_node
            self.bottom = new_node
        else: # add a new node as the top node if it isn't empty
            holding_pointer = self.top
            self.top = new_node
            self.top.next = holding_pointer # new node points to previous top
        self.length += 1
    
    def pop(self): # O(1)
        if not self.top:
            return None
        if self.top == self.bottom: # only one item remaining.
            self.bottom = None
        holding_pointer = self.top
        # garbage collection would remove self.top automatically
        # if nothing points to it, so we keep it as a holding pointer.
        self.top = self.top.next
        self.length -= 1
        return holding_pointer
    
    def print_list(self):
        array = []
        current_node = self.top # print stack from top to bottom
        while current_node != None:
            array.append(current_node.value)
            current_node = current_node.next
        print("Stack: ", array, " Length: ", self.length)
    
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
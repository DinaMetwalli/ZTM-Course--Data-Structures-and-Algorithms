# Implementation of Queue Data Structure using Linked List

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def peek(self): # O(1)
        if self.length == 0:
            return None
        return self.first.value

    def enqueue(self, value): # O(1)
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
            
    
    def dequeue(self): # O(1)
        if not self.first: # if queue is empty.
            return None
        if self.first == self.last: # if just one item in queue.
            self.last = None
        holding_pointer = self.first
        self.first = self.first.next
        self.length -= 1
        return holding_pointer
    
    def print_list(self):
        array = []
        current_node = self.first # print queue from first to last item.
        while current_node != None:
            array.append(current_node.value)
            current_node = current_node.next
        print("Queue: ", array, " Length: ", self.length)
    
my_queue = Queue()

my_queue.enqueue('Joy')
my_queue.print_list()
my_queue.enqueue('Matt')
my_queue.print_list()
my_queue.enqueue('Pavel')
my_queue.print_list()
my_queue.enqueue('Samir')
my_queue.print_list()

print(my_queue.peek())

my_queue.dequeue()
my_queue.print_list()
my_queue.dequeue()
my_queue.print_list()
my_queue.dequeue()
my_queue.print_list()
my_queue.dequeue()
my_queue.print_list()
print(my_queue.peek())
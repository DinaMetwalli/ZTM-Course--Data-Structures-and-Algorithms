# Implementation of Doubly Linked List Data Structure

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self, value):

        self.head = Node(value)
        self.tail = self.head
        self.length = 1

    def append(self, value): # O(1)
        new_node = Node(value)
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1

    def prepend(self, value): # O(1)
        new_head = Node(value)
        new_head.next = self.head
        self.head.prev = new_head
        self.head = new_head
        self.length += 1

    def print_list(self):
        array = []
        current_node = self.head
        while current_node != None:
            array.append(current_node.value)
            current_node = current_node.next
        print("Linked List: ", array, " Length: ", self.length)
    
    def traverse_list(self, index) -> Node: # O(n)
        position = 0
        current_node = self.head
        while current_node != None:
            if position == index:
                return current_node
            position += 1
            current_node = current_node.next

    def insert(self, index, value): # O(n)
        if index == 0:
            self.prepend(value)
            return
        elif index >= self.length:
            if index > self.length:
                print("Position provided is unavailable. Inserting at end of list instead.")
            self.append(value)
            return

        new_node = Node(value)
        current_node = self.traverse_list(index-1)

        new_node.next = current_node.next
        new_node.prev = current_node

        current_node.next = new_node
        new_node.next.prev = new_node

        self.length += 1

    def remove(self, index): # O(n)
        if self.head == None:
            print("No nodes found to delete from the list.")
            return
        if index == 0:
            self.head = self.head.next
            if self.head == None or self.head.next == None:
                self.tail = self.head
            if self.head != None:
                self.head.prev = None
            self.length -= 1    
            return
        if index >= self.length:
            print("No node found at this position.")
            return
        current_node = self.traverse_list(index-1)
        current_node.next = current_node.next.next
        if current_node.next != None:
            current_node.next.prev = current_node
        self.length -= 1

my_linked_list = LinkedList(10)
# 10 -> None. Size = 1

my_linked_list.append(5)
my_linked_list.print_list()
# 10 -> 5 -> None. Size = 2

my_linked_list.append(16)
my_linked_list.print_list()
# 10 -> 5 -> 16 -> None. Size = 3

my_linked_list.prepend(1)
my_linked_list.print_list()
# 1 -> 10 -> 5 -> 16 -> None. Size = 4

my_linked_list.insert(2, 44)
my_linked_list.print_list()

# test inserting at the start:
my_linked_list.insert(0, 13)
my_linked_list.print_list()

# test inserting at invalid index:
my_linked_list.insert(7, 17)
my_linked_list.print_list()
print(my_linked_list.tail.value)

my_linked_list.insert(7, 88)
my_linked_list.print_list()
print(my_linked_list.tail.value)

my_linked_list.remove(1)
my_linked_list.print_list()
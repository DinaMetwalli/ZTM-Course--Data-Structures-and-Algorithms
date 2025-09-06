# Implementation of Linked List Data Structure

class LinkedList:
    def __init__(self, value):

        self.head = {
            "value": value,
            "next": None
        }
        self.tail = self.head
        self.length = 1

    def append(self, value):
        new_node = {
            "value": value,
            "next": None
        }
        self.tail["next"] = new_node
        # remember that earlier tail was set to head because it was 1 node
        # you dont want this to be head instead because it will only work when there are 2 nodes in the LL
        # but if the LL size was more than 2 it will make head point to 3rd node+.
        self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_head = {
            "value": value,
            "next": self.head
        }
        self.head = new_head
        self.length += 1


my_linked_list = LinkedList(10)
print(my_linked_list.head)
print(my_linked_list.length)
# 10 -> None. Size = 1

my_linked_list.append(5)
print(my_linked_list.tail)
print(my_linked_list.head)
print(my_linked_list.length)
# 10 -> 5 -> None. Size = 2

my_linked_list.append(16)
print(my_linked_list.tail)
print(my_linked_list.head)
print(my_linked_list.length)
# 10 -> 5 -> 16 -> None. Size = 3

my_linked_list.prepend(1)
print(my_linked_list.tail)
print(my_linked_list.head)
print(my_linked_list.length)
# 1 -> 10 -> 5 -> 16 -> None. Size = 4
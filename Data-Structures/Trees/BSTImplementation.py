# Implementation of Binary Search Tree Data Structure

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
            return self.root
        else:
            cur = self.root
            while True:
                if value < cur.value: # Left
                    if not cur.left:
                        cur.left = new_node
                        return self.root
                    cur = cur.left
                else: # Right
                    if not cur.right:
                        cur.right = new_node
                        return self.root
                    cur = cur.right
    
    def lookup(self, value): # iterate through BST using divide and conquer, not every node needs to be visited
        if self.root == None:
            return
        else:
            cur = self.root
            while cur: # if the current node becomes None then no node with that value was found in the tree
                if value < cur.value:
                    cur = cur.left
                elif value > cur.value:
                    cur = cur.right
                elif value == cur.value:
                    return cur
            return False # if no matching node is found
    
tree = BinarySearchTree()
tree.insert(50)
tree.insert(38)
tree.insert(40)
tree.lookup(40)
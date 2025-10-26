# Breadth First Search on BST Implementation

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
    
    def breadth_first_search(self):
        cur = self.root
        search_result = []
        queue = [] # keep track of the current level to access its children once its traveresed
        queue.append(cur) # the queue is the main culprit of the memory consumption in BFS
        
        while len(queue) > 0: # as long as there is something to go through in the queue
            cur = queue.pop(0) # similar to javascript's shift method. removes the first item and returns it.
            print(cur.value)
            search_result.append(cur.value)
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        return search_result
        
    def breadth_first_search_recursive(self, queue, search_result):
        if not len(queue): # if queue is empty
            return search_result # base case
        cur = queue.pop(0)
        search_result.append(cur.value)
        if cur.left:
            queue.append(cur.left)
        if cur.right:
            queue.append(cur.right)
        return self.breadth_first_search_recursive(queue, search_result)

tree = BinarySearchTree()

tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)

#        9
#    4       20
#  1   6   15  170

tree.lookup(40)
# False

print(tree.breadth_first_search())
# [9, 4, 20, 1, 6, 15, 170]

print(tree.breadth_first_search_recursive([tree.root], []))
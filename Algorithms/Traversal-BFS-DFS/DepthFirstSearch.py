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
    
    # memory consumption will be O(height of the tree) because the call stack will grow bigger with each
    # recusrive call until the leaf nodes are reached, meaning it will grow as big as the height of the tree

    def DFS_inorder(self):
        return self.traverse_inorder(self.root, [])

    def DFS_preorder(self):
        return self.traverse_preorder(self.root, [])

    def DFS_postorder(self):
        return self.traverse_postorder(self.root, [])
    

    def traverse_inorder(self, node, result):
        if node.left:
            self.traverse_inorder(node.left, result)
        result.append(node.value)
        if node.right:
            self.traverse_inorder(node.right, result)
        return result
    
    def traverse_preorder(self, node, result):
        result.append(node.value)
        if node.left:
            self.traverse_preorder(node.left, result)
        if node.right:
            self.traverse_preorder(node.right, result)
        return result
    
    def traverse_postorder(self, node, result):
        if node.left:
            self.traverse_postorder(node.left, result)
        if node.right:
            self.traverse_postorder(node.right, result)
        result.append(node.value)
        return result


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

print(tree.DFS_inorder()) # InOrder - [1, 4, 6, 9, 15, 20, 170]
print(tree.DFS_preorder()) # PreOrder - [9, 4, 1, 6, 20, 15, 170]
print(tree.DFS_postorder()) # PostOrder - [1, 6, 4, 15, 170, 20, 9]
💡 Question-1
You are given a binary tree. The binary tree is represented using the TreeNode class. Each TreeNode has an integer value and left and right children, represented using the TreeNode class itself. Convert this binary tree into a binary search tree.

# Solution - 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_traversal(node, values):
    if node is not None:
        inorder_traversal(node.left, values)
        values.append(node.val)
        inorder_traversal(node.right, values)

def construct_BST(values):
    if not values:
        return None

    mid = len(values) // 2
    root = TreeNode(values[mid])
    root.left = construct_BST(values[:mid])
    root.right = construct_BST(values[mid+1:])

    return root

def convert_to_BST(root):
    values = []
    inorder_traversal(root, values)
    return construct_BST(values)

Driver code # Construct the binary tree
root = TreeNode(10)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(8)
root.left.right = TreeNode(4)

# Convert the binary tree to a binary search tree
new_root = convert_to_BST(root)

# Function to print the BST in in-order traversal
def inorder_traversal(node):
    if node is not None:
        inorder_traversal(node.left)
        print(node.val, end=' ')
        inorder_traversal(node.right)

# Print the converted BST
inorder_traversal(new_root)


💡 Question-2:

Given a Binary Search Tree with all unique values and two keys. Find the distance between two nodes in BST. The given keys always exist in BST.

# Solution:

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def construct_BST(values):
    if not values:
        return None

    mid = len(values) // 2
    root = TreeNode(values[mid])
    root.left = construct_BST(values[:mid])
    root.right = construct_BST(values[mid+1:])

    return root

def find_distance(root, node1, node2):
    if root.val > node1 and root.val > node2:
        return find_distance(root.left, node1, node2)

    if root.val < node1 and root.val < node2:
        return find_distance(root.right, node1, node2)

    return distance_from_node(root, node1) + distance_from_node(root, node2)

def distance_from_node(root, node):
    if root.val == node:
        return 0

    if root.val > node:
        return 1 + distance_from_node(root.left, node)

    return 1 + distance_from_node(root.right, node)

# Driver code 
values = [8, 3, 1, 6, 4, 7, 10, 14, 13]
root = construct_BST(values)

# Test case 1
node1 = 6
node2 = 14
distance = find_distance(root, node1, node2)
print("The distance between the two keys:", distance)  # Output: The distance between the two keys: 4

# Test case 2
node1 = 3
node2 = 4
distance = find_distance(root, node1, node2)
print("The distance between the two keys:", distance)  # Output: The distance between the two keys: 2


💡 Question-3:

Write a program to convert a binary tree to a doubly linked list.

# Solution -

class TreeNode:
    def __init__(self, val=0, left=None, right=None, prev=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.prev = prev
        self.next = next

def convert_to_DLL(root):
    if root is None:
        return None

    global prev
    prev = None

    def convert_node(node):
        nonlocal prev

        if node is None:
            return None

        convert_node(node.left)

        if prev is not None:
            prev.next = node
            node.prev = prev

        if prev is None:
            head = node

        prev = node

        convert_node(node.right)

    convert_node(root)

    return head

# Helper function to print the doubly linked list
def print_DLL(head):
    current = head
    while current is not None:
        print(current.val, end=' ')
        current = current.next
    print()

# Driver code
# Construct the binary tree
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(20)
root.right.left = TreeNode(30)
root.right.right = TreeNode(35)

# Convert the binary tree to a doubly linked list
head = convert_to_DLL(root)

# Print the doubly linked list
print_DLL(head)


💡 Question-4:

Write a program to connect nodes at the same level.

# Solution

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

def connect_nodes(root):
    if root is None:
        return None

    queue = deque()
    queue.append(root)

    while queue:
        level_size = len(queue)
        prev = None

        for _ in range(level_size):
            current = queue.popleft()

            if prev is not None:
                prev.next = current

            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)

            prev = current

        prev.next = None

# Helper function to print the connected nodes
def print_connect_nodes(root):
    current = root
    while current:
        temp = current
        while temp:
            print(temp.val, end=' ')
            temp = temp.next
        print()
        current = current.left
#Driver Code
# Construct the binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# Connect the nodes at the same level
connecct_nodes(root)

# Print the connected nodes
print_connect_nodes(root)



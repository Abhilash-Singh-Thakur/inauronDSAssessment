💡 Question-1:

Given a Binary Tree (Bt), convert it to a Doubly Linked List(DLL). The left and right pointers in nodes are to be used as previous and next pointers respectively in converted DLL. The order of nodes in DLL must be the same as in Inorder for the given Binary Tree. The first node of Inorder traversal (leftmost node in BT) must be the head node of the DLL.

# Solution -
  
class TreeNode:
    def __init__(self, val=0, left=None, right=None, prev=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.prev = prev
        self.next = next

def convert_DLL(root):
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

# Example usage
# Construct the binary tree
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(20)
root.right.left = TreeNode(30)
root.right.right = TreeNode(35)

# Convert the binary tree to a doubly linked list
head = convert_DLL(root)

# Print the doubly linked list
print_DLL(head)



# 💡 Question-2

A Given a binary tree, the task is to flip the binary tree towards the right direction that is clockwise. See the below examples to see the transformation.

In the flip operation, the leftmost node becomes the root of the flipped tree and its parent becomes its right child and the right sibling becomes its left child and the same should be done for all left most nodes recursively.

# Solution - --------------------------

                                                                                                                                                                                             class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def flip_binary_tree(root):
    if root is None or (root.left is None and root.right is None):
        return root

    flipped_left = flip_binary_tree(root.left)
    flipped_right = flip_binary_tree(root.right)

    root.left = flipped_right
    root.right = flipped_left

    return root

# Helper function to print the flipped binary tree
def print_binary_tree(root):
    if root is None:
        return

    print(root.val, end=' ')
    print_binary_tree(root.left)
    print_binary_tree(root.right)

# Example usage
# Construct the binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Flip the binary tree
flipped_tree = flip_binary_tree(root)

# Print the flipped binary tree
print_binary_tree(flipped_tree)

# ---------------------------------------/

💡 Question-3:

Given a binary tree, print all its root-to-leaf paths without using recursion. For example, consider the following Binary Tree.

  # Solution-
  
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def print_root_to_leaf_path(root):
    if root is None:
        return

    stack = deque()
    stack.append(root)
    parents = {root: None}

    while stack:
        current = stack.pop()

        if current.left is None and current.right is None:
            print_path(root, current, parents)
        
        if current.right:
            stack.append(current.right)
            parents[current.right] = current
        
        if current.left:
            stack.append(current.left)
            parents[current.left] = current

def print_path(root, leaf, parents):
    path = []
    while leaf != root:
        path.append(str(leaf.val))
        leaf = parents[leaf]
    path.append(str(root.val))
    path.reverse()
    print('->'.join(path))

# Example usage
# Construct the binary tree
root = TreeNode(6)
root.left = TreeNode(3)
root.right = TreeNode(5)
root.left.left = TreeNode(2)
root.left.right = TreeNode(5)
root.right.right = TreeNode(4)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)

# Print all root-to-leaf paths
print_root_to_leaf_path(root)

# --------------------------------------------------
💡 Question-4:

Given Preorder, Inorder and Postorder traversals of some tree. Write a program to check if they all are of the same tree.

# Solution

def is_same_tree(preorder, inorder, postorder):
    if len(preorder) != len(inorder) or len(inorder) != len(postorder):
        return False

    if not preorder:
        return True

    def check_traversal(pre_start, pre_end, in_start, in_end, post_start, post_end):
        if pre_start > pre_end:
            return True

        root_value = preorder[pre_start]
        root_index = inorder.index(root_value)

        left_length = root_index - in_start
        right_length = in_end - root_index

        left_check = check_traversal(pre_start + 1, pre_start + left_length, in_start, root_index - 1, post_start, post_start + left_length - 1)
        right_check = check_traversal(pre_end - right_length + 1, pre_end, root_index + 1, in_end, post_end - right_length, post_end - 1)

        return left_check and right_check

    return check_traversal(0, len(preorder) - 1, 0, len(inorder) - 1, 0, len(postorder) - 1)

# Example usage
preorder1 = [1, 2, 4, 5, 3]
inorder1 = [4, 2, 5, 1, 3]
postorder1 = [4, 5, 2, 3, 1]
print("Output1:", is_same_tree(preorder1, inorder1, postorder1))  # Output1: True

preorder2 = [1, 5, 4, 2, 3]
inorder2 = [4, 2, 5, 1, 3]
postorder2 = [4, 1, 

                                                                                                                                                    
                                                                                                                                                                                             
                                                                                                                                                                                             

                                                                                                                                                                                            
                                                                                                                                                                                             


💡 Question-1:

Given preorder of a binary tree, calculate its **[depth(or height)](https://www.geeksforgeeks.org/write-a-c-program-to-find-the-maximum-depth-or-height-of-a-tree/)** [starting from depth 0]. The preorder is given as a string with two possible characters.

1. ‘l’ denotes the leaf
2. ‘n’ denotes internal node

The given tree can be seen as a full binary tree where every node has 0 or two children. The two children of a node can ‘n’ or ‘l’ or mix of both.

# Solution -

  def calculate_depth(preorder):
    depth = 0
    maxDepth = 0

    for char in preorder:
        if char == 'n':
            depth += 1
        elif char == 'l':
            maxDepth = max(depth, maxDepth)
            depth -= 1

    return maxDepth

# Driver Code
preorder1 = 'nlnll'
depth1 = calculate_depth(preorder1)
print("Output1:", depth1)  # Output1: 2

preorder2 = 'nlnnlll'
depth2 = calculate_depth(preorder2)
print("Output2:", depth2)  # Output2: 3

#--------------------------------
💡 Question-2:

Given a Binary tree, the task is to print the **left view** of the Binary Tree. The left view of a Binary Tree is a set of leftmost nodes for every level.
                                                                                                                                         
# Solution- 
  class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def print_left_view(root):
    levelNodes = {}

    def traverse_tree(node, level):
        if node is None:
            return

        if level not in levelNodes:
            levelNodes[level] = node.val

        traverse_tree(node.left, level + 1)
        traverse_tree(node.right, level + 1)

    traverse_tree(root, 0)

    for level in sorted(levelNodes.keys()):
        print(levelNodes[level], end=' ')
    print()

# Example usage
# Construct the binary tree
root1 = TreeNode(4)
root1.left = TreeNode(5)
root1.right = TreeNode(2)
root1.right.left = TreeNode(3)
root1.right.right = TreeNode(1)
root1.right.left.left = TreeNode(6)
root1.right.left.right = TreeNode(7)

# Print the left view of the binary tree
print("Left view 1:")
print_left_view(root1)  # Output: 4 5 3 6

# Construct another binary tree
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
root2.left.right = TreeNode(4)
root2.left.right.right = TreeNode(5)
root2.left.right.right.right = TreeNode(6)

# Print the left view of the binary tree
print("Left view 2:")
print_left_view(root2)  # Output: 1 2 4 5 6

#--------------------------------
💡 Question-3:

Given a Binary Tree, print the Right view of it.

The right view of a Binary Tree is a set of nodes visible when the tree is visited from the Right side.

# Solution -

  class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def print_right_view(root):
    levelNodes = {}

    def traverse_tree(node, level):
        if node is None:
            return

        levelNodes[level] = node.val

        traverse_tree(node.right, level + 1)
        traverse_tree(node.left, level + 1)

    traverse_tree(root, 0)

    for level in sorted(levelNodes.keys()):
        print(levelNodes[level], end=' ')
    print()

# Example usage
# Construct the binary tree
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.left = TreeNode(4)
root1.left.right = TreeNode(5)
root1.right.left = TreeNode(6)
root1.right.right = TreeNode(7)
root1.right.right.right = TreeNode(8)

# Print the right view of the binary tree
print("Right view 1:")
print_right_view(root1)  # Output: 1 3 7 8

# Construct another binary tree
root2 = TreeNode(1)
root2.left = TreeNode(8)
root2.left.left = TreeNode(7)

# Print the right view of the binary tree
print("Right view 2:")
print_right_view(root2)  # Output: 1 8 7



💡 Question-4:

Given a Binary Tree, The task is to print the **bottom view** from left to right. A node **x** is there in output if x is the bottommost node at its horizontal distance. The horizontal distance of the left child of a node x is equal to a horizontal distance of x minus 1, and that of a right child is the horizontal distance of x plus 1.

# Solution - 


from collections import deque

class TreeNode:
    def __init__(self, val=0, hd=0, left=None, right=None):
        self.val = val
        self.hd = hd
        self.left = left
        self.right = right

def print_bottom_view(root):
    if root is None:
        return

    bottomView = {}

    queue = deque()
    queue.append((root, 0))

    while queue:
        node, hd = queue.popleft()

        bottomView[hd] = node.val

        if node.left:
            queue.append((node.left, hd - 1))

        if node.right:
            queue.append((node.right, hd + 1))

    for hd in sorted(bottomView.keys()):
        print(bottomView[hd], end=' ')
    print()

# Example usage
# Construct the binary tree
root1 = TreeNode(20)
root1.left = TreeNode(8)
root1.right = TreeNode(22)
root1.left.left = TreeNode(5)
root1.left.right = TreeNode(3)
root1.right.right = TreeNode(25)
root1.left.right.left = TreeNode(10)
root1.left.right.right = TreeNode(14)

# Print the bottom view of the binary tree
print("Bottom view 1:")
print_bottom_view(root1)  # Output: 5 10 3 14 25

# Construct another binary tree
root2 = TreeNode(20)
root2.left = TreeNode(8)
root2.right = TreeNode(22)
root2.left.left = TreeNode(5)
root2.left.right = TreeNode(3)
root2.right.left = TreeNode(4)
root2.right.right = TreeNode(25)
root2.left.right.left = TreeNode(10)
root2.left.right.right = TreeNode(14)

# Print the bottom view of the binary tree
print("Bottom view 2:")
print_bottom_view(root2)  # Output: 5 10 4 14 25

                                                                                                                                
                                                                                                                                         





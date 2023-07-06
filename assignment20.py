
💡 Question-1

# Given a binary tree, your task is to find subtree with maximum sum in tree.

# Solution

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxSubtreeSum(root):
    if root is None:
        return 0
    
    left_sum = maxSubtreeSum(root.left)
    right_sum = maxSubtreeSum(root.right)
    
    current_sum = root.val + left_sum + right_sum
    
    global max_sum
    global max_subtree_root
    
    if current_sum > max_sum:
        max_sum = current_sum
        max_subtree_root = root
    
    return current_sum


# Construct the binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# Initialize the maximum sum and subtree root variables
max_sum = float('-inf')
max_subtree_root = None

# Find the subtree with maximum sum
maxSubtreeSum(root)

# Print the maximum sum and the subtree values
print("Maximum Sum:", max_sum)
print("Subtree Root:", max_subtree_root.val)



💡 Question-2

# Construct the BST (Binary Search Tree) from its given level order traversal.

# Solution - 

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def constructBST(arr):
    if not arr:
        return None

    root = TreeNode(arr[0])
    queue = []
    queue.append(root)
    i = 1

    while i < len(arr):
        current = queue.pop(0)

        left_val = arr[i]
        if left_val is not None:
            left_node = TreeNode(left_val)
            current.left = left_node
            queue.append(left_node)

        i += 1

        if i < len(arr):
            right_val = arr[i]
            if right_val is not None:
                right_node = TreeNode(right_val)
                current.right = right_node
                queue.append(right_node)

            i += 1

    return root

# Driver code 
arr = [7, 4, 12, 3, 6, 8, 1, 5, 10]
root = constructBST(arr)

# Function to print the BST in in-order traversal
def inorderTraversal(node):
    if node is not None:
        inorderTraversal(node.left)
        print(node.val, end=' ')
        inorderTraversal(node.right)

# Print the constructed BST
inorderTraversal(root)



💡 Question-3

# Given an array of size n. The problem is to check whether the given array can represent the level order traversal of a Binary Search Tree or not.

# Solution

def isLevelOrderBST(arr):
    if len(arr) <= 1:
        return True

    root = arr[0]
    n = len(arr)

    left_subtree = []
    right_subtree = []

    i = 1
    while i < n and arr[i] < root:
        left_subtree.append(arr[i])
        i += 1

    for j in range(i, n):
        if arr[j] < root:
            return False
        right_subtree.append(arr[j])

    return isLevelOrderBST(left_subtree) and isLevelOrderBST(right_subtree)

# Example usage
arr1 = [7, 4, 12, 3, 6, 8, 1, 5, 10]
print("Output1:", isLevelOrderBST(arr1))  # Output1: True

arr2 = [11, 6, 13, 5, 12, 10]
print("Output2:", isLevelOrderBST(arr2))  # Output2: False




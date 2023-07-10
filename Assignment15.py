
# 💡 Que1: - Given an array **arr[ ]** of size **N** having elements, the task is to find the next greater element for each element of the array in order of their appearance in the array.Next greater element of an element in the array is the nearest element on the right which is greater than the current element.If there does not exist next greater of current element, then next greater element for current element is -1. For example, next greater of the last element is always -1.

# **Example 1:**
# Input:
# N = 4, arr[] = [1 3 2 4]
# Output:
# 3 4 4 -1
# Explanation:
# In the array, the next larger element
# to 1 is 3 , 3 is 4 , 2 is 4 and for 4 ?
# since it doesn't exist, it is -1.

# Solution

def find_next_greater_elements(arr):
    stack = []
    result = [-1] * len(arr)

    for i in range(len(arr) - 1, -1, -1):
        while stack and stack[-1] <= arr[i]:
            stack.pop()

        if stack:
            result[i] = stack[-1]

        stack.append(arr[i])

    return result

# Driver code
arr = [1, 3, 2, 4]
next_greater = find_next_greater_elements(arr)
print(next_greater)



# 💡 **Question 2**

# Given an array **a** of integers of length **n**, find the nearest smaller number for every element such that the smaller element is on left side.If no small element present on the left print -1.

# **Example 1:**
# Input: n = 3
# a = {1, 6, 2}
# Output: -1 1 1
# Explaination: There is no number at the
# left of 1. Smaller number than 6 and 2 is 1.

# Solution

def find_nearest_smaller_numbers(a):
    stack = []
    result = [-1] * len(a)

    for i in range(len(a)):
        while stack and stack[-1] >= a[i]:
            stack.pop()

        if stack:
            result[i] = stack[-1]

        stack.append(a[i])

    return result

# Example usage
a = [1, 6, 2]
nearest_smaller = find_nearest_smaller_numbers(a)
print(nearest_smaller)



# 💡 **Question 3**

# Implement a Stack using two queues **q1** and **q2**.

  
# Example 1:

# Input:
# push(2)
# push(3)
# pop()
# push(4)
# pop()
# Output:3 4
# Explanation:
# push(2) the stack will be {2}
# push(3) the stack will be {2 3}
# pop()   poped element will be 3 the
#         stack will be {2}
# push(4) the stack will be {2 4}
# pop()   poped element will be 4


# Soluion

class Stack:
    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, val):
        self.q1.append(val)

    def pop(self):
        if not self.q1:
            return None

        while len(self.q1) > 1:
            self.q2.append(self.q1.pop(0))

        popped_element = self.q1.pop(0)

        self.q1, self.q2 = self.q2, self.q1

        return popped_element


# Example usage
stack = Stack()
stack.push(2)
stack.push(3)
print(stack.pop())  # Output: 3
stack.push(4)
print(stack.pop())  # Output: 4




# 💡 **Question 4**

# You are given a stack **St**. You have to reverse the stack using recursion.

# Example 1:

# Input:St = {3,2,1,7,6}
# Output:{6,7,1,2,3}

# Solution

def reverse_stack(St):
    if len(St) <= 1:
        return St

    temp = St.pop()
    reversed_stack = reverse_stack(St)
    reversed_stack.append(temp)

    return reversed_stack


# Example usage
St = [3, 2, 1, 7, 6]
reversed_St = reverse_stack(St)
print(reversed_St)



# 💡 **Question 5**

# You are given a string **S**, the task is to reverse the string using stack.

# # **Example 1:**

# Input: S="GeeksforGeeks"
# Output: skeeGrofskeeG

# Solution 

def reverse_string(S):
    stack = []
    reversed_string = ""

    # Push characters onto the stack
    for char in S:
        stack.append(char)

    # Pop characters from the stack to reverse the string
    while stack:
        reversed_string += stack.pop()

    return reversed_string

# Example 
S = "GeeksforGeeks"
reversed_S = reverse_string(S)
print(reversed_S)



# 💡 **Question 6**

# Given string **S** representing a postfix expression, the task is to evaluate the expression and find the final value. Operators will only include the basic arithmetic operators like ***, /, + and -**.

# Example 1:

# Input: S = "231*+9-"
# Output: -4
# Explanation:
# After solving the given expression,
# we have -4 as result.

# Solution 

def evaluate_postfix_expression(S):
    stack = []

    for char in S:
        if char.isdigit():
            stack.append(int(char))
        else:
            num2 = stack.pop()
            num1 = stack.pop()

            result = None
            if char == '+':
                result = num1 + num2
            elif char == '-':
                result = num1 - num2
            elif char == '*':
                result = num1 * num2
            elif char == '/':
                result = num1 / num2

            stack.append(result)

    return stack.pop()


# Example usage
S = "231*+9-"
result = evaluate_postfix_expression(S)
print(result)


💡 **Question 7**

# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# Implement the `MinStack` class:

# - `MinStack()` initializes the stack object.
# - `void push(int val)` pushes the element `val` onto the stack.
# - `void pop()` removes the element on the top of the stack.
# - `int top()` gets the top element of the stack.
# - `int getMin()` retrieves the minimum element in the stack.

# You must implement a solution with `O(1)` time complexity for each function.

# **Example 1:**
# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]

# Output
# [null,null,null,null,-3,null,0,-2]

# Explanation
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top();    // return 0
# minStack.getMin(); // return -2


# Solution 

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        if self.stack:
            popped_element = self.stack.pop()
            if popped_element == self.min_stack[-1]:
                self.min_stack.pop()
            return popped_element

    def top(self):
        if self.stack:
            return self.stack[-1]

    def getMin(self):
        if self.min_stack:
            return self.min_stack[-1]


# 💡 **Question 8**

# Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, compute how much water it can trap after raining.

# **Example 1:**

# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

# Solutions

def trap_water(height):
    left = 0
    right = len(height) - 1
    left_max = right_max = total_water = 0

    while left <= right:
        if height[left] <= height[right]:
            left_max = max(left_max, height[left])
            total_water += left_max - height[left]
            left += 1
        else:
            right_max = max(right_max, height[right])
            total_water += right_max - height[right]
            right -= 1

    return total_water

# Example usage
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
water_trapped = trap_water(height)
print(water_trapped)





  

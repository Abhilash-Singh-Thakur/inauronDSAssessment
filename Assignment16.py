
# 💡 **Question 1**

# Given an array, for each element find the value of the nearest element to the right which is having a frequency greater than that of the current element. If there does not exist an answer for a position, then make the value ‘-1’.

# **Examples:**

# Input: a[] = [1, 1, 2, 3, 4, 2, 1]
# Output : [-1, -1, 1, 2, 2, 1, -1]

# Explanation:
# Given array a[] = [1, 1, 2, 3, 4, 2, 1]
# Frequency of each element is: 3, 3, 2, 1, 1, 2, 3

# Lets calls Next Greater Frequency element as NGF
# 1. For element a[0] = 1 which has a frequency = 3,
#    As it has frequency of 3 and no other next element
#    has frequency more than 3 so  '-1'
# 2. For element a[1] = 1 it will be -1 same logic
#    like a[0]
# 3. For element a[2] = 2 which has frequency = 2,
#    NGF element is 1 at position = 6  with frequency
#    of 3 > 2
# 4. For element a[3] = 3 which has frequency = 1,
#    NGF element is 2 at position = 5 with frequency
#    of 2 > 1
# 5. For element a[4] = 4 which has frequency = 1,
#    NGF element is 2 at position = 5 with frequency
#    of 2 > 1
# 6. For element a[5] = 2 which has frequency = 2,
#    NGF element is 1 at position = 6 with frequency
#    of 3 > 2
# 7. For element a[6] = 1 there is no element to its
#    right, hence -1

# Solution

def find_nearest_greater_frequency(a):
    stack = []
    frequency = {}
    result = [-1] * len(a)

    for i in range(len(a) - 1, -1, -1):
        frequency[a[i]] = frequency.get(a[i], 0) + 1

        while stack and frequency[stack[-1]] <= frequency[a[i]]:
            stack.pop()

        if stack:
            result[i] = stack[-1]

        stack.append(a[i])

    return result


# Example usage
a = [1, 1, 2, 3, 4, 2, 1]
nearest_greater_frequency = find_nearest_greater_frequency(a)
print(nearest_greater_frequency)


# 💡 **Question 2**

# Given a stack of integers, sort it in ascending order using another temporary stack.

# **Examples:**
  
# Input : [34, 3, 31, 98, 92, 23]
# Output : [3, 23, 31, 34, 92, 98]

# Input : [3, 5, 1, 4, 2, 8]
# Output : [1, 2, 3, 4, 5, 8]

# Solution

def sort_stack(stack):
    temp_stack = []

    while stack:
        temp = stack.pop()

        while temp_stack and temp_stack[-1] > temp:
            stack.append(temp_stack.pop())

        temp_stack.append(temp)

    while temp_stack:
        stack.append(temp_stack.pop())

    return stack


# Example usage
stack = [34, 3, 31, 98, 92, 23]
sorted_stack = sort_stack(stack)
print(sorted_stack)


# 💡 **Question 3**

# Given a stack with **push()**, **pop()**, and **empty()** operations, The task is to delete the **middle** element ****of it without using any additional data structure.

# Input  : Stack[] = [1, 2, 3, 4, 5]

# Output : Stack[] = [1, 2, 4, 5]

# Input  : Stack[] = [1, 2, 3, 4, 5, 6]

# Output : Stack[] = [1, 2, 4, 5, 6]

# Solution -

def delete_middle(stack):
    size = len(stack)
    mid = size // 2

    def delete_middle_recursive(stack, current_index, is_middle_found):
        if current_index == mid:
            stack.pop()
            is_middle_found[0] = True
            return

        temp = stack.pop()
        delete_middle_recursive(stack, current_index + 1, is_middle_found)

        if not is_middle_found[0]:
            stack.append(temp)

    is_middle_found = [False]
    delete_middle_recursive(stack, 0, is_middle_found)

# Example usage
stack = [1, 2, 3, 4, 5]
delete_middle(stack)
print(stack)



# 💡 **Question 4**

# Given a Queue consisting of first **n** natural numbers (in random order). The task is to check whether the given Queue elements can be arranged in increasing order in another Queue using a stack. The operation allowed are:

# 1. Push and pop elements from the stack
# 2. Pop (Or Dequeue) from the given Queue.
# 3. Push (Or Enqueue) in the another Queue.

# **Examples :**

# Input : Queue[] = { 5, 1, 2, 3, 4 } 

# Output : Yes 

# Pop the first element of the given Queue 

# i.e 5. Push 5 into the stack. 

# Now, pop all the elements of the given Queue and push them to second Queue. 

# Now, pop element 5 in the stack and push it to the second Queue.   

# Input : Queue[] = { 5, 1, 2, 6, 3, 4 } 

# Output : No 

# Push 5 to stack. 

# Pop 1, 2 from given Queue and push it to another Queue. 

# Pop 6 from given Queue and push to stack. 

# Pop 3, 4 from given Queue and push to second Queue. 

# Now, from using any of above operation,

# Solution -

def check_arrangement(queue):
    stack = []
    second_queue = []

    expected_element = 1

    while queue:
        if queue[0] == expected_element:
            second_queue.append(queue.pop(0))
            expected_element += 1
        elif stack and stack[-1] == expected_element:
            second_queue.append(stack.pop())
            expected_element += 1
        else:
            stack.append(queue.pop(0))

    while stack and stack[-1] == expected_element:
        second_queue.append(stack.pop())
        expected_element += 1

    return not queue and not stack


# Example usage
queue1 = [5, 1, 2, 3, 4]
print(check_arrangement(queue1))  # Output: True

queue2 = [5, 1, 2, 6, 3, 4]
print(check_arrangement(queue2))  # Output: False


# 💡 **Question 5**

# Given a number , write a program to reverse this number using stack.

# **Examples:**

# Input : 365
# Output : 563

# Input : 6899
# Output : 9986

# Solution --

def reverse_number(number):
    stack = []

    # Extract digits and push them onto the stack
    while number > 0:
        digit = number % 10
        stack.append(digit)
        number //= 10

    reversed_number = 0
    decimal_place = 1

    # Build the reversed number from the stack
    while stack:
        digit = stack.pop()
        reversed_number += digit * decimal_place
        decimal_place *= 10

    return reversed_number


# Example usage
number1 = 365
reversed_number1 = reverse_number(number1)
print(reversed_number1)  # Output: 563

number2 = 6899
reversed_number2 = reverse_number(number2)
print(reversed_number2)  # Output: 9986



# 💡 **Question 6**

# Given an integer k and a **[queue](https://www.geeksforgeeks.org/queue-data-structure/)** of integers, The task is to reverse the order of the first **k** elements of the queue, leaving the other elements in the same relative order.

# Only following standard operations are allowed on queue.

# - **enqueue(x) :** Add an item x to rear of queue
# - **dequeue() :** Remove an item from front of queue
# - **size() :** Returns number of elements in queue.
# - **front() :** Finds front item.

# Solution 

def reverse_k_elements(queue, k):
    if not queue or k <= 0 or k > len(queue):
        return

    stack = []

    # Dequeue and push the first k elements onto the stack
    for _ in range(k):
        element = queue.pop(0)
        stack.append(element)

    # Enqueue the remaining elements back into the given queue
    while queue:
        queue.append(queue.pop(0))

    # Pop elements from the stack and enqueue them back into the given queue
    while stack:
        queue.append(stack.pop())


# Example usage
queue = [1, 2, 3, 4, 5]
k = 3


# 💡 **Question 7**

# Given a sequence of n strings, the task is to check if any two similar words come together and then destroy each other then print the number of words left in the sequence after this pairwise destruction.

# **Examples:**

# Input : ab aa aa bcd ab

# Output : 3

# *As aa, aa destroys each other so,*

# *ab bcd ab is the new sequence.*

# Input :  tom jerry jerry tom

# Output : 0

# *As first both jerry will destroy each other.*

# *Then sequence will be tom, tom they will also destroy*

# *each other. So, the final sequence doesn’t contain any*

# *word.*

# Solution

def count_words_left(sequence):
    words = sequence.split()
    remaining_words = []

    for word in words:
        if remaining_words and remaining_words[-1] == word:
            remaining_words.pop()
        else:
            remaining_words.append(word)

    return len(remaining_words)


# Example usage
sequence1 = "ab aa aa bcd ab"
result1 = count_words_left(sequence1)
print(result1)  # Output: 3

sequence2 = "tom jerry jerry tom"
result2 = count_words_left(sequence2)
print(result2)  # Output: 0


# 💡 **Question 8**

# Given an array of integers, the task is to find the maximum absolute difference between the nearest left and the right smaller element of every element in the array.

# **Note:** If there is no smaller element on right side or left side of any element then we take zero as the smaller element. For example for the leftmost element, the nearest smaller element on the left side is considered as 0. Similarly, for rightmost elements, the smaller element on the right side is considered as 0.

# **Examples:**

# Input : arr[] = {2, 1, 8}
# Output : 1
# Left smaller  LS[] {0, 0, 1}
# Right smaller RS[] {1, 0, 0}
# Maximum Diff of abs(LS[i] - RS[i]) = 1

# Input  : arr[] = {2, 4, 8, 7, 7, 9, 3}
# Output : 4
# Left smaller   LS[] = {0, 2, 4, 4, 4, 7, 2}
# Right smaller  RS[] = {0, 3, 7, 3, 3, 3, 0}
# Maximum Diff of abs(LS[i] - RS[i]) = 7 - 3 = 4

# Input : arr[] = {5, 1, 9, 2, 5, 1, 7}
# Output : 1

# Solution

def max_abs_difference(arr):
    N = len(arr)
    max_diff = 0
    stack = []

    # Compute left smaller indices
    for i in range(N):
        while stack and arr[i] <= arr[stack[-1]]:
            top = stack.pop()
            left_smaller_index = stack[-1] if stack else -1
            diff = i - left_smaller_index - 1
            max_diff = max(max_diff, diff)
        stack.append(i)

    # Clear the stack
    stack.clear()

    # Compute right smaller indices
    for i in range(N-1, -1, -1):
        while stack and arr[i] <= arr[stack[-1]]:
            top = stack.pop()
            right_smaller_index = stack[-1] if stack else N
            diff = right_smaller_index - i - 1
            max_diff = max(max_diff, diff)
        stack.append(i)

    return max_diff


# Example usage
arr1 = [2, 1, 8]
result1 = max_abs_difference(arr1)
print(result1)  # Output: 1

arr2 = [2, 4, 8, 7, 7, 9, 3]
result2 = max_abs_difference(arr2)
print(result2)  # Output: 4

arr3 = [5, 1, 9, 2, 5, 1, 7]
result3 = max_abs_difference(arr3)
print(result3)  # Output: 1


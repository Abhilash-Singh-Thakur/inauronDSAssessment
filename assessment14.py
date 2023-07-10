
# 💡 **Question 1**

# Given a linked list of **N** nodes such that it may contain a loop.

# A loop here means that the last node of the link list is connected to the node at position X(1-based index). If the link list does not have any loop, X=0.

# Remove the loop from the linked list, if it is present, i.e. unlink the last node which is forming the loop.

# Solution

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def detectAndRemoveLoop(head):
    if not head or not head.next:
        return head

    slow = head
    fast = head

    # Detect loop
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    # No loop present
    if not fast or not fast.next:
        return head

    # Reset slow to head
    slow = head

    # Find the starting point of the loop
    while slow != fast:
        slow = slow.next
        fast = fast.next

    # Remove the loop by setting the next of the last node to None
    prev = None
    while fast.next != slow:
        prev = fast
        fast = fast.next

    prev.next = None

    return head

# Test the implementation with the provided example
head = ListNode(1)
head.next = ListNode(3)
head.next.next = ListNode(4)
head.next.next.next = head.next

newHead = detectAndRemoveLoop(head)
if not newHead:
    print("No loop")
else:
    node = newHead
    while node:
        print(node.val, end=" ")
        node = node.next


# 💡 **Question 2**

# A number **N** is represented in Linked List such that each digit corresponds to a node in linked list. You need to add 1 to it.

# **Example 1:**

#   Input:
# LinkedList: 4->5->6
# Output:457

# Solution

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseLinkedList(head):
    prev = None
    curr = head
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev

def addOne(head):
    # Reverse the linked list
    reversedHead = reverseLinkedList(head)

    # Traverse the reversed list and add 1
    curr = reversedHead
    carry = 1
    while curr:
        sum = curr.val + carry
        curr.val = sum % 10
        carry = sum // 10
        if carry == 0:
            break
        curr = curr.next

    # If there is still a carry, append a new node
    if carry > 0:
        curr.next = ListNode(carry)

    # Reverse the modified linked list
    newHead = reverseLinkedList(reversedHead)

    return newHead

# Test the implementation with the provided example
head = ListNode(4)
head.next = ListNode(5)
head.next.next = ListNode(6)

newHead = addOne(head)
while newHead:
    print(newHead.val, end=" ")
    newHead = newHead.next


# 💡 **Question 3**

# Given a Linked List of size N, where every node represents a sub-linked-list and contains two pointers:(i) a **next** pointer to the next node,(ii) a **bottom** pointer to a linked list where this node is head.Each of the sub-linked-list is in sorted order.Flatten the Link List such that all the nodes appear in a single level while maintaining the sorted order. **Note:** The flattened list will be printed using the bottom pointer instead of next pointer.

# **Example 1**


class ListNode:
    def __init__(self, val=0, next=None, bottom=None):
        self.val = val
        self.next = next
        self.bottom = bottom

def mergeLists(head1, head2):
    if not head1:
        return head2
    if not head2:
        return head1

    if head1.val < head2.val:
        mergedHead = head1
        mergedHead.bottom = mergeLists(head1.bottom, head2)
    else:
        mergedHead = head2
        mergedHead.bottom = mergeLists(head1, head2.bottom)

    return mergedHead

def flattenLinkedList(head):
    if not head or not head.next:
        return head

    head.next = flattenLinkedList(head.next)

    return mergeLists(head, head.next)

# Test the implementation with the provided example
head = ListNode(5)
head.next = ListNode(10)
head.next.bottom = ListNode(7)
head.next.next = ListNode(19)
head.next.next.bottom = ListNode(8)
head.next.next.next = ListNode(20)
head.next.next.next.bottom = ListNode(22)

flattenedHead = flattenLinkedList(head)

while flattenedHead:
    print(flattenedHead.val, end=" ")
    flattenedHead = flattenedHead.bottom


# 💡 **Question 4**

# You are given a special linked list with **N** nodes where each node has a next pointer pointing to its next node. You are also given **M** random pointers, where you will be given **M** number of pairs denoting two nodes **a** and **b**  **i.e. a->arb = b** (arb is pointer to random node)**.**

# Construct a copy of the given list. The copy should consist of exactly **N** new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

# For example, if there are two nodes **X** and **Y** in the original list, where **X.arb** **-->** **Y**, then for the corresponding two nodes **x** and **y** in the copied list, **x.arb --> y.**

# Return the head of the copied linked list.

# SOlution

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.random = None

def copyRandomList(head):
    if not head:
        return None

    mapping = {}
    curr = head

    # Create a copy of each node and store the mapping
    while curr:
        mapping[curr] = Node(curr.data)
        curr = curr.next

    # Set the next and random pointers of the copied nodes
    curr = head
    while curr:
        copied_node = mapping[curr]
        copied_node.next = mapping.get(curr.next)
        copied_node.random = mapping.get(curr.random)
        curr = curr.next

    return mapping[head]

# Test the implementation with the provided example
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

head.random = head.next.next
head.next.random = head.next.next.next

copied_head = copyRandomList(head)

# Print the values of the copied linked list and its random pointers
curr = copied_head
while curr:
    print("Value:", curr.data, end=" ")
    if curr.random:
       

# 💡 **Question 5**

# Given the `head` of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return *the reordered list*.

# The **first** node is considered **odd**, and the **second** node is **even**, and so on.

# Note that the relative order inside both the even and odd groups should remain as it was in the input.

# You must solve the problem in `O(1)` extra space complexity and `O(n)` time complexity.

# **Example 1:**
# Input: head = [1,2,3,4,5]
# Output: [1,3,5,2,4]

# Solution

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def oddEvenList(head):
    if not head or not head.next:
        return head

    odd_head = head
    even_head = head.next
    odd = odd_head
    even = even_head

    while even and even.next:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next

    odd.next = even_head

    return odd_head

# Test the implementation with the provided example
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

reordered_head = oddEvenList(head)

# Print the values of the reordered linked list
curr = reordered_head
while curr:
    print(curr.val, end=" ")
    curr = curr.next

# 💡 **Question 6**

# Given a singly linked list of size **N**. The task is to **left-shift** the linked list by **k** nodes, where **k** is a given positive integer smaller than or equal to length of the linked list.

# **Example 1:**

# Input:
# N = 5
# value[] = {2, 4, 7, 8, 9}
# k = 3
# Output:8 9 2 4 7
# Explanation:Rotate 1:4 -> 7 -> 8 -> 9 -> 2
# Rotate 2: 7 -> 8 -> 9 -> 2 -> 4
# Rotate 3: 8 -> 9 -> 2 -> 4 -> 7

# Solution

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def leftShift(head, k):
    if not head or not head.next or k == 0:
        return head

    # Find the k+1th node from the start
    temp = head
    for _ in range(k):
        if temp.next:
            temp = temp.next
        else:
            # Wrap around the list if k > N
            temp = head

    new_head = temp.next
    temp.next = None

    # Traverse to the end and link it to the original head
    curr = new_head
    while curr.next:
        curr = curr.next
    curr.next = head

    return new_head

# Test the implementation with the provided example
head = ListNode(2)
head.next = ListNode(4)
head.next.next = ListNode(7)
head.next.next.next = ListNode(8)
head.next.next.next.next = ListNode(9)

shifted_head = leftShift(head, 3)

# Print the values of the shifted linked list
curr = shifted_head
while curr:
    print(curr.val, end=" ")
    curr = curr.next



# 💡 **Question 7**

# You are given the `head` of a linked list with `n` nodes.

# For each node in the list, find the value of the **next greater node**. That is, for each node, find the value of the first node that is next to it and has a **strictly larger** value than it.

# Return an integer array `answer` where `answer[i]` is the value of the next greater node of the `ith` node (**1-indexed**). If the `ith` node does not have a next greater node, set `answer[i] = 0`

# Solution



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def nextGreaterNodes(head):
    # Convert the linked list to a list for easier manipulation
    values = []
    curr = head
    while curr:
        values.append(curr.val)
        curr = curr.next

    stack = []  # Stack to keep track of greater nodes
    result = [0] * len(values)  # Array to store the next greater nodes

    for i in range(len(values) - 1, -1, -1):
        while stack and values[i] >= stack[-1]:
            stack.pop()

        if stack:
            result[i] = stack[-1]

        stack.append(values[i])

    return result

# Test the implementation with the provided example
head = ListNode(2)
head.next = ListNode(7)
head.next.next = ListNode(4)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(5)

answer = nextGreaterNodes(head)
print(answer)  # Output: [7, 0, 5, 5, 0]


💡 **Question 8**

Given the `head` of a linked list, we repeatedly delete consecutive sequences of nodes that sum to `0` until there are no such sequences.

After doing so, return the head of the final linked list.  You may return any such answer.

(Note that in the examples below, all sequences are serializations of `ListNode` objects.)

# Solution

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeZeroSumSublists(head):
    # Create a dummy node as the prefix sum of 0
    dummy = ListNode(0)
    dummy.next = head

    prefix_sum = 0
    prefix_sum_map = {}  # Map to store prefix sums and their corresponding nodes

    # Traverse the list to calculate prefix sums
    curr = dummy
    while curr:
        prefix_sum += curr.val

        if prefix_sum in prefix_sum_map:
            # Remove nodes between the previous occurrence of prefix sum and the current node
            prev = prefix_sum_map[prefix_sum].next
            prev_sum = prefix_sum + prev.val
            while prev_sum != prefix_sum:
                del prefix_sum_map[prev_sum]
                prev = prev.next
                prev_sum += prev.val

            prefix_sum_map[prefix_sum].next = curr.next
        else:
            prefix_sum_map[prefix_sum] = curr

        curr = curr.next

    return dummy.next

# Test the implementation with the provided example
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(-3)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(1)

result = removeZeroSum


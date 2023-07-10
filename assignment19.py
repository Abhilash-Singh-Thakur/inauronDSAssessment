
# 💡 1. **Merge k Sorted Lists**

# You are given an array of `k` linked-lists `lists`, each linked-list is sorted in ascending order.

# *Merge all the linked-lists into one sorted linked-list and return it.*

# **Example 1:** Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    if not lists:
        return None
    n = len(lists)
    if n == 1:
        return lists[0]
    mid = n // 2
    left_lists = mergeKLists(lists[:mid])
    right_lists = mergeKLists(lists[mid:])
    return mergeTwoLists(left_lists, right_lists)

def mergeTwoLists(l1, l2):
    if not l1:
        return l2
    if not l2:
        return l1
    if l1.val <= l2.val:
        l1.next = mergeTwoLists(l1.next, l2)
        return l1
    else:
        l2.next = mergeTwoLists(l1, l2.next)
        return l2


# 💡 2. **Count of Smaller Numbers After Self**

# Given an integer array `nums`, return *an integer array* `counts` *where* `counts[i]` *is the number of smaller elements to the right of* `nums[i]`.

# **Example 1:**

# Input: nums = [5,2,6,1]
# Output: [2,1,1,0]
# Explanation:
# To the right of 5 there are2 smaller elements (2 and 1).
# To the right of 2 there is only1 smaller element (1).
# To the right of 6 there is1 smaller element (1).
# To the right of 1 there is0 smaller element.

# Solution

def countSmaller(nums):
    def merge_and_count(left, right, count):
        merged = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i][1] <= right[j][1]:
                merged.append(left[i])
                count[left[i][0]] += j
                i += 1
            else:
                merged.append(right[j])
                j += 1
        while i < len(left):
            merged.append(left[i])
            count[left[i][0]] += j
            i += 1
        while j < len(right):
            merged.append(right[j])
            j += 1
        return merged

    def merge_sort_and_count(nums, count):
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left = merge_sort_and_count(nums[:mid], count)
        right = merge_sort_and_count(nums[mid:], count)
        return merge_and_count(left, right, count)

    count = [0] * len(nums)
    nums = [(i, num) for i, num in enumerate(nums)]
    merge_sort_and_count(nums, count)
    return count

# Test the implementation with the provided input
nums = [5, 2, 6, 1]
result = countSmaller(nums)
print(result)  # Output: [2, 1, 1, 0]
def countSmaller(nums):
    def merge_and_count(left, right, count):
        merged = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i][1] <= right[j][1]:
                merged.append(left[i])
                count[left[i][0]] += j
                i += 1
            else:
                merged.append(right[j])
                j += 1
        while i < len(left):
            merged.append(left[i])
            count[left[i][0]] += j
            i += 1
        while j < len(right):
            merged.append(right[j])
            j += 1
        return merged

    def merge_sort_and_count(nums, count):
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left = merge_sort_and_count(nums[:mid], count)
        right = merge_sort_and_count(nums[mid:], count)
        return merge_and_count(left, right, count)

    count = [0] * len(nums)
    nums = [(i, num) for i, num in enumerate(nums)]
    merge_sort_and_count(nums, count)
    return count


# 💡 3. **Sort an Array**

# Given an array of integers `nums`, sort the array in ascending order and return it.

# You must solve the problem **without using any built-in** functions in `O(nlog(n))` time complexity and with the smallest space complexity possible.

# **Example 1:**
# Input: nums = [5,2,3,1]
# Output: [1,2,3,5]
# Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).

# Solution

def sortArray(nums):
    def merge(left, right):
        merged = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged

    def merge_sort(nums):
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left = merge_sort(nums[:mid])
        right = merge_sort(nums[mid:])
        return merge(left, right)

    return merge_sort(nums)


# 💡 4. **Move all zeroes to end of array**

# Given an array of random numbers, Push all the zero’s of a given array to the end of the array. For example, if the given arrays is {1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0}, it should be changed to {1, 9, 8, 4, 2, 7, 6, 0, 0, 0, 0}. The order of all other elements should be same. Expected time complexity is O(n) and extra space is O(1).

# **Example:**
# Input :  arr[] = {1, 2, 0, 4, 3, 0, 5, 0};
# Output : arr[] = {1, 2, 4, 3, 5, 0, 0, 0};

# Input : arr[]  = {1, 2, 0, 0, 0, 3, 6};
# Output : arr[] = {1, 2, 3, 6, 0, 0, 0};

# Solution

def moveZeroes(nums):
    left = 0
    right = 0
    while right < len(nums):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
        right += 1

# Test the implementation with the provided input
nums = [1, 2, 0, 4, 3, 0, 5, 0]
moveZeroes(nums)
print(nums)  # Output: [1, 2, 4, 3, 5, 0, 0, 0]

nums = [1, 2, 0, 0, 0, 3, 6]
moveZeroes(nums)
print(nums)  # Output: [1, 2, 3, 6, 0, 0, 0]


# 💡 5. **Rearrange array in alternating positive & negative items with O(1) extra space**

# Given an **array of positive** and **negative numbers**, arrange them in an **alternate** fashion such that every positive number is followed by a negative and vice-versa maintaining the **order of appearance**. The number of positive and negative numbers need not be equal. If there are more positive numbers they appear at the end of the array. If there are more negative numbers, they too appear at the end of the array.

# **Examples:**

# > Input:  arr[] = {1, 2, 3, -4, -1, 4}
# Output: arr[] = {-4, 1, -1, 2, 3, 4}

# Input:  arr[] = {-5, -2, 5, 2, 4, 7, 1, 8, 0, -8}
# Output: arr[] = {-5, 5, -2, 2, -8, 4, 7, 1, 8, 0}

# Solution

def rearrangeArray(nums):
    left = 0
    right = 0
    n = len(nums)
    while left < n and right < n:
        if nums[left] >= 0:
            right = max(right, left + 1)
            while right < n and nums[right] >= 0:
                right += 1
            if right < n:
                rotateRight(nums, left, right)
        left += 1

def rotateRight(nums, start, end):
    temp = nums[end]
    for i in range(end, start, -1):
        nums[i] = nums[i - 1]
    nums[start] = temp

# Test the implementation with the provided input
nums = [1, 2, 3, -4, -1, 4]
rearrangeArray(nums)
print(nums)  # Output: [-4, 1, -1, 2, 3, 4]

nums = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]
rearrangeArray(nums)
print(nums)  # Output: [-5, 5, -2, 2, -8, 4, 7, 1, 8, 0]

# 💡 **6. Merge two sorted arrays**

# Given two sorted arrays, the task is to merge them in a sorted manner.
# **Examples:**

# > Input: arr1[] = { 1, 3, 4, 5}, arr2[] = {2, 4, 6, 8} 
# Output: arr3[] = {1, 2, 3, 4, 4, 5, 6, 8}

# Input: arr1[] = { 5, 8, 9}, arr2[] = {4, 7, 8}
# Output: arr3[] = {4, 5, 7, 8, 8, 9}

# Solution

def mergeSortedArrays(arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    i = 0
    j = 0
    result = []
    while i < n1 and j < n2:
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    while i < n1:
        result.append(arr1[i])
        i += 1
    while j < n2:
        result.append(arr2[j])
        j += 1
    return result

# Test the implementation with the provided examples
arr1 = [1, 3, 4, 5]
arr2 = [2, 4, 6, 8]
print(mergeSortedArrays(arr1, arr2))  # Output: [1, 2, 3, 4, 4, 5, 6, 8]



# 💡 7. **Intersection of Two Arrays**

# Given two integer arrays `nums1` and `nums2`, return *an array of their intersection*. Each element in the result must be **unique** and you may return the result in **any order**.

# **Example 1:**
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]

def intersection(nums1, nums2):
    set1 = set(nums1)
    intersection = set()
    for num in nums2:
        if num in set1:
            intersection.add(num)
    return list(intersection)

# Test the implementation with the provided example
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(intersection(nums1, nums2))  # Output: [2]


# 💡 8. **Intersection of Two Arrays II**

# Given two integer arrays `nums1` and `nums2`, return *an array of their intersection*. Each element in the result must appear as many times as it shows in both arrays and you may return the result in **any order**.

# **Example 1:**
# **Example 1:**
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]

# Solution

def intersect(nums1, nums2):
    freqMap = {}
    for num in nums1:
        if num in freqMap:
            freqMap[num] += 1
        else:
            freqMap[num] = 1
    
    intersection = []
    for num in nums2:
        if num in freqMap and freqMap[num] > 0:
            intersection.append(num)
            freqMap[num] -= 1
    
    return intersection

# Test the implementation with the provided example
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(intersect(nums1, nums2))  # Output: [2, 2]


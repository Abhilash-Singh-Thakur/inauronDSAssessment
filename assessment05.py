# 💡 **Question 1**

# Convert 1D Array Into 2D Array

# You are given a **0-indexed** 1-dimensional (1D) integer array original, and two integers, m and n. You are tasked with creating a 2-dimensional (2D) array with  m rows and n columns using **all** the elements from original.

# The elements from indices 0 to n - 1 (**inclusive**) of original should form the first row of the constructed 2D array, the elements from indices n to 2 * n - 1 (**inclusive**) should form the second row of the constructed 2D array, and so on.

# Return *an* m x n *2D array constructed according to the above procedure, or an empty 2D array if it is impossible*.

# Solution

def convert_to_2d_array(original, m, n):
    if m * n != len(original):
        return []  # Return an empty 2D array if it is impossible
    
    result = []
    for i in range(m):
        row = original[i * n : (i + 1) * n]
        result.append(row)
    
    return result

# 💡 **Question 2**

# You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase **may be** incomplete.

# Given the integer n, return *the number of **complete rows** of the staircase you will build*.

# Solution

def complete_rows(n):
    left = 0
    right = n
    while left <= right:
        mid = left + (right - left) // 2
        coins_needed = (mid * (mid + 1)) // 2

        if coins_needed == n:
            return mid
        elif coins_needed < n:
            left = mid + 1
        else:
            right = mid - 1
    
    return right

# 💡 **Question 3**

# Given an integer array nums sorted in **non-decreasing** order, return *an array of **the squares of each number** sorted in non-decreasing order*.

# **Example 1:**

# **Input:** nums = [-4,-1,0,3,10]

# **Output:** [0,1,9,16,100]

# **Explanation:** After squaring, the array becomes [16,1,0,9,100].

# After sorting, it becomes [0,1,9,16,100].

# Solution 

def sorted_squares(nums):
    n = len(nums)
    result = [0] * n
    left = 0
    right = n - 1
    index = n - 1

    while left <= right:
        if abs(nums[left]) > abs(nums[right]):
            result[index] = nums[left] ** 2
            left += 1
        else:
            result[index] = nums[right] ** 2
            right -= 1
        index -= 1

    return result


# 💡 **Question 4**

# Given two **0-indexed** integer arrays nums1 and nums2, return *a list* answer *of size* 2 *where:*

# - answer[0] *is a list of all **distinct** integers in* nums1 *which are **not** present in* nums2*.*
# - answer[1] *is a list of all **distinct** integers in* nums2 *which are **not** present in* nums1.

# **Note** that the integers in the lists may be returned in **any** order.

# **Example 1:**

# **Input:** nums1 = [1,2,3], nums2 = [2,4,6]

# **Output:** [[1,3],[4,6]]

# **Explanation:**

# For nums1, nums1[1] = 2 is present at index 0 of nums2, whereas nums1[0] = 1 and nums1[2] = 3 are not present in nums2. Therefore, answer[0] = [1,3].

# For nums2, nums2[0] = 2 is present at index 1 of nums1, whereas nums2[1] = 4 and nums2[2] = 6 are not present in nums2. Therefore, answer[1] = [4,6

# Solution

def distinct_nums(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)
    distinct_nums1 = list(set1 - set2)
    distinct_nums2 = list(set2 - set1)
    return [distinct_nums1, distinct_nums2]

# 💡 **Question 5**

# Given two integer arrays arr1 and arr2, and the integer d, *return the distance value between the two arrays*.

# The distance value is defined as the number of elements arr1[i] such that there is not any element arr2[j] where |arr1[i]-arr2[j]| <= d.

# **Example 1:**

# **Input:** arr1 = [4,5,8], arr2 = [10,9,1]

# Solution

def distance_value(arr1, arr2, d):
    distance = 0
    for num1 in arr1:
        valid = True
        for num2 in arr2:
            if abs(num1 - num2) <= d:
                valid = False
                break
        if valid:
            distance += 1
    return distance
    
# 💡 **Question 6**

# Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears **once** or **twice**, return *an array of all the integers that appears **twice***.

# You must write an algorithm that runs in O(n) time and uses only constant extra space.

# **Example 1:**

# **Input:** nums = [4,3,2,7,8,2,3,1]

# **Output:**

# [2,3]

# Solution

def find_duplicates(nums):
    result = []
    for num in nums:
        index = abs(num)
        if nums[index - 1] > 0:
            nums[index - 1] = -nums[index - 1]
        else:
            result.append(index)
    return result

💡 **Question 7**

Suppose an array of length n sorted in ascending order is **rotated** between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

- [4,5,6,7,0,1,2] if it was rotated 4 times.
- [0,1,2,4,5,6,7] if it was rotated 7 times.

Notice that **rotating** an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of **unique** elements, return *the minimum element of this array*.

You must write an algorithm that runs in O(log n) time.

**Example 1:**

**Input:** nums = [3,4,5,1,2]

# Solution

def find_min(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    return nums[left]

# 💡 **Question 8**

# An integer array original is transformed into a **doubled** array changed by appending **twice the value** of every element in original, and then randomly **shuffling** the resulting array.

# Given an array changed, return original *if* changed *is a **doubled** array. If* changed *is not a **doubled** array, return an empty array. The elements in* original *may be returned in **any** order*.

# **Example 1:**

# **Input:** changed = [1,3,4,2,6,8]

# **Output:** [1,3,4]



def find_original(changed):
    counter = {}

    for num in changed:
        if num not in counter:
            counter[num] = 0
        counter[num] += 1

    for num in counter:
        if counter[num * 2] != counter[num]:
            return []

    return list(counter.keys())


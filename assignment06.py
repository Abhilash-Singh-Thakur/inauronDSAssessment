# 💡 **Question 1**

# A permutation perm of n + 1 integers of all the integers in the range [0, n] can be represented as a string s of length n where:

# - s[i] == 'I' if perm[i] < perm[i + 1], and
# - s[i] == 'D' if perm[i] > perm[i + 1].

# Given a string s, reconstruct the permutation perm and return it. If there are multiple valid permutations perm, return **any of them**.

# **Example 1:**

# **Input:** s = "IDID"

# **Output:**

# [0,4,1,3,2]

# Solution

def reconstruct_permutation(s):
    n = len(s)
    perm = [0] * (n + 1)
    low, high = 0, n

    for i in range(n):
        if s[i] == 'I':
            perm[i] = low
            low += 1
        else:
            perm[i] = high
            high -= 1

    perm[n] = low

    return perm

# 💡 **Question 2**

# You are given an m x n integer matrix matrix with the following two properties:

# - Each row is sorted in non-decreasing order.
# - The first integer of each row is greater than the last integer of the previous row.

# Given an integer target, return true *if* target *is in* matrix *or* false *otherwise*.

# You must write a solution in O(log(m * n)) time complexity.

# Solution

def search_matrix(matrix, target):
    m, n = len(matrix), len(matrix[0])
    left, right = 0, m * n - 1

    while left <= right:
        mid = left + (right - left) // 2
        num = matrix[mid // n][mid % n]

        if num == target:
            return True
        elif num < target:
            left = mid + 1
        else:
            right = mid - 1

    return False




# 💡 **Question 3**

# Given an array of integers arr, return *true if and only if it is a valid mountain array*.

# Recall that arr is a mountain array if and only if:

# - arr.length >= 3
# - There exists some i with 0 < i < arr.length - 1 such that:
#     - arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
#     - arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

def valid_mountain_array(arr):
    n = len(arr)
    if n < 3:
        return False

    i = 0
    while i < n - 1 and arr[i] < arr[i + 1]:
        i += 1

    if i == 0 or i == n - 1:
        return False

    while i < n - 1 and arr[i] > arr[i + 1]:
        i += 1

    return i == n - 1

# 💡 **Question 4**

# Given a binary array nums, return *the maximum length of a contiguous subarray with an equal number of* 0 *and* 1.

# **Example 1:**

# **Input:** nums = [0,1]

# **Output:** 2

# **Explanation:**

# [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.

# Solution

def find_max_length(nums):
    count = 0
    max_length = 0
    count_map = {0: -1}  # Initial count of 0 is -1 to handle starting edge case

    for i, num in enumerate(nums):
        if num == 0:
            count -= 1
        else:
            count += 1

        if count in count_map:
            max_length = max(max_length, i - count_map[count])
        else:
            count_map[count] = i

    return max_length

# 💡 **Question 5**

# The **product sum** of two equal-length arrays a and b is equal to the sum of a[i] * b[i] for all 0 <= i < a.length (**0-indexed**).

# - For example, if a = [1,2,3,4] and b = [5,2,3,1], the **product sum** would be 1*5 + 2*2 + 3*3 + 4*1 = 22.

# Given two arrays nums1 and nums2 of length n, return *the **minimum product sum** if you are allowed to **rearrange** the **order** of the elements in* nums1.

# **Example 1:**

# **Input:** nums1 = [5,3,4,2], nums2 = [4,2,2,5]

# **Output:** 40

# **Explanation:**

# We can rearrange nums1 to become [3,5,4,2]. The product sum of [3,5,4,2] and [4,2,2,5] is 3*4 + 5*2 + 4*2 + 2*5 = 40.

# Solution

def min_product_sum(nums1, nums2):
    nums1.sort()
    nums2.sort(reverse=True)

    min_product = 0

    for i in range(len(nums1)):
        min_product += nums1[i] * nums2[i]

    return min_product

# 💡 **Question 6**

# An integer array original is transformed into a **doubled** array changed by appending **twice the value** of every element in original, and then randomly **shuffling** the resulting array.

# Given an array changed, return original *if* changed *is a **doubled** array. If* changed *is not a **doubled** array, return an empty array. The elements in* original *may be returned in **any** order*.

# **Example 1:**

# **Input:** changed = [1,3,4,2,6,8]

# **Output:** [1,3,4]

# **Explanation:** One possible original array could be [1,3,4]:

# - Twice the value of 1 is 1 * 2 = 2.
# - Twice the value of 3 is 3 * 2 = 6.
# - Twice the value of 4 is 4 * 2 = 8.

# Other original arrays could be [4,3,1] or [3,1,4].

# Solution

def find_original(changed):
    counter = {}

    for num in changed:
        if num not in counter:
            counter[num] = 0
        counter[num] += 1

    original = []

    for num in counter:
        if num * 2 not in counter or counter[num] != counter[num * 2]:
            return []

        original += [num] * counter[num]

    return original


# 💡 **Question 7**

# Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

# **Example 1:**
# **Input:** n = 3

# **Output:** [[1,2,3],[8,9,4],[7,6,5]]

#Solution

def generate_matrix(n):
    matrix = [[0] * n for _ in range(n)]
    num = 1
    top, bottom, left, right = 0, n - 1, 0, n - 1

    while num <= n * n:
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1

        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1

        for i in range(right, left - 1, -1):
            matrix[bottom][i] = num
            num += 1
        bottom -= 1

        for i in range(bottom, top - 1, -1):
            matrix[i][left] = num
            num += 1
        left += 1

    return matrix


# 💡 **Question 8**

# Given two [sparse matrices](https://en.wikipedia.org/wiki/Sparse_matrix) mat1 of size m x k and mat2 of size k x n, return the result of mat1 x mat2. You may assume that multiplication is always possible.

# **Example 1:**

def multiply_matrices(mat1, mat2):
    m, k = len(mat1), len(mat1[0])
    n = len(mat2[0])

    result = [[0] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            for x in range(k):
                result[i][j] += mat1[i][x] * mat2[x][j]

    return result





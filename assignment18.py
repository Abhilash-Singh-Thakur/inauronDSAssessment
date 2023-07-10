
# 💡 1. **Merge Intervals**

# Given an array of `intervals` where `intervals[i] = [starti, endi]`, merge all overlapping intervals, and return *an array of the non-overlapping intervals that cover all the intervals in the input*.

# **Example 1:**
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].


def merge(intervals):
    # Sort the intervals based on the start time
    intervals.sort(key=lambda x: x[0])

    # Initialize an empty result list
    result = []

    # Iterate through the sorted intervals
    for interval in intervals:
        # If the result list is empty or the current interval does not overlap with the last interval in the result list
        if not result or interval[0] > result[-1][1]:
            # Add the current interval to the result list
            result.append(interval)
        else:
            # Merge the current interval with the last interval in the result list
            result[-1][1] = max(result[-1][1], interval[1])

    return result


# 💡 2. **Sort Colors**

# Given an array `nums` with `n` objects colored red, white, or blue, sort them **[in-place](https://en.wikipedia.org/wiki/In-place_algorithm)** so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers `0`, `1`, and `2` to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.

# # **Example 1:**

# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]

# Solution
def sortColors(nums):
    n = len(nums)
    low, mid, high = 0, 0, n - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[mid], nums[low] = nums[low], nums[mid]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:  # nums[mid] == 2
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

    return nums

# 💡 3. **First Bad Version Solution**

# You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

# Suppose you have `n` versions `[1, 2, ..., n]` and you want to find out the first bad one, which causes all the following ones to be bad.

# You are given an API `bool isBadVersion(version)` which returns whether `version` is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

# Example 1: Input: n = 5, bad = 4
# Output: 4
# Explanation:
# call isBadVersion(3) -> false
# call isBadVersion(5) -> true
# call isBadVersion(4) -> true
# Then 4 is the first bad version.

def firstBadVersion(n):
    left = 1
    right = n

    while left < right:
💡 8. **132 Pattern**

Given an array of `n` integers `nums`, a **132 pattern** is a subsequence of three integers `nums[i]`, `nums[j]` and `nums[k]` such that `i < j < k` and `nums[i] < nums[k] < nums[j]`.

Return `true` *if there is a **132 pattern** in* `nums`*, otherwise, return* `false`*.*

**Example 1:**
Input: nums = [1,2,3,4]
Output: false
Explanation: There is no 132 pattern in the sequence.
💡 8. **132 Pattern**

Given an array of `n` integers `nums`, a **132 pattern** is a subsequence of three integers `nums[i]`, `nums[j]` and `nums[k]` such that `i < j < k` and `nums[i] < nums[k] < nums[j]`.

Return `true` *if there is a **132 pattern** in* `nums`*, otherwise, return* `false`*.*

**Example 1:**
Input: nums = [1,2,3,4]
Output: false
Explanation: There is no 132 pattern in the sequence.
        mid = left + (right - left) // 2
        if isBadVersion(mid):
            right = mid
        else:
            left = mid + 1

    return left


# 💡 4. **Maximum Gap**

# Given an integer array `nums`, return *the maximum difference between two successive elements in its sorted form*. If the array contains less than two elements, return `0`.

# You must write an algorithm that runs in linear time and uses linear extra space.

# **Example 1:**

# Input: nums = [3,6,9,1]
# Output: 3
# Explanation: The sorted form of the array is [1,3,6,9], either (3,6) or (6,9) has the maximum difference 3.

# Solution

def maximumGap(nums):
    if len(nums) < 2:
        return 0

    max_num = max(nums)
    exp = 1
    n = len(nums)
    buckets = []

    while max_num // exp > 0:
        count = [0] * 10

        for num in nums:
            count[(num // exp) % 10] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        for num in reversed(nums):
            bucket_index = (num // exp) % 10
            buckets[count[bucket_index] - 1] = num
            count[bucket_index] -= 1

        nums = list(buckets)
        exp *= 10

    max_gap = 0

    for i in range(1, n):
        max_gap = max(max_gap, nums[i] - nums[i - 1])

    return max_gap

# 💡 5. **Contains Duplicate**

# Given an integer array `nums`, return `true` if any value appears **at least twice** in the array, and return `false` if every element is distinct.

# **Example 1:**

# Input: nums = [1,2,3,1]
# Output: true

def containsDuplicate(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return True
        seen.add(num)

    return False


# 💡 6. **Minimum Number of Arrows to Burst Balloons**

# There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array `points` where `points[i] = [xstart, xend]` denotes a balloon whose **horizontal diameter** stretches between `xstart` and `xend`. You do not know the exact y-coordinates of the balloons.

# Arrows can be shot up **directly vertically** (in the positive y-direction) from different points along the x-axis. A balloon with `xstart` and `xend` is **burst** by an arrow shot at `x` if `xstart <= x <= xend`. There is **no limit** to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

# Given the array `points`, return *the **minimum** number of arrows that must be shot to burst all balloons*.

# Solution


def findMinArrowShots(points):
    if not points:
        return 0

    points.sort(key=lambda x: x[1])
    arrows = 1
    end = points[0][1]

    for i in range(1, len(points)):
        if points[i][0] > end:
            arrows += 1
            end = points[i][1]
        else:
            end = min(end, points[i][1])

    return arrows


# 💡 7. **Longest Increasing Subsequence**

# Given an integer array `nums`, return *the length of the longest **strictly increasing***

# ***subsequence***

# Example 1: Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

# Solution

def lengthOfLIS(nums):
    n = len(nums)
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

# 💡 8. **132 Pattern**

# Given an array of `n` integers `nums`, a **132 pattern** is a subsequence of three integers `nums[i]`, `nums[j]` and `nums[k]` such that `i < j < k` and `nums[i] < nums[k] < nums[j]`.

# Return `true` *if there is a **132 pattern** in* `nums`*, otherwise, return* `false`*.*

# **Example 1:**
# Input: nums = [1,2,3,4]
# Output: false
# Explanation: There is no 132 pattern in the sequence.


# Solution


def find132pattern(nums):
    stack = []
    s3 = float('-inf')
    n = len(nums)

    for i in range(n - 1, -1, -1):
        num = nums[i]

        if num < s3:
            return True

        while stack and stack[-1] < num:
            s3 = stack.pop()

        stack.append(num)

    return False





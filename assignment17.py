💡 **Question 1**

Given a string `s`, *find the first non-repeating character in it and return its index*. If it does not exist, return `-1`.
Example: Input: s = "leetcode"
Output: 0

# Solution

def firstUniqChar(s):
    char_count = [0] * 26  # array to store the frequency count of each character

    # Update the frequency count of each character
    for char in s:
        char_count[ord(char) - ord('a')] += 1

    # Find the index of the first non-repeating character
    for i, char in enumerate(s):
        if char_count[ord(char) - ord('a')] == 1:
            return i

    return -1  # Return -1 if no non-repeating character is found

# Test the function
s = "leetcode"
print(firstUniqChar(s))  # Output: 0


# 💡 **Question 2**

# Given a **circular integer array** `nums` of length `n`, return *the maximum possible sum of a non-empty **subarray** of* `nums`.

# A **circular array** means the end of the array connects to the beginning of the array. Formally, the next element of `nums[i]` is `nums[(i + 1) % n]` and the previous element of `nums[i]` is `nums[(i - 1 + n) % n]`.

# A **subarray** may only include each element of the fixed buffer `nums` at most once. Formally, for a subarray `nums[i], nums[i + 1], ..., nums[j]`, there does not exist `i <= k1`, `k2 <= j` with `k1 % n == k2 % n`.

# Solution 


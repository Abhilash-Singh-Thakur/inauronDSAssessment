
# 💡 1. **Roman to Integer**

# Roman numerals are represented by seven different symbols: `I`, `V`, `X`, `L`, `C`, `D` and `M`.


# Solution

def roman_to_integer(s):
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    total = 0
    n = len(s)
    i = 0
    
    while i < n:
        if i < n - 1 and roman_values[s[i]] < roman_values[s[i+1]]:
            # Subtraction case
            total += roman_values[s[i+1]] - roman_values[s[i]]
            i += 2
        else:
            # Normal case
            total += roman_values[s[i]]
            i += 1
    
    return total



# 💡 2. **Longest Substring Without Repeating Characters**

# Given a string `s`, find the length of the **longest substring** without repeating characters.

# **Example 1:**
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

def length_of_longest_substring(s):
    start = 0
    end = 0
    max_length = 0
    seen = set()
    
    while end < len(s):
        if s[end] in seen:
            seen.remove(s[start])
            start += 1
        else:
            seen.add(s[end])
            max_length = max(max_length, end - start + 1)
            end += 1
    
    return max_length

# 💡 3. **Majority Element**

# Given an array `nums` of size `n`, return *the majority element*.

# The majority element is the element that appears more than `⌊n / 2⌋` times. You may assume that the majority element always exists in the array.

# **Example 1:**

# Input: nums = [3,2,3]
# Output: 3

# solution
def majority_element(nums):
    majority = nums[0]
    count = 1
    
    for i in range(1, len(nums)):
        if count == 0:
            majority = nums[i]
            count = 1
        elif nums[i] == majority:
            count += 1
        else:
            count -= 1
    
    return majority




# 💡 4. **Group Anagram**

# Given an array of strings `strs`, group **the anagrams** together. You can return the answer in **any order**.

# An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# **Example 1:**

#   Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Solution

def group_anagrams(strs):
    anagram_groups = {}
    
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        
        key = tuple(count)
        if key not in anagram_groups:
            anagram_groups[key] = []
        
        anagram_groups[key].append(s)
    
    return list(anagram_groups.values())


# 💡 5. **Ugly Numbers**

# An **ugly number** is a positive integer whose prime factors are limited to `2`, `3`, and `5`.

# Given an integer `n`, return *the* `nth` ***ugly number***.

# Solution- 
def nth_ugly_number(n):
    ugly = [0] * n
    ugly[0] = 1
    p2 = p3 = p5 = 0
    
    for i in range(1, n):
        next_ugly = min(ugly[p2] * 2, ugly[p3] * 3, ugly[p5] * 5)
        ugly[i] = next_ugly
        
        if next_ugly == ugly[p2] * 2:
            p2 += 1
        if next_ugly == ugly[p3] * 3:
            p3 += 1
        if next_ugly == ugly[p5] * 5:
            p5 += 1
    
    return ugly[n-1]



# 💡 6. **Top K Frequent Words**

# Given an array of strings `words` and an integer `k`, return *the* `k` *most frequent strings*.

# Return the answer **sorted** by **the frequency** from highest to lowest. Sort the words with the same frequency by their **lexicographical order**.

# **Example 1:**

# Input: words = ["i","love","leetcode","i","love","coding"], k = 2
# Output: ["i","love"]
# Explanation: "i" and "love" are the two most frequent words.
# Note that "i" comes before "love" due to a lower alphabetical order.

# Solution
from collections import Counter

def top_k_frequent_words(words, k):
    word_counts = Counter(words)
    unique_words = list(word_counts.keys())
    
    unique_words.sort(key=lambda word: (-word_counts[word], word))
    
    return unique_words[:k]

# 💡 7. **Sliding Window Maximum**

# You are given an array of integers `nums`, there is a sliding window of size `k` which is moving from the very left of the array to the very right. You can only see the `k` numbers in the window. Each time the sliding window moves right by one position.

# Return *the max sliding window*.

# Solution

import heapq

def max_sliding_window(nums, k):
    max_heap = []
    result = []
    
    for i in range(len(nums)):
        while max_heap and max_heap[0][1] <= i - k:
            heapq.heappop(max_heap)
        
        heapq.heappush(max_heap, (-nums[i], i))
        
        if i >= k - 1:
            result.append(-max_heap[0][0])
    
    return result


# 💡 8. **Find K Closest Elements**

# Given a **sorted** integer array `arr`, two integers `k` and `x`, return the `k` closest integers to `x` in the array. The result should also be sorted in ascending order.

# An integer `a` is closer to `x` than an integer `b` if:

# - `|a - x| < |b - x|`, or
# - `|a - x| == |b - x|` and `a < b`

# **Example 1:**

# Input: arr = [1,2,3,4,5], k = 4, x = 3
# Output: [1,2,3,4]



def find_closest_elements(arr, k, x):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            right = mid
            break
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    
    left = right
    right = right + 1
    
    while k > 0:
        if left >= 0 and right < len(arr):
            if x - arr[left] <= arr[right] - x:
                left -= 1
            else:
                right += 1
        elif left < 0:
            right += 1
        elif right >= len(arr):
            left -= 1
        
        k -= 1
    
    return arr[left+1:right]











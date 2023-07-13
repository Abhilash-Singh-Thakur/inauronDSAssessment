# 💡 **Question 1**

# Given two strings s1 and s2, return *the lowest **ASCII** sum of deleted characters to make two strings equal*.

# **Example 1:**

# **Input:** s1 = "sea", s2 = "eat"

# **Output:** 231

# **Explanation:** Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.

# Deleting "t" from "eat" adds 116 to the sum.

# At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.

# Solution

def minimum_delete_sum(s1, s2):
    m, n = len(s1), len(s2)

    # Create a 2D table to store the minimum ASCII sum of deleted characters
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the table starting from the last characters of the strings
    for i in range(m - 1, -1, -1):
        dp[i][n] = dp[i + 1][n] + ord(s1[i])

    for j in range(n - 1, -1, -1):
        dp[m][j] = dp[m][j + 1] + ord(s2[j])

    # Fill the rest of the table by considering the characters of both strings
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if s1[i] == s2[j]:
                dp[i][j] = dp[i + 1][j + 1]
            else:
                dp[i][j] = min(dp[i + 1][j] + ord(s1[i]), dp[i][j + 1] + ord(s2[j]))

    return dp[0][0]


# 💡 **Question 2**

# Given a string s containing only three types of characters: '(', ')' and '*', return true *if* s *is **valid***.

# The following rules define a **valid** string:

# - Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# - Any right parenthesis ')' must have a corresponding left parenthesis '('.
# - Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# - '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".

# **Example 1:**

# **Input:** s = "()"

# **Output:**

# true

# Solution

def is_valid_string(s):
    stack = []
    star_stack = []

    for char in s:
        if char == '(':
            stack.append(char)
        elif char == '*':
            star_stack.append(char)
        else:
            if stack:
                stack.pop()
            elif star_stack:
                star_stack.pop()
            else:
                return False

    while stack and star_stack:
        if stack[-1] > star_stack[-1]:
            return False
        stack.pop()
        star_stack.pop()

    return len(stack) == 0


# 💡 **Question 3**

# Given two strings word1 and word2, return *the minimum number of **steps** required to make* word1 *and* word2 *the same*.

# In one **step**, you can delete exactly one character in either string.

# **Example 1:**

# **Input:** word1 = "sea", word2 = "eat"

# **Output:** 2

# **Explanation:** You need one step to make "sea" to "ea" and another step to make "eat" to "ea".

# Solution

def min_steps_to_same(word1, word2):
    m, n = len(word1), len(word2)

    # Create a 2D table to store the minimum number of steps
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the table starting from the last characters of the strings
    for i in range(m - 1, -1, -1):
        dp[i][n] = dp[i + 1][n] + 1

    for j in range(n - 1, -1, -1):
        dp[m][j] = dp[m][j + 1] + 1

    # Fill the rest of the table by considering the characters of both strings
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if word1[i] == word2[j]:
                dp[i][j] = dp[i + 1][j + 1]
            else:
                dp[i][j] = min(dp[i + 1][j], dp[i][j + 1]) + 1

    return dp[0][0]


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 💡 **Question 4**

# You need to construct a binary tree from a string consisting of parenthesis and integers.

# The whole input represents a binary tree. It contains an integer followed by zero, one or two pairs of parenthesis. The integer represents the root's value and a pair of parenthesis contains a child binary tree with the same structure.
# You always start to construct the **left** child node of the parent first if it exists.

# Solution 

def str_to_tree(s):
    if not s:
        return None

    # Find the first occurrence of '(' to determine the root value
    i = s.find('(')
    if i == -1:
        # No children, so the entire string is the root value
        return TreeNode(int(s))

    # Create a new tree node with the root value
    root = TreeNode(int(s[:i]))

    # Find the positions of the parentheses for the left and right subtrees
    count = 0
    j = i
    while j < len(s):
        if s[j] == '(':
            count += 1
        elif s[j] == ')':
            count -= 1
        if count == 0:
            break
        j += 1

    # Recursively construct the left and right subtrees
    root.left = str_to_tree(s[i+1:j])
    root.right = str_to_tree(s[j+2:-1])

    return root


# 💡 **Question 5**

# Given an array of characters chars, compress it using the following algorithm:

# Begin with an empty string s. For each group of **consecutive repeating characters** in chars:

# - If the group's length is 1, append the character to s.
# - Otherwise, append the character followed by the group's length.

# The compressed string s **should not be returned separately**, but instead, be stored **in the input character array chars**. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

# After you are done **modifying the input array,** return *the new length of the array*.

# You must write an algorithm that uses only constant extra space.

# **Example 1:**

# **Input:** chars = ["a","a","b","b","c","c","c"]

# **Output:** Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]

# **Explanation:**

# The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".

# Solution

def compress(chars):
    if len(chars) <= 1:
        return len(chars)

    anchor = 0  # Start of a group
    write = 0   # Position to write the compressed characters

    for read in range(1, len(chars)):
        if chars[read] != chars[read - 1]:
            chars[write] = chars[anchor]  # Write the character

            if read - anchor > 1:
                count = str(read - anchor)  # Convert group length to string

                for digit in count:
                    write += 1
                    chars[write] = digit  # Write the group length digit

            write += 1
            anchor = read  # Move anchor to the start of the next group

    chars[write] = chars[anchor]  # Write the last character

    if len(chars) - anchor > 1:
        count = str(len(chars) - anchor)  # Convert group length to string

        for digit in count:
            write += 1
            chars[write] = digit  # Write the group length digit

    return write + 1

# 💡 **Question 6**

# Given two strings s and p, return *an array of all the start indices of* p*'s anagrams in* s. You may return the answer in **any order**.

# An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# **Example 1:**

# **Input:** s = "cbaebabacd", p = "abc"

# **Output:** [0,6]

# **Explanation:**

# The substring with start index = 0 is "cba", which is an anagram of "abc".

# The substring with start index = 6 is "bac", which is an anagram of "abc".

# Solution

from collections import Counter

def find_anagrams(s, p):
    result = []
    len_s, len_p = len(s), len(p)
    
    # Convert string p to a character frequency counter
    p_counter = Counter(p)
    
    # Initialize the sliding window counters
    window_counter = Counter(s[:len_p])
    
    # Compare the initial window with the frequency counter of p
    if window_counter == p_counter:
        result.append(0)
    
    # Slide the window through the string s
    for i in range(1, len_s - len_p + 1):
        # Update the sliding window counters
        window_counter[s[i - 1]] -= 1
        if window_counter[s[i - 1]] == 0:
            del window_counter[s[i - 1]]
        window_counter[s[i + len_p - 1]] += 1
        
        # Compare the current window with the frequency counter of p
        if window_counter == p_counter:
            result.append(i)
    
    return result


# 💡 **Question 7**

# Given an encoded string, return its decoded string.

# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

# You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

# The test cases are generated so that the length of the output will never exceed 105.

# **Example 1:**

# **Input:** s = "3[a]2[bc]"

# **Output:** "aaabcbc"

#Solution

def decode_string(s):
    stack = []
    current_string = ''
    current_count = 0

    for char in s:
        if char.isdigit():
            # Update the current count
            current_count = current_count * 10 + int(char)
        elif char == '[':
            # Push the current count and current string to the stack
            stack.append((current_string, current_count))
            current_string = ''
            current_count = 0
        elif char == ']':
            # Retrieve the previous count and string from the stack
            prev_string, prev_count = stack.pop()
            # Multiply the previous string by the current count
            current_string = prev_string + prev_count * current_string
        else:
            # Append the character to the current string
            current_string += char

    return current_string

# 💡 **Question 8**

# Given two strings s and goal, return true *if you can swap two letters in* s *so the result is equal to* goal*, otherwise, return* false*.*

# Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at s[i] and s[j].

# - For example, swapping at indices 0 and 2 in "abcd" results in "cbad".

# **Example 1:**

# **Input:** s = "ab", goal = "ba"

# **Output:** true

# **Explanation:** You can swap s[0] = 'a' and s[1] = 'b' to get "ba", which is equal to goal.

# Solution

def buddy_strings(s, goal):
    if len(s) != len(goal):
        return False

    if s == goal:
        # Check if there are any repeated characters in s
        seen = set()
        for char in s:
            if char in seen:
                return True
            seen.add(char)
        return False

    pairs = []
    for i in range(len(s)):
        if s[i] != goal[i]:
            pairs.append((s[i], goal[i]))
            if len(pairs) > 2:
                return False

    return len(pairs) == 2 and pairs[0] == pairs[1][::-1]

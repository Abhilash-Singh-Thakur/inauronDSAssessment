
# 💡 **Question 1**

# Given two strings s and t, *determine if they are isomorphic*.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

# **Example 1:**

# **Input:** s = "egg", t = "add"

# **Output:** true

# Solution

def is_isomorphic(s, t):
    if len(s) != len(t):
        return False

    char_map = {}
    used_chars = set()

    for i in range(len(s)):
        if s[i] in char_map:
            if char_map[s[i]] != t[i]:
                return False
        else:
            if t[i] in used_chars:
                return False
            char_map[s[i]] = t[i]
            used_chars.add(t[i])

    return True

# 💡 **Question 2**

# Given a string num which represents an integer, return true *if* num *is a **strobogrammatic number***.

# A **strobogrammatic number** is a number that looks the same when rotated 180 degrees (looked at upside down).

# **Example 1:**

# **Input:** num = "69"

# **Output:**

# true

# Solution

def is_strobogrammatic(num):
    strobogrammatic_map = {
        '0': '0',
        '1': '1',
        '6': '9',
        '8': '8',
        '9': '6'
    }

    left, right = 0, len(num) - 1

    while left <= right:
        if num[left] not in strobogrammatic_map or num[right] not in strobogrammatic_map:
            return False

        if num[left] != strobogrammatic_map[num[right]]:
            return False

        left += 1
        right -= 1

    return True



# 💡 **Question 3**

# Given two non-negative integers, num1 and num2 represented as string, return *the sum of* num1 *and* num2 *as a string*.

# You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

# **Example 1:**

# **Input:** num1 = "11", num2 = "123"

# **Output:**

# "134"


def is_strobogrammatic(num):
    strobogrammatic_map = {
        '0': '0',
        '1': '1',
        '6': '9',
        '8': '8',
        '9': '6'
    }

    left, right = 0, len(num) - 1

    while left <= right:
        if num[left] not in strobogrammatic_map or num[right] not in strobogrammatic_map:
            return False

        if num[left] != strobogrammatic_map[num[right]]:
            return False

        left += 1
        right -= 1

    return True



# 💡 **Question 4**

# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

# **Example 1:**

# **Input:** s = "Let's take LeetCode contest"

# **Output:** "s'teL ekat edoCteeL tsetnoc"

# Solution

def reverse_words(s):
    words = s.split()  # Split the sentence into words
    reversed_words = [word[::-1] for word in words]  # Reverse each word
    return ' '.join(reversed_words)  # Join the reversed words with whitespace


# 💡 **Question 5**

# Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.

# If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and leave the other as original.

# **Example 1:**

# **Input:** s = "abcdefg", k = 2

# **Output:**

# "bacdfeg"

# Solution

def reverse_str(s, k):
    result = []
    for i in range(0, len(s), 2 * k):
        segment = s[i:i+k]  # Extract the segment of length k
        reversed_segment = segment[::-1]  # Reverse the segment
        result.append(reversed_segment + s[i+k:i+2*k])  # Add the reversed segment and the remaining characters
    return ''.join(result)  # Join the segments to form the final string


# 💡 **Question 6**

# Given two strings s and goal, return true *if and only if* s *can become* goal *after some number of **shifts** on* s.

# A **shift** on s consists of moving the leftmost character of s to the rightmost position.

# - For example, if s = "abcde", then it will be "bcdea" after one shift.

# **Example 1:**

# **Input:** s = "abcde", goal = "cdeab"

# **Output:**

# true

# Solution

def can_shift_to_goal(s, goal):
    if len(s) != len(goal):
        return False

    if s == goal:
        return True

    for _ in range(len(s)):
        s = s[1:] + s[0]  # Perform a shift on s
        if s == goal:
            return True

    return False


# 💡 **Question 7**

# Given two strings s and t, return true *if they are equal when both are typed into empty text editors*. '#' means a backspace character.

# Note that after backspacing an empty text, the text will continue empty.

# **Example 1:**

# **Input:** s = "ab#c", t = "ad#c"

# **Output:** true

# **Explanation:**

# Both s and t become "ac".

# Solution

def backspace_compare(s, t):
    def process_string(string):
        result = []
        for char in string:
            if char != '#':
                result.append(char)
            elif result:
                result.pop()
        return ''.join(result)

    return process_string(s) == process_string(t)

# 💡 **Question 8**

# You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

# **Input:** coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]

# **Output:** true

# Solution

def check_straight_line(coordinates):
    x0, y0 = coordinates[0]
    x1, y1 = coordinates[1]

    for i in range(2, len(coordinates)):
        x, y = coordinates[i]
        if (y1 - y0) * (x - x0) != (y - y0) * (x1 - x0):
            return False

    return True


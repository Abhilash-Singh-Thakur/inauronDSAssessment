# Question 1
# Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2),..., (an, bn) such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum. Example 1:
# Input: nums = [1,4,3,2]
# Output: 4

# Solution

def arrayPairSum(nums):
    nums.sort()  # Sort the array in ascending order
    result = 0
    for i in range(0, len(nums), 2):
        result += nums[i]
    return result

# Test the implementation with the provided example
nums = [1, 4, 3, 2]
max_sum = arrayPairSum(nums)
print(max_sum)  # Output: 4

# Question 2
# Alice has n candies, where the ith candy is of type candyType[i]. Alice noticed that she started to gain weight, so she visited a doctor. 

# The doctor advised Alice to only eat n / 2 of the candies she has (n is always even). Alice likes her candies very much, and she wants to eat the maximum number of different types of candies while still following the doctor's advice. 

# Given the integer array candyType of length n, return the maximum number of different types of candies she can eat if she only eats n / 2 of them.

# Example 1:
# Input: candyType = [1,1,2,2,3,3]
# Output: 3

def maxCandies(candyType):
    unique_candies = set(candyType)  # Get the unique candy types using a set
    max_candies = len(unique_candies)  # Count the number of unique candy types
    max_limit = len(candyType) // 2  # Calculate the maximum limit of candies Alice can eat
    
    return min(max_candies, max_limit)  # Return the minimum of the two limits

# Test the implementation with the provided example
candyType = [1, 1, 2, 2, 3, 3]
max_types = maxCandies(candyType)
print(max_types)  # Output: 3

# Question 3
# We define a harmonious array as an array where the difference between its maximum value
# and its minimum value is exactly 1.

# Given an integer array nums, return the length of its longest harmonious subsequence
# among all its possible subsequences.

# A subsequence of an array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.

# Example 1:
# Input: nums = [1,3,2,2,5,2,3,7]
# Output: 5

# Solution

def findLHS(nums):
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    longest_subsequence = 0
    for num in freq:
        if num + 1 in freq:
            longest_subsequence = max(longest_subsequence, freq[num] + freq[num + 1])

    return longest_subsequence

# Test the implementation with the provided example
nums = [1, 3, 2, 2, 5, 2, 3, 7]
longest_subseq = findLHS(nums)
print(longest_subseq)  # Output: 5


# Question 4
# You have a long flowerbed in which some of the plots are planted, and some are not.
# However, flowers cannot be planted in adjacent plots.
# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

# Example 1:
# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true

# Solution

def canPlaceFlowers(flowerbed, n):
    i = 0
    count = 0
    while i < len(flowerbed):
        if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
            flowerbed[i] = 1
            count += 1
        i += 1

    return count >= n

# Test the implementation with the provided example
flowerbed = [1, 0, 0, 0, 1]
n = 1
result = canPlaceFlowers(flowerbed, n)
print(result)  # Output: True


# Question 5
# Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

# Example 1:
# Input: nums = [1,2,3]
# Output: 6

def maximumProduct(nums):
    min1 = float('inf')
    min2 = float('inf')
    max1 = float('-inf')
    max2 = float('-inf')
    max3 = float('-inf')
    
    for num in nums:
        if num <= min1:
            min2 = min1
            min1 = num
        elif num <= min2:
            min2 = num
        
        if num >= max1:
            max3 = max2
            max2 = max1
            max1 = num
        elif num >= max2:
            max3 = max2
            max2 = num
        elif num >= max3:
            max3 = num
    
    return max(min1 * min2 * max1, max1 * max2 * max3)

# Test the implementation with the provided example
nums = [1, 2, 3]
result = maximumProduct(nums)
print(result)  # Output: 6


# Question 6
# Given an array of integers nums which is sorted in ascending order, and an integer target,
# write a function to search target in nums. If target exists, then return its index. Otherwise,
# return -1.

# You must write an algorithm with O(log n) runtime complexity.

# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4

# Explanation: 9 exists in nums and its index is 4

# Solution

def search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# Test the implementation with the provided example
nums = [-1, 0, 3, 5, 9, 12]
target = 9
result = search(nums, target)
print(result)  # Output: 4

# Question 7
# An array is monotonic if it is either monotone increasing or monotone decreasing.

# An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is
# monotone decreasing if for all i <= j, nums[i] >= nums[j].

# Given an integer array nums, return true if the given array is monotonic, or false otherwise.

# Example 1:
# Input: nums = [1,2,2,3]
# Output: true

# Solution

def isMonotonic(nums):
    increasing = decreasing = True

    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            increasing = False
        if nums[i] > nums[i - 1]:
            decreasing = False

    return increasing or decreasing

# Test the implementation with the provided example
nums = [1, 2, 2, 3]
result = isMonotonic(nums)
print(result)  # Output: True


# Question 8
# You are given an integer array nums and an integer k.

# In one operation, you can choose any index i where 0 <= i < nums.length and change nums[i] to nums[i] + x where x is an integer from the range [-k, k]. You can apply this operation at most once for each index i.

# The score of nums is the difference between the maximum and minimum elements in nums.

# Return the minimum score of nums after applying the mentioned operation at most once for each index in it.

# Example 1:
# Input: nums = [1], k = 0
# Output: 0


def minimumScore(nums, k):
    nums.sort()  # Sort the array in ascending order
    min_score = nums[-1] - nums[0]  # Initialize min_score with the maximum difference

    # Iterate from the second element to the second-to-last element
    for i in range(1, len(nums) - 1):
        # Calculate the potential minimum and maximum values after applying the operation
        potential_min = min(nums[0] + k, nums[i] - k)
        potential_max = max(nums[-1] - k, nums[i] + k)
        
        # Calculate the potential score
        potential_score = potential_max - potential_min
        
        # Update min_score if the potential score is smaller
        min_score = min(min_score, potential_score)

    return min_score

# Test the implementation with the provided example
nums = [1]
k = 0
result = minimumScore(nums, k)
print(result)  # Output: 0




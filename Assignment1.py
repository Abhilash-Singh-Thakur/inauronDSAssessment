# Solution 1. 

def twoSum(nums, target):
    # Create a dictionary to store the complement of each number and its index
    complement_map = {}

    # Iterate through the array
    for i, num in enumerate(nums):
        # Check if the complement of the current number exists in the dictionary
        complement = target - num
        if complement in complement_map:
            # Return the indices of the two numbers
            return [complement_map[complement], i]
        else:
            # Add the current number and its index to the dictionary
            complement_map[num] = i

    # If no solution is found, return an empty list
    return []

# Example usage
nums = [2, 7, 11, 15]
target = 9
result = twoSum(nums, target)
print(result)  # Output: [0, 1]

# Solution 2


def removeElement(nums, val):
    # Initialize two pointers
    i = 0  # Pointer for iterating through the array
    k = 0  # Pointer for storing elements not equal to val

    # Iterate through the array
    while i < len(nums):
        if nums[i] != val:
            # If the current element is not equal to val,
            # move it to the k-th position and increment k
            nums[k] = nums[i]
            k += 1
        i += 1

    # Return the count of elements not equal to val
    return k

# Example usage
nums = [3, 2, 2, 3]
val = 3
result = removeElement(nums, val)
print(result)  # Output: 2
print(nums)    # Output: [2, 2, 2, 3]


# solution 3


def searchInsert(nums, target):
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

    # If the target is not found, return the index where it would be inserted
    return left

# Example usage
nums = [1, 3, 5, 6]
target = 5
result = searchInsert(nums, target)
print(result)  # Output: 2


# Solution 4

def plusOne(digits):
    n = len(digits)
    # Start from the rightmost digit
    for i in range(n - 1, -1, -1):
        if digits[i] < 9:
            # If the digit is less than 9, simply increment it by one
            digits[i] += 1
            return digits
        else:
            # If the digit is 9, set it to 0 and move to the next digit
            digits[i] = 0

    # If all digits become 10, insert 1 at the most significant position
    return [1] + digits

# Example usage
digits = [1, 2, 3]
result = plusOne(digits)
print(result)  # Output: [1, 2, 4]


# Solution 5

def merge(nums1, m, nums2, n):
    # Initialize pointers for nums1, nums2, and the merged array
    i = m - 1
    j = n - 1
    k = m + n - 1

    # Merge the arrays in reverse order
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

    # Copy any remaining elements from nums2 to nums1
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1
        
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

merge(nums1, m, nums2, n)
print(nums1)  # Output: [1, 2, 2, 3, 5, 6

# Solution 6


def containsDuplicate(nums):
    num_set = set()

    for num in nums:
        if num in num_set:
            return True
        else:
            num_set.add(num)

    return False

nums = [1, 2, 3, 4, 5]
result = containsDuplicate(nums)
print(result)  # Output: False

nums = [1, 2, 3, 2, 5]
result = containsDuplicate(nums)
print(result)  # Output: True


# Solution 7

def moveZeroes(nums):
    # Initialize a pointer to track the position for non-zero elements
    non_zero_pos = 0

    # Iterate through the array
    for i in range(len(nums)):
        if nums[i] != 0:
            # If the current element is non-zero, swap it with the element at non_zero_pos
            nums[i], nums[non_zero_pos] = nums[non_zero_pos], nums[i]
            non_zero_pos += 1
            
nums = [0, 1, 0, 3, 12]
moveZeroes(nums)
print(nums)  # Output: [1, 3, 12, 0, 0]

# Solution 8

def findErrorNums(nums):
    num_set = set()
    duplicate, missing = None, None

    for num in nums:
        if num in num_set:
            duplicate = num
        num_set.add(num)

    n = len(nums)
    for i in range(1, n + 1):
        if i not in num_set:
            missing = i
            break

    return [duplicate, missing]
  
  
# Solution 8 

def findErrorNums(nums):
    num_set = set()
    duplicate, missing = None, None

    for num in nums:
        if num in num_set:
            duplicate = num
        num_set.add(num)

    n = len(nums)
    for i in range(1, n + 1):
        if i not in num_set:
            missing = i
            break

    return [duplicate, missing]



nums = [1, 2, 2, 4]  # Example input array
result = findErrorNums(nums)
print("Duplicate number:", result[0])
print("Missing number:", result[1])






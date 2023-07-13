
# 💡 **Question 1**
# Given three integer arrays arr1, arr2 and arr3 **sorted** in **strictly increasing** order, return a sorted array of **only** the integers that appeared in **all** three arrays.

# **Example 1:**

# Input: arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]

# Output: [1,5]

# **Explanation:** Only 1 and 5 appeared in the three arrays.

# Solution 

def commonElements(arr1, arr2, arr3):
    set1 = set(arr1)
    set2 = set(arr2)
    set3 = set(arr3)
    
    common = set1.intersection(set2, set3)
    
    return sorted(list(common))

# Test the implementation with the provided example
arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 2, 5, 7, 9]
arr3 = [1, 3, 4, 5, 8]
result = commonElements(arr1, arr2, arr3)
print(result)  # Output: [1, 5]






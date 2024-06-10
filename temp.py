def two_sum(nums, target):
    num_to_index = {}
    for i, num in enumerate(nums):
        complement = target - num
        
        if complement in num_to_index:
           
            return [num_to_index[complement], i]
        
        num_to_index[num] = i

# Test Case 1
nums1 = [2, 7, 11, 15]
target1 = 9
print(two_sum(nums1, target1))

# Test Case 2
nums2 = [3, 2, 4]
target2 = 6
print(two_sum(nums2, target2))  
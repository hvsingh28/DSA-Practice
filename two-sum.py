'''QUESTION - Given an array of integers nums and an integer target, 
   return the indices of the two numbers such that they add up to target.
   NOTE - only unique elements are present and only one possible pair'''

def two_sum(nums, target):
    for i in range(len(nums)):
        find = target - nums[i]
        if find in nums and nums.index(find) != i:
            return (i, nums.index(find))

nums = [1, 2, 3, 4, 5, 6, 8]
target = 6
a, b = two_sum(nums, target)    
print(a, b)

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        increasing_order = True
        decreasing_order = True

        
        for i in range(1, len(nums)):

            if nums[i] > nums[i-1]:
                decreasing_order = False

            if nums[i] < nums[i-1]:

                increasing_order = False

        return increasing_order or decreasing_order

'''
Example 1:

Input: nums = [1,2,2,3]
Output: true
Example 2:

Input: nums = [6,5,4,4]
Output: true
Example 3:

Input: nums = [1,3,2]
Output: false
 



'''

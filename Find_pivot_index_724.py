class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        sumNum = sum(nums)
        for i in range(len(nums)):
            if left == sumNum - left - nums[i]:
                return i
            left += nums[i]
        return -1

     

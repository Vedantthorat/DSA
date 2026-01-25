class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # selection sort
        for i in range(len(nums)):
            min_idx = i
            for j in range(i, len(nums)):
                if nums[j] < nums[min_idx]:
                    nums[j], nums[min_idx] = nums[min_idx], nums[j]

    

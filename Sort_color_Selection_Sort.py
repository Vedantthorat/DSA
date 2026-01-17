class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # selection sort

        n = len(nums)
        for i in range(n):
            min_idx = i
            for j in range(i, n):
                if nums[j] < nums[min_idx]:
                    nums[j], nums[min_idx] = nums[min_idx], nums[j]

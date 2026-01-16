class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sumNum = 0
        res = []
        for i in range(len(nums)):
            sumNum += nums[i]
            res.append(sumNum)
        return res

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def backtrack(start):
            if start == len(nums):
                res.append(nums[:])
                return
            seen = set()
            for i in range(start, len(nums)):
                if nums[i] in seen:
                    continue
                seen.add(nums[i])

                nums[i], nums[start] = nums[start], nums[i]
                backtrack(start+1)
                nums[i], nums[start] = nums[start], nums[i]
        backtrack(0)
        return res


'''  
Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 


'''

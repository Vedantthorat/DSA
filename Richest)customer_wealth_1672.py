class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_ele = 0
        res = []
        for i in accounts:
            max_ele = max(max_ele, i)
            res += max_ele
        return res

  # or
  return max(map(sum, accounts))

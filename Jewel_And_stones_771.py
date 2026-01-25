class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_count = 0
        for i in stones:
            if i in jewels:
                jewel_count += 1
        return jewel_count      

''' 
Example 1:

Input: jewels = "aA", stones = "aAAbbbb"
Output: 3
Example 2:

Input: jewels = "z", stones = "ZZ"
Output: 0
'''

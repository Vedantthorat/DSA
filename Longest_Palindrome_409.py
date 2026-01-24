class Solution:
    def longestPalindrome(self, s: str) -> int:
        dict = {}
        count = 0
        odd_count = False
        for i in s:
            dict[i] = dict.get(i,0) +1
        for i in dict.values():
            if  i % 2 == 0:
                count += i
            else:
                count += i-1
                odd_count = True
        if odd_count:
            count += 1
        return count
                

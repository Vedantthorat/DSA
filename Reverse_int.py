class Solution:
    def reverse(self, x: int) -> int:
        max_scale = 2** 31 - 1
        min_scale = -2** 31
        if x <  0:
            sign = -1
        else:
            sign = 1

        x = abs(x)

        x = int(str(x)[::-1])
        res = x*sign
        return res if res >= min_scale and res <= max_scale else 0


'''
Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 

'''

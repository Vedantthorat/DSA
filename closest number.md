class Solution:
    def closestNumber(self, n, m):
        lower = (n // m) * m
        upper = lower + m
        
        low = abs(n - lower)
        upp = abs(n - upper)
        
        if low < upp:
            return lower      # ✅ was: return low (wrong — returns distance, not the number)
        elif upp < low:
            return upper      # ✅ was: return upp (wrong — same bug)
        else:
            return lower if abs(lower) >= abs(upper) else upper

      '''
      Problem Statement
Given two integers n and m (m != 0). Find the number closest to n that is divisible by m. If there are two such numbers equidistant from n, return the one with the maximum absolute value.

Function Signature
pythondef closestNumber(self, n: int, m: int) -> int:

Sample Test Cases
nmOutputReason1341212 and 16 are nearest; 12 is closer-156-18-12 and -18 are equidistant; |-18| > |-12|0500 is already divisible by 510101010 is already divisible by 107-36nearest multiple of -3 to 7 is 6-73-6-6 and -9 are equidistant; |-9| > |-6|... wait, -9 → output -9

Constraints
-10^5 <= n, m <= 10^5
m != 0

Input / Output Format
Input:  n = 13, m = 4
Output: 12

Input:  n = -15, m = 6
Output: -18

      Link L https://www.geeksforgeeks.org/batch/dsa-step-by-step-learning/track/easy-maths-dsa-360/problem/closest-number5728

      


      '''

class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        
        return sorted([s1[0], s1[2]]) == sorted([s2[0],s2[2]]) and \
               sorted([s1[1], s1[3]]) == sorted([s2[1], s2[3]])
# or 
        return sorted(s1[0::2]) == sorted(s2[0::2]) and \
                sorted(s1[1::2]) == sorted(s2[1::2])


  '''
Example 1:

Input: s1 = "abcd", s2 = "cdab"
Output: true
Explanation: We can do the following operations on s1:
- Choose the indices i = 0, j = 2. The resulting string is s1 = "cbad".
- Choose the indices i = 1, j = 3. The resulting string is s1 = "cdab" = s2.
Example 2:

Input: s1 = "abcd", s2 = "dacb"
Output: false
Explanation: It is not possible to make the two strings equal.

  '''

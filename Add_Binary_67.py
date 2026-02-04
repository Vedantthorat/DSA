class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        return bin(int(a,2) + int(b,2)) [2:]


''' 
67. Add Binary
Solved
Easy
Topics
premium lock icon
Companies
Given two binary strings a and b, return their sum as a binary string.

 

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself


Explanation

Step-by-step explanation
1. int(a, 2)

Converts binary string → decimal integer

Example:

a = "101"
int("101", 2) = 5


Because:

1×2² + 0×2¹ + 1×2⁰
= 4 + 0 + 1
= 5


Same for b.

2. Add integers
int(a, 2) + int(b, 2)


Normal decimal addition happens.

Example:

5 + 3 = 8

3. bin(number)

Converts decimal → binary string

bin(8) = "0b1000"


Python adds "0b" prefix to indicate binary.

4. [2:]

Removes "0b"

"0b1000"[2:] = "1000"


Final result → binary sum string

Complexity

Conversion takes O(n)

Overall: O(n)


''''





class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        cnt = 0
        s = set(word)

        for i in range(26):
            upper = chr(ord('a')+ i)
            lower = chr(ord('A') + i)

            if upper in s and lower in s:
                cnt += 1

        return cnt


'''
Example 1:

Input: word = "aaAbcBC"

Output: 3

Explanation:

The special characters in word are 'a', 'b', and 'c'.

Example 2:

Input: word = "abc"

Output: 0

Explanation:

No character in word appears in uppercase.

Example 3:

Input: word = "abBCab"

Output: 1

Explanation:

The only special character in word is 'b'.

'''

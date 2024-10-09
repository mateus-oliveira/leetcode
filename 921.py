"""
My solution to the 921 LeetCode's problem, a challenge from 9th October 2024.

Runtime: 27 ms
Allocated memory: 16.55 MB
Complexity: O(n)

https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/description/
"""

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        missing_open = 0
        missing_close = 0
        for c in s:
            if c == '(':
                missing_close += 1
            elif missing_close > 0:
                missing_close -= 1
            else:
                missing_open += 1

        return missing_open + missing_close

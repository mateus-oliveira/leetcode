"""
My solution to the 6 LeetCode's problem in Python.

Runtime: 42 ms
Allocated memory: 16.80 MB
Complexity: O(n)

https://leetcode.com/problems/zigzag-conversion/description/
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        zigzag_strings = ['']*numRows
        
        row = -1
        up = False
        for c in s:
            row += -1 if up else 1
            zigzag_strings[row] += c
            if not up and row >= numRows-1:
                up = True
            elif up and row <= 0:
                up = False

        return ''.join(zigzag_strings)

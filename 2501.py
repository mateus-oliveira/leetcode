"""
My solution to the 2501 LeetCode's problem, a challenge from 28th October 2024.

Runtime: 107 ms
Allocated memory: 37.8 MB
Complexity: O(n log n)

https://leetcode.com/problems/longest-square-streak-in-an-array/description//
"""

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        """
        nums = [4, 3, 6, 16, 8, 2]

        sub1 = [2, 4, 16]
        sub2 = [3] - 3x3 = 9
        sub3 = [6] - 6x6 = 36
        sub4 = [8] - 8x8 = 64

        nums.sort()
        nums = [2, 3, 4, 6, 8, 16]

        num[0] == 2
        2x2 = 4 in set_nums ? YES
        4x4 = 16 in set_nums ? YES
        16x16 = 256 in set_nums ? NO
        """
        nums.sort()
        set_nums = set(nums)
        checked = set()
        result = 0

        for x in nums:
            if x in checked:
                continue
            
            x_squares = 1
            checked.add(x)

            xx = x**2 # x^2
            while xx in set_nums:
                checked.add(xx)
                x_squares += 1
                xx *= xx # xx * xx = xx^2

            if x_squares > result:
                result = x_squares
        
        return result if result > 1 else -1
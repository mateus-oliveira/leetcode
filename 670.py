"""
My solution to the 670. Maximum Swap LeetCode's problem, a challenge from 17th October 2024.

Runtime: ≈ 0 ms
Allocated memory: 16.63 MB
Complexity: O(n log n)
Difficulty: Medium

https://leetcode.com/problems/maximum-swap/description/
"""

from typing import List

class Solution:
    def maximumSwap(self, num: int) -> int:
        if num <= 1:
            return num

        nums = [int(s) for s in str(num)]
        nums_sorted = sorted(nums, reverse=True)

        if nums_sorted == nums:
            return num

        s = str(num)
        for i, n in enumerate(nums_sorted):
            if str(n) == nums[i]:
                continue
            
            if n > nums[i]:
                gt_pos = self.right_index(nums, n)
                lower = nums[i]
                s = s[:i] + str(n) + s[i + 1:]
                s = s[:gt_pos] + str(lower) + s[gt_pos + 1:]
                break

        return int(s)
    
    def right_index(self, lst: List[int], value: int) -> int:
        i = lst[::-1].index(value)
        return len(lst) - i - 1

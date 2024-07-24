"""
My solution to the 1636 LeetCode's problem, a challenge from 23rd July 2024.

Runtime: 52 ms
Allocated memory: 16,7 MB
Complexity: O(n log n)

https://leetcode.com/problems/sort-array-by-increasing-frequency/description/
"""

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        frequence = {}
        counted = {}
        for n in nums:
            if n not in frequence:
                frequence[n] = 1
            else:
                frequence[n] += 1

        for n, v in frequence.items():
            if v not in counted:
                counted[v] = []
            counted[v].append(n)

        result = []
        for n in sorted(counted):
            for i in sorted(counted[n], reverse=True):
                result += [i]*n
        return result


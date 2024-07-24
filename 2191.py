"""
My solution to the 2191 LeetCode's problem, a challenge from 24th July 2024.

Runtime: 1131 ms
Allocated memory: 30.9 MB
Complexity: O(n log n)

https://leetcode.com/problems/sort-the-jumbled-numbers/description/
"""

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        """
        - Example 1
                  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        mapping = [8, 9, 4, 0, 2, 1, 3, 5, 7, 6]
        nums = [991, 338, 38]
        nums_mapped = [669, 007, 07]
        sorted(nums_mapped) # [007, 07, 669]
        sorted(nums) # [338, 38, 991]

        - Example 2
                  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        mapping = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        nums = [789, 456, 123]
        nums_mapped = [789, 456, 123]
        sorted(nums_mapped) # [123, 456, 789]
        sorted(nums) # [123, 456, 789]
        """

        decoded_mapping = {str(n): m for n, m in enumerate(mapping)}

        decoded_nums = []
        for i, n in enumerate(nums):
            num = ''
            for digit in str(n):
                num += '%d' % decoded_mapping[digit]
            decoded_nums.append({
                'val': n,
                'index': i,
                'mapped_val': int(num),
            })

        return [d['val'] for d in sorted(decoded_nums, key=lambda k:(k['mapped_val'], k['index']))]

"""
My solution to the 1395 LeetCode's problem, a challenge from 29th July 2024.

Runtime: 487 ms
Allocated memory: 16.5 MB
Complexity: O(n²)

https://leetcode.com/problems/count-number-of-teams/description/
"""

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        rating_len = len(rating)
        count = 0

        for j in range(1, rating_len-1):
            left_less = 0
            left_greater = 0
            for i in range(j):
                if rating[i] < rating[j]:
                    left_less += 1
                elif rating[i] > rating[j]:
                    left_greater += 1

            right_less = 0
            right_greater = 0
            for k in range(j+1, rating_len):
                if rating[k] < rating[j]:
                    right_less += 1
                elif rating[k] > rating[j]:
                    right_greater += 1

            count += left_less * right_greater + left_greater * right_less

        return count

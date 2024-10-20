from math import ceil
from typing import List

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        score = 0

        if len(nums) == 1:
            for _ in range(k):
                score += nums[0]
                nums[0] = ceil(nums[0]/3)
            return score

        nums.sort()
        i = len(nums)-1
        last = i
        for _ in range(k):
            score += nums[i]
            nums[i] = ceil(nums[i]/3)
            i = 0 if i == 0 else i-1
            if nums[i] < nums[last]:
                i = len(nums)-1
                last = i
                nums.sort()

        return score

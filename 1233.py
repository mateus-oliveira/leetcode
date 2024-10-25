"""
My solution to the 1233 LeetCode's problem, a challenge from 25th October 2024.

Runtime: 20 ms
Allocated memory: 29.5 MB
Complexity: O(n log n)

https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/description/
"""

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        folders = [folder[0]]
        for f in folder:
            if f == folders[-1] or f.startswith(f'{folders[-1]}/'):
                continue
            folders.append(f)
        return folders

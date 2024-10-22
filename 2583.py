# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        levels = {}
        self.sum_node_to_level(root, 1, levels)
        if k not in levels:
            return -1
        return sorted(levels.values())[-k]

    def sum_node_to_level(self, node: TreeNode, level: int, levels: dict):
        if level not in levels:
            levels[level] = 0
        levels[level] += node.val
        if node.left:
            self.sum_node_to_level(node.left, level+1, levels)
        if node.right:
            self.sum_node_to_level(node.right, level+1, levels)

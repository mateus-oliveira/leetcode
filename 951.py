"""
My solution to the 951 LeetCode's problem, a challenge from 24th October 2024.

Runtime: 0 ms
Allocated memory: 16.6 MB
Complexity: O(n)

https://leetcode.com/problems/flip-equivalent-binary-trees/description/
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return True

        if not all([root1, root2]):
            return False

        if root1.val != root2.val:
            return False

        return self.check_nodes(root1, root2)

    def check_nodes(self, node1: TreeNode, node2: TreeNode) -> bool:
        nodes = {}
        if node1.left:
            nodes[node1.left.val] = [node1.left]
        if node1.right:
            nodes[node1.right.val] = [node1.right]
        
        if node2.left:
            if node2.left.val not in nodes:
                return False
            nodes[node2.left.val].append(node2.left)
        if node2.right:
            if node2.right.val not in nodes:
                return False
            nodes[node2.right.val].append(node2.right)
        
        result = True
        for _nodes in nodes.values():
            if len(_nodes) != 2:
                return False
            result &= self.check_nodes(_nodes[0], _nodes[1])

        return result

#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def recursive(p: Optional[TreeNode], q: Optional[TreeNode]) -> int:
            if p or q:
                if p:
                    leftDepth = recursive(p.left, p.right)
                else: 
                    leftDepth = math.inf
                if q:
                    rightDepth = recursive(q.left, q.right)
                else:
                    rightDepth = math.inf

                if leftDepth <= rightDepth:
                    return 1 + leftDepth
                else:
                    return 1 + rightDepth
            else:
                return 1
        if root:
            return recursive(root.left, root.right)
        else:
            return 0
# @lc code=end


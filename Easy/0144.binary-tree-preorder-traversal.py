#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def recursive(root: Optional[TreeNode], pt: List[int]) -> List[int]:
            if root:
                pt.append(root.val)
                recursive(root.left, pt)
                recursive(root.right, pt)
                return pt
        
        pt = []
        if root:
            return recursive(root, pt)
        return []
        
# @lc code=end


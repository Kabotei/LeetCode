#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def recursive(root: Optional[TreeNode], pt: List[int]) -> List[int]:
            if root:
                recursive(root.left, pt)
                recursive(root.right, pt)
                pt.append(root.val)
                return pt
        
        pt = []
        if root:
            return recursive(root, pt)
        return []
        
# @lc code=end


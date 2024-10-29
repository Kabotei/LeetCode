#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def recursive(root: Optional[TreeNode], targetSum: int, sum: int) -> bool:
            if root:
                sum+=root.val
            if root and root.left and root.right:
                leftRoot = root.left
                rightRoot = root.right
                return recursive(leftRoot, targetSum, sum) or recursive(rightRoot, targetSum, sum)
            elif root and root.left:
                leftRoot = root.left
                return recursive(leftRoot, targetSum, sum)
            elif root and root.right:
                rightRoot = root.right
                return recursive(rightRoot, targetSum, sum)
            else:
                return sum == targetSum
        
        if root:
            return recursive(root, targetSum, 0)
        else:
            return False
                
        
# @lc code=end


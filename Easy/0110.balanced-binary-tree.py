#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def getHeight(root: Optional[TreeNode]) -> int:
            if root:
                return max(getHeight(root.left), getHeight(root.right)) + 1
            else:
                return 0
        
        def recursive(root: Optional[TreeNode]) -> bool:
            if root:
                leftHeight = getHeight(root.left)
                rightHeight = getHeight(root.right)

                return (
                    abs(leftHeight - rightHeight) <= 1 
                    and recursive(root.left)
                    and recursive(root.right)
                )
            else:
                return True
        
        return recursive(root)
            

        
# @lc code=end


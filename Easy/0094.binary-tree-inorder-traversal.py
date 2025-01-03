#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def concatenateList(l1,l2,l3):
            return [*l1, *l2, *l3]

        def recursive(root: Optional[TreeNode]) -> List[int]:
            if root:
                l1 = recursive(root.left)
                l2 = [root.val]
                l3 = recursive(root.right)

                return concatenateList(l1,l2,l3)
            else:
                return []
        
        return recursive(root)
        
# @lc code=end


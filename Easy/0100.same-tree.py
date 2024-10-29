#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def recursive(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if p:
                if q:
                    if p.val == q.val:
                        return recursive(p.left,q.left) and recursive(p.right,q.right)
                    else:
                        return False
                else:
                    return False
            else:
                if q:
                    return False
                else:
                    return True
        
        return recursive(p,q)
# @lc code=end


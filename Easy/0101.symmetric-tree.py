#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def recursive(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if p:
                if q:
                    if p.val == q.val:
                        return recursive(p.left,q.right) and recursive(p.right,q.left)
                    else:
                        return False
                else:
                    return False
            else:
                if q:
                    return False
                else:
                    return True
        
        p = root.left
        q = root.right
        return recursive(p,q)
# @lc code=end


#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def getMedianInd(nums: List[int]) -> int:
            return len(nums)//2
        
        def recursive(nums: List[int]) -> Optional[TreeNode]:
            if len(nums) == 0:
                return None
            elif len(nums) == 1:
                return TreeNode(nums[0])
            else:
                medianInd = getMedianInd(nums)
                val = nums[medianInd]
                left = nums[0:medianInd]
                right = nums[medianInd+1::]
                return TreeNode(
                    val=val,
                    left=recursive(left),
                    right=recursive(right)
                )
        
        return recursive(nums)

        
        
# @lc code=end


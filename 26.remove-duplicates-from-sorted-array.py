#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        iToRemove = []

        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                iToRemove.append(i)
        
        for ind in iToRemove[::-1]:
            nums.pop(ind)
        
        k = len(nums)
        return k
# @lc code=end
#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
import math
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        nums.append(math.inf)
        for i in range(0,len(nums),2):
            if nums[i] != nums[i+1]:
                return nums[i]
        


        
# @lc code=end


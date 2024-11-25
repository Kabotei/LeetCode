#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            val1 = nums[i]
            nums2 = nums[i+1:i+1+k]
            if val1 in nums2:
                return True
        return False
        

        
# @lc code=end


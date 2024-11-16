#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    # Boyer–Moore majority vote algorithm
    def majorityElement(self, nums: List[int]) -> int:
        m = -1
        c = 0
        n = len(nums)

        for i in range (n):
            if (c == 0):
                m = nums[i]
                c = 1
            else:
                if (nums[i] == m):
                    c += 1
                else:
                    c -= 1
        
        count = 0
        for i in range (n):
            if (nums[i] == m):
                count += 1
                
        if (count > n // 2):
            return m
        else:
            return -1
        
# @lc code=end


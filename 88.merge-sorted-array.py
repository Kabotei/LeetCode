#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
import math
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        #Functions
        def getValue(nums,ind,size):
            if ind >= size :
                val = math.inf
            else:
                val = nums[ind]
            return val
        
        #init
        nums3 = nums1[0:m]
        i = 0
        j = 0
        val1 = getValue(nums3,i,m)
        val2 = getValue(nums2,j,n)

        while i < m or j < n:
            if val1 <= val2:
                nums1[i+j] = val1
                i+=1
                val1 = getValue(nums3,i,m)
            elif val1 > val2:
                nums1[i+j] = val2
                j+=1
                val2 = getValue(nums2,j,n)

        m = m+n

      
# @lc code=end


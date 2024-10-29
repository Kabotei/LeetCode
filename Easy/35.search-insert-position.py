#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def getMedian(nums):
            return (len(nums))//2
        
        def quickSearch(nums,target):
            pointeur = getMedian(nums)
            if len(nums) == 1: #point d'arret
                if nums[pointeur] < target:
                    return pointeur+1
                elif nums[pointeur] > target:
                    return pointeur
            
            if nums[pointeur] < target:
                return pointeur + quickSearch(nums[pointeur:len(nums)],target)
            elif nums[pointeur] > target:
                return quickSearch(nums[0:pointeur],target)
            else: # nums[pointeur] = target (arret reccursif)
                return pointeur
        
        return quickSearch(nums,target)
        
# @lc code=end


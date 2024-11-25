#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        visited = set()

        for val in nums:
            if val in visited:
                return True
            else:
                visited.add(val)
        return False
        
# @lc code=end


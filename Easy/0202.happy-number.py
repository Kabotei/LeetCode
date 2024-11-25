#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        def getNext(n: int) -> int:
            som = 0
            while n >0:
                som += (n%10)**2
                n = n//10
            return som
        
        visited = set()
        while n !=1 and n not in visited:
            visited.add(n)
            n = getNext(n)
        
        return n==1

        
        
# @lc code=end


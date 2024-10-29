#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        
        def nonRecursiveFibo(n):
            i=2
            outn1 = 1
            outn2 = 2

            if n == 1:
                return outn1
            elif n == 2:
                return outn2
            
            while i<n:
                temp = outn1 + outn2
                outn1 = outn2
                outn2 = temp
                i+=1
            
            return outn2

        return nonRecursiveFibo(n)
    
        # def fibonnacci(n):
        #     if n == 1:
        #         return 1
        #     elif n == 2:
        #         return 2
        #     else:
        #         return fibonnacci(n-1) + fibonnacci(n-2)
        
        # return fibonnacci(n)
# @lc code=end


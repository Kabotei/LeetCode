#
# @lc app=leetcode id=191 lang=python3
#
# [191] Number of 1 Bits
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        n_bin = "{0:b}".format(n)

        hammingWeight = 0
        for b in n_bin:
            if b == "1":
                hammingWeight+=1
        
        return hammingWeight
# @lc code=end


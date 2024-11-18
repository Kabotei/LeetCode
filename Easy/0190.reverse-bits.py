#
# @lc app=leetcode id=190 lang=python3
#
# [190] Reverse Bits
#

# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        n_bin = "{0:b}".format(n)
        n_bin = n_bin.zfill(32)
        inverted_bin = ""
        for b in n_bin[::-1]:
            inverted_bin += b

        return int(inverted_bin,2)
# @lc code=end


#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        sList = s.split(' ')
        sList = [word for word in sList if len(word)>0]
        return len(sList[-1])
# @lc code=end


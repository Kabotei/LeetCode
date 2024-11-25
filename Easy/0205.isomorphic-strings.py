#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        def getWord(s,t):
            mapping = {}
            word = ""
            for i,c in enumerate(s):
                if c not in mapping:
                    mapping[c] = t[i]
                word += mapping[c]
            return word
        
        word_s = getWord(s,t)
        word_t = getWord(t,s)

        return word_s == t and word_t == s
                

        
# @lc code=end


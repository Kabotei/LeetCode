#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""

        # taille minimum
        sizeMin = 200
        for word in strs:
            if sizeMin > len(word):
                sizeMin = len(word)
        
        # Recherche du prefixe commun le plus long
        for i in range(sizeMin):
            lettre = strs[0][i]
            for word in strs:
                if lettre != word[i]:
                    return prefix
            prefix += lettre

        return prefix

        
# @lc code=end


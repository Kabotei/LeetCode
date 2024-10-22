#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:    
    def romanToInt(self, s: str) -> int:
        symbol = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        value = [1, 5, 10, 50, 100, 500, 1000]
        romanInt = [value[symbol.index(c)] for c in s]
        valeur = 0
        for i in range(1,len(romanInt)):
            if romanInt[i-1] >= romanInt[i]:
                valeur += romanInt[i-1]
            else:
                valeur -= romanInt[i-1]
        valeur += romanInt[-1]
        return valeur
# @lc code=end


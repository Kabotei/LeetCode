#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        def listToInt(digits):
            integer = 0
            for i in range(len(digits)):
                integer+=digits[i]*10**(len(digits)-1-i)
            return integer
        
        def intToList(integer):
            return [int(digit) for digit in str(integer)]
        
        output = listToInt(digits)
        output = intToList(output+1)
        return output

# @lc code=end


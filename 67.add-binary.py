#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def binToInt(binary):
            decimal = 0
            for i,b in enumerate(binary):
                decimal+=int(b)*2**(len(binary)-1-i)
            return decimal
        
        def intToBin(integer):
            quotient = integer//2
            reste = integer%2
            if quotient == 1:
                return str(quotient) + str(reste)
            elif quotient == 0:
                return str(reste)
            else:
                return intToBin(quotient) + str(reste)
        
        def main(a,b):
            aInt = binToInt(a)
            bInt = binToInt(b)

            som = aInt+bInt

            return intToBin(som)
        
        return main(a,b)

        
# @lc code=end


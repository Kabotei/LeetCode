#
# @lc app=leetcode id=168 lang=python3
#
# [168] Excel Sheet Column Title
#

# @lc code=start
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        
        def recursive(n,inds):
            if n <= 26:
                inds.append(n)
                return inds
            else :
                mod = n%26
                n = n//26
                if mod == 0:
                    inds.append(26)
                    n-=1
                else:
                    inds.append(mod)
                recursive(n,inds)
                return inds
        
        converter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        output = ''
        inds = recursive(columnNumber,[])[::-1]
        print(inds)
        for ind in inds:
            output += converter[ind-1]
        
        return output
        
# @lc code=end


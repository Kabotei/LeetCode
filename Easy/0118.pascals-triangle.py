#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        def recursivePascal(n: int) -> List[List[int]]:
            if n == 1:
                return [[1]]
            else:
                triPascal = recursivePascal(n-1)
                lastRow = triPascal[-1]
                newRow = [1]
                for i in range(len(lastRow)-1):
                    newRow.append(lastRow[i]+lastRow[i+1])
                newRow.append(1)
                triPascal.append(newRow)
                return triPascal
        
        return recursivePascal(numRows)
            
# @lc code=end


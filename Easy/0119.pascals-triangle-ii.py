#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def recursivePascal(n):
            if n == 0:
                return [1]
            else:
                lastRow = recursivePascal(n-1)
                newRow = [1]
                for i in range(len(lastRow)-1):
                    newRow.append(lastRow[i]+lastRow[i+1])
                newRow.append(1)
                return newRow
        return recursivePascal(rowIndex)
# @lc code=end


#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        i = 0
        valid = True
        while s != "" and valid:
            if i+1 >= len(s):
                valid = False
            elif s[i] == '(':
                print(s)
                if s[i+1] == ')':
                    s = s[0:i]+s[i+2:len(s)]
                    if i > 0:
                        i-=1
                elif s[i+1] == '(' or s[i+1] == '{' or s[i+1] == '[':
                    i+=1
                else:
                    valid = False
            elif s[i] == '{':
                if s[i+1] == '}':
                    s = s[0:i]+s[i+2:len(s)]
                    if i > 0:
                        i-=1
                elif s[i+1] == '(' or s[i+1] == '{' or s[i+1] == '[':
                    i+=1
                else:
                    valid = False
            elif s[i] == '[':
                if s[i+1] == ']':
                    s = s[0:i]+s[i+2:len(s)]
                    if i > 0:
                        i-=1
                elif s[i+1] == '(' or s[i+1] == '{' or s[i+1] == '[':
                    i+=1
                else:
                    valid = False
            else:
                valid = False
        
        return valid

# @lc code=end
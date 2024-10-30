#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        def preprocess(s: str) -> str:
            #lower case
            s = s.lower()
            #remove non alphanumeric char
            s = ''.join(c for c in s if c.isalnum())
            return s
        
        def palindrome(s: str) -> bool:
            reversed_s = s[::-1]
            for i in range(len(s)):
                if s[i] != reversed_s[i]:
                    return False
            return True
        
        def main(s: str) -> bool:
            s_prepro = preprocess(s)
            return palindrome(s_prepro)
        
        return main(s)

        
# @lc code=end


#
# @lc app=leetcode id=193 lang=bash
#
# [193] Valid Phone Numbers
#
#    patern 1: (xxx) xxx-xxxx                  pattern 2: xxx-xxx-xxxx
# @lc code=start
# Read from the file file.txt and output all valid phone numbers to stdout.
grep -e '^([0-9]\{3\}) [0-9]\{3\}-[0-9]\{4\}$' -e '^[0-9]\{3\}-[0-9]\{3\}-[0-9]\{4\}$' file.txt

# @lc code=end


#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import math
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        while head:
            if head.val == math.inf:
                return True
            head.val = math.inf
            head = head.next
        return False

        
        
# @lc code=end


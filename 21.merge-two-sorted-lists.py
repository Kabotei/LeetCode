#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # init
        output = []

        # merge
        while list1 or list2:
            if list1:
                val1 = list1.val
            else:
                val1 = math.inf
            if list2:
                    val2 = list2.val
            else:
                val2 = math.inf

            if val1 < val2:
                output.append(val1)
                list1 = list1.next
                
            elif val1 == val2:
                output.append(val1)
                output.append(val2)
                list1 = list1.next
                list2 = list2.next
                
            else:
                output.append(val2)
                list2 = list2.next

        # output format
        if output != []:
            outputLN = ListNode(output[-1])
            output.pop()
            for val in output[::-1]:
                outputLN = ListNode(val,next=outputLN)
            return outputLN
        else:
             return None

# @lc code=end


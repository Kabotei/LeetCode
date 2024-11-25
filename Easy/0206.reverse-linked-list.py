#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def linkedListToArray(head: Optional[ListNode]) -> set:
            llist = []
            while head:
                llist.append(head.val)
                head = head.next
            return llist
        def addValToLList(val:int,head: Optional[ListNode]) -> Optional[ListNode]:
            new_head = ListNode(val)
            new_head.next = head
            return new_head
        
        llist = linkedListToArray(head)
        output = None
        for val in llist:
            output = addValToLList(val,output)
        return output
        
# @lc code=end


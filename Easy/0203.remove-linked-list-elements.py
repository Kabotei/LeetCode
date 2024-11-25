#
# @lc app=leetcode id=203 lang=python3
#
# [203] Remove Linked List Elements
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        def linkedListToArray(head: Optional[ListNode]) -> set:
            llist = []
            while head:
                llist.append(head.val)
                head = head.next
            return llist
        
        llist = linkedListToArray(head)

        def addValToLList(val,head=None):
            new_head = ListNode(val)
            new_head.next = head
            return new_head
        
        output = None
        for n in llist[::-1]:
            if n != val:
                output = addValToLList(n,output)
        
        return output

        
# @lc code=end


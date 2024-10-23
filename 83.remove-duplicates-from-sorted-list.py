#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def deleteDupli(LN):
            array = []
            while LN:
                if len(array) == 0:
                    array.append(LN.val)
                else:
                    if LN.val != array[-1]:
                        array.append(LN.val)
                LN = LN.next
            
            return array
        def arrayToListNode(arr):
            if arr != []:
                outputLN = ListNode(arr[-1])
                arr.pop()
                for val in arr[::-1]:
                    outputLN = ListNode(val,next=outputLN)
                return outputLN
            else:
                return None
        
        def main(head):
            return arrayToListNode(deleteDupli(head))
        
        return main(head)
# @lc code=end
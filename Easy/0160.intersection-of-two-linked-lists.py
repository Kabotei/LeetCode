#
# @lc app=leetcode id=160 lang=python3
#
# [160] Intersection of Two Linked Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        def headToArray(head):
            array = []
            while head:
                array.append(head.val)
                head = head.next
            
            return array
        
        def isIntersection(headA, headB):
            while headA.next:
                headA = headA.next
                lastNodeA = headA
            while headB.next:
                headB = headB.next
                lastNodeB = headB
            
            return lastNodeA == lastNodeB
        
        def reduceToSameSize(listA, listB):
            skipA = 0
            skipB = 0

            while len(listA) != len(listB):
                if len(listA) > len(listB):
                    listA.pop(0)
                    skipA +=1
                else:
                    listB.pop(0)
                    skipB +=1
            
            return (skipA, skipB)
        
        def listToHead(array):
            if array == []:
                return None
            old_head = ListNode(array[::-1][0])
            array.pop(-1)
            for val in  array[::-1]:
                new_head = ListNode(val)
                new_head.next = old_head
                old_head = new_head

            return new_head
        
        def skipHead(head, skip):
            if skip == 0:
                return head
            else:
                return skipHead(head.next,skip-1)
        def getIntersection(headA,headB,skipA, skipB):
            #Skipping head
            headA = skipHead(headA, skipA)
            headB = skipHead(headB, skipB)

            #seraching the common linked list
            while headA != headB:
                headA = headA.next
                headB = headB.next
            
            return headA

        listA = headToArray(headA)
        listB = headToArray(headB)
        (skipA, skipB) = reduceToSameSize(listA, listB)
        return getIntersection(headA,headB,skipA, skipB)
        

        
# @lc code=end


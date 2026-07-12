# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carry = 0
        dummy = ListNode()
        res = dummy

        while l1 and l2:
            curSum = l1.val + l2.val + carry
            curVal = curSum % 10
            carry = curSum // 10

            res.next = ListNode(curVal)
            res = res.next
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            curSum = l1.val + carry
            curVal = curSum % 10
            carry = curSum // 10
            res.next = ListNode(curVal)
            res = res.next
            l1 = l1.next
        
        while l2:
            curSum = l2.val + carry
            curVal = curSum % 10
            carry = curSum // 10
            res.next = ListNode(curVal)
            res = res.next
            l2 = l2.next
        
        if carry > 0:
            res.next = ListNode(carry)
        
        return dummy.next
             
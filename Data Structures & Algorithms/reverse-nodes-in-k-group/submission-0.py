# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        curr = head
        prev = dummy

        while curr:
            tail = curr
            count = 0
            while curr and count < k:
                curr = curr.next
                count += 1
            
            
            if count != k:
                prev.next = tail
                break
            else:
                prev.next = self.reverse(tail, k)
                prev = tail

        return dummy.next

    def reverse(self, node, k):
        prev = None
        curr = node

        while curr and k > 0:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            k -= 1
        
        return prev
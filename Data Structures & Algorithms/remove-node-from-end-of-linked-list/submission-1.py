# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            length+=1
            curr=curr.next
        
        diff = length - n
        if diff==0: head=head.next
        else:
            prev = None
            curr = head
            while diff:
                prev = curr
                curr = curr.next
                diff-=1
            prev.next = curr.next
        return head

           






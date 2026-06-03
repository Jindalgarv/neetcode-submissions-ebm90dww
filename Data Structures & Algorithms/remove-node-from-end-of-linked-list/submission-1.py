# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ptr=head
        c=0
        while ptr:
            c+=1
            ptr=ptr.next
        m=c-n
        if m==0:
            return head.next
        curr=head
        for i in range(m-1):
            curr=curr.next
        curr.next=curr.next.next
        return head
        
        
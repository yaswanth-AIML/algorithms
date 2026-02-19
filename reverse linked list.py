# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head ==None or head.next==None:
            return head
        curr=head
        l=[]
        while curr!=None:
            l.append(curr.val)
            curr=curr.next
        curr=head
        while curr!=None:
            curr.val=l.pop()
            curr=curr.next
        return head

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        if not head:
            return None
        if n==1 and head.next is None:
            return None
        temp=head
        count=0
        while temp:
            temp=temp.next
            count+=1
        pos=count-n
        if pos==0:
            Next=head.next
            head=Next
            return head
        count=0
        temp=head
        while temp and temp.next:
            if count==pos-1:
                Next=temp.next.next
                temp.next=Next
            temp=temp.next
            count+=1
        return head
        
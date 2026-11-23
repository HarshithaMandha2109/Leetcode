# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        if not head:
            return None
        prev=None
        temp=head
        while temp:
            Next=temp.next
            temp.next=prev
            prev=temp
            temp=Next
        return prev

        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
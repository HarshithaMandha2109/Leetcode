# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        if not head:
            return None
        temp = head
        prev = None
        while temp:
            if temp.val == val:
                Next = temp.next
                if prev is None:
                    head = Next
                else:
                    prev.next = Next
                temp = Next
            else:
                prev = temp
                temp = temp.next
        return head

        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy=ListNode(-1)
        curr=dummy
        temp1=list1
        temp2=list2
        while temp1 and temp2:
            if temp1.val<=temp2.val:
                curr.next=temp1
                temp1=temp1.next
            else:
                curr.next=temp2
                temp2=temp2.next
            curr=curr.next
        while temp1:
            curr.next=temp1
            temp1=temp1.next
            curr=curr.next
        while temp2:
            curr.next=temp2
            temp2=temp2.next
            curr=curr.next
        return dummy.next
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
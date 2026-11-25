"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
    def flatten(self, head):
        if not head:
            return None
        def flatten_tail(head):
            curr=head
            tail=head
            while curr:
                next=curr.next
                if curr.child:
                    child=curr.child
                    child_tail=flatten_tail(child)
                    curr.next=child
                    child.prev=curr
                    curr.child=None
                    if next:
                        child_tail.next=next
                        next.prev=child_tail
                    curr=child_tail
                tail=curr
                curr=curr.next
            return tail
        flatten_tail(head)
        return head
        